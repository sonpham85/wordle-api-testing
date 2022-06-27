import pytest
from apitest.src.helpers.guess_daily_helper import DailyHelper
from apitest.src.utilities.genericUtilities import generate_random_string


@pytest.mark.tcdaily
def test_get_daily_success():

    daily_helper = DailyHelper()
    number = input(
        "Please input a number for size, remember that size must be greater than 0: "
    )
    while int(number) == 0:
        number = input(
            "Please input a number for size, remember that size can not be 0: "
        )
    size = int(number)
    guess = generate_random_string(length=size)
    daily_json = daily_helper.get_daily(guess=guess, size=size)
    result = ["absent", "present", "correct"]
    result_guess = [c for c in guess]
    for x in range(size):
        assert daily_json[x]["slot"] == x
        assert (
                daily_json[x]["guess"] == result_guess[x]
        ), f"The expected guess is not correct. The expected is: {result_guess[x]} but the actual is: {daily_json[x]['guess']}"
        for i in result:
            if daily_json[x]["result"] == i:
                data = 1
                break
            else:
                data = 0
        assert data == 1


@pytest.mark.tcdaily
def test_get_daily_return_500():

    daily_helper = DailyHelper()
    size = 0
    guess = ""
    expected_status_code = 500
    daily_string = daily_helper.get_daily(
        guess=guess, size=size, expected_status_code=expected_status_code
    )
    assert daily_string == "Internal Server Error"


@pytest.mark.tcdaily
def test_get_daily_return_400():

    daily_helper = DailyHelper()
    number = input(
        "Please input a number for size, remember that size must be greater than 0: "
    )
    while int(number) == 0:
        number = input(
            "Please input a number for size, remember that size can not be 0: "
        )
    size = int(number)
    guess = generate_random_string(length=size)
    expected_status_code = 400
    daily_string = daily_helper.get_daily(
        guess=guess, size=size - 1, expected_status_code=expected_status_code
    )
    assert daily_string == "Guess must be the same length as the word"


@pytest.mark.tcdaily
def test_get_daily_without_required_field_return_422():

    daily_helper = DailyHelper()
    number = input(
        "Please input a number for size, remember that size must be greater than 0: "
    )
    while int(number) == 0:
        number = input(
            "Please input a number for size, remember that size can not be 0: "
        )
    size = int(number)
    expected_status_code = 422
    daily_json = daily_helper.get_daily_without_required_field(
        size=size, expected_status_code=expected_status_code
    )
    assert daily_json["detail"][0]["loc"] == ["query", "guess"]
    assert daily_json["detail"][0]["msg"] == "field required"
    assert daily_json["detail"][0]["type"] == "value_error.missing"


@pytest.mark.tcdaily
def test_get_daily_with_invalid_type_return_422():

    daily_helper = DailyHelper()
    size = "abc"
    expected_status_code = 422
    daily_json = daily_helper.get_daily(
        size=size, expected_status_code=expected_status_code
    )
    assert daily_json["detail"][0]["loc"] == ["query", "size"]
    assert daily_json["detail"][0]["msg"] == "value is not a valid integer"
    assert daily_json["detail"][0]["type"] == "type_error.integer"
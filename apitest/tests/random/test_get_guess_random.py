import pytest
from apitest.src.helpers.guess_random_helper import RandomHelper
from apitest.src.utilities.genericUtilities import generate_random_string


@pytest.mark.tcrandom
def test_get_random_success():

    random_helper = RandomHelper()
    number = input(
        "Please input a number for size, remember that size must be greater than 0: "
    )
    while int(number) == 0:
        number = input(
            "Please input a number for size, remember that size can not be 0: "
        )
    size = int(number)
    guess = generate_random_string(length=size)
    random_json = random_helper.get_random(guess=guess, size=size)
    result = ["absent", "present", "correct"]
    result_guess = [c for c in guess]
    for x in range(size):
        assert random_json[x]["slot"] == x
        assert (
                random_json[x]["guess"] == result_guess[x]
        ), f"The expected guess is not correct. The expected is: {result_guess[x]} but the actual is: {random_json[x]['guess']}"
        for i in result:
            if random_json[x]["result"] == i:
                data = 1
                break
            else:
                data = 0
        assert data == 1


@pytest.mark.tcrandom
def test_get_random_return_500():

    random_helper = RandomHelper()
    size = 0
    guess = ""
    expected_status_code = 500
    random_string = random_helper.get_random(
        guess=guess, size=size, expected_status_code=expected_status_code
    )
    assert random_string == "Internal Server Error"


@pytest.mark.tcrandom
def test_get_random_return_400():

    random_helper = RandomHelper()
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
    random_string = random_helper.get_random(
        guess=guess, size=size - 1, expected_status_code=expected_status_code
    )
    assert random_string == "Guess must be the same length as the word"


@pytest.mark.tcrandom
def test_get_random_without_required_field_return_422():

    random_helper = RandomHelper()
    number = input(
        "Please input a number for size, remember that size must be greater than 0: "
    )
    while int(number) == 0:
        number = input(
            "Please input a number for size, remember that size can not be 0: "
        )
    size = int(number)
    expected_status_code = 422
    random_json = random_helper.get_random_without_required_field(
        size=size, expected_status_code=expected_status_code
    )
    assert random_json["detail"][0]["loc"] == ["query", "guess"]
    assert random_json["detail"][0]["msg"] == "field required"
    assert random_json["detail"][0]["type"] == "value_error.missing"


@pytest.mark.tcrandom
def test_get_random_with_invalid_type_return_422():

    random_helper = RandomHelper()
    size = "abc"
    seed = "abc"
    expected_status_code = 422
    random_json = random_helper.get_random(
        size=size, seed=seed, expected_status_code=expected_status_code
    )
    assert random_json["detail"][0]["loc"] == ["query", "size"]
    assert random_json["detail"][1]["loc"] == ["query", "seed"]
    assert (
        random_json["detail"][0]["msg"]
        == random_json["detail"][1]["msg"]
        == "value is not a valid integer"
    )
    assert (
        random_json["detail"][0]["type"]
        == random_json["detail"][1]["type"]
        == "type_error.integer"
    )

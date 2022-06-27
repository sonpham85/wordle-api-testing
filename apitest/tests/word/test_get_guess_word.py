import pytest
from apitest.src.helpers.guess_word_helper import WordHelper
from apitest.src.utilities.genericUtilities import generate_random_string


@pytest.mark.tcword
def test_get_word_success():

    word_helper = WordHelper()
    number = input(
        "Please input a number for size, remember that size must be greater than 0: "
    )
    while int(number) == 0:
        number = input(
            "Please input a number for size, remember that size can not be 0: "
        )
    size = int(number)
    guess = generate_random_string(length=size)
    word = generate_random_string(length=size)
    word_json = word_helper.get_word(guess=guess, word=word)
    result = ["absent", "present", "correct"]
    result_guess = [c for c in guess]
    for x in range(size):
        assert word_json[x]["slot"] == x
        assert (
            word_json[x]["guess"] == result_guess[x]
        ), f"The expected guess is not correct. The expected is: {result_guess[x]} but the actual is: {word_json[x]['guess']}"
        for i in result:
            if word_json[x]["result"] == i:
                data = 1
                break
            else:
                data = 0
        assert data == 1


@pytest.mark.tcword
def test_get_word_return_400():

    word_helper = WordHelper()
    number = input(
        "Please input a number for size, remember that size must be greater than 0: "
    )
    while int(number) == 0:
        number = input(
            "Please input a number for size, remember that size can not be 0: "
        )
    size = int(number)
    guess = generate_random_string(length=size)
    word = generate_random_string(length=size + 1)
    expected_status_code = 400
    word_string = word_helper.get_word(
        guess=guess, word=word, expected_status_code=expected_status_code
    )
    assert word_string == "Guess must be the same length as the word"


@pytest.mark.tcword
def test_get_word_without_required_field_return_404():

    word_helper = WordHelper()
    expected_status_code = 404
    word_json = word_helper.get_word(word="", expected_status_code=expected_status_code)
    assert word_json["detail"] == "Not Found"


@pytest.mark.tcword
def test_get_word_without_required_field_return_422():

    word_helper = WordHelper()
    expected_status_code = 422
    word_json = word_helper.get_word_without_required_field(
        expected_status_code=expected_status_code
    )
    assert word_json["detail"][0]["loc"] == ["query", "guess"]
    assert word_json["detail"][0]["msg"] == "field required"
    assert word_json["detail"][0]["type"] == "value_error.missing"

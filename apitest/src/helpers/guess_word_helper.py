from apitest.src.utilities.requestsUtility import RequestsUtility
import json
import os


class WordHelper(object):
    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.request_helper = RequestsUtility()

    def get_word(self, guess="a", word="a", expected_status_code=200):

        rs_api = self.request_helper.get(
            f"word/{word}?guess={guess}",
            headers={"Content-Type": "application/json"},
            expected_status_code=expected_status_code,
        )
        return rs_api

    def get_word_without_required_field(self, word="a", expected_status_code=422):

        rs_api = self.request_helper.get(
            f"word/{word}",
            headers={"Content-Type": "application/json"},
            expected_status_code=expected_status_code,
        )
        return rs_api

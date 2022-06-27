from apitest.src.utilities.requestsUtility import RequestsUtility
import json
import os


class RandomHelper(object):
    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.request_helper = RequestsUtility()

    def get_random(self, guess="abcde", size=5, seed=1, expected_status_code=200):

        rs_api = self.request_helper.get(
            f"random?guess={guess}&size={size}&seed={seed}",
            headers={"Content-Type": "application/json"},
            expected_status_code=expected_status_code,
        )
        return rs_api

    def get_random_without_required_field(self, size=5, seed=1, expected_status_code=422):

        rs_api = self.request_helper.get(
            f"random?size={size}&seed={seed}",
            headers={"Content-Type": "application/json"},
            expected_status_code=expected_status_code,
        )
        return rs_api

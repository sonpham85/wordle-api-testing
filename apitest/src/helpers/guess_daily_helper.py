from apitest.src.utilities.requestsUtility import RequestsUtility
import json
import os


class DailyHelper(object):
    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.request_helper = RequestsUtility()

    def get_daily(self, guess="abcde", size=5, expected_status_code=200):

        rs_api = self.request_helper.get(
            f"daily?guess={guess}&size={size}",
            headers={"Content-Type": "application/json"},
            expected_status_code=expected_status_code,
        )
        return rs_api

    def get_daily_without_required_field(self, size=5, expected_status_code=200):

        rs_api = self.request_helper.get(
            f"daily?size={size}",
            headers={"Content-Type": "application/json"},
            expected_status_code=expected_status_code,
        )
        return rs_api

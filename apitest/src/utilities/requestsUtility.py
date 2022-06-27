from apitest.src.configs.hosts_config import API_HOSTS
import requests
import os
import json


class RequestsUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]


    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status code" \
              f" Expected: {self.expected_status_code}, actual status code {self.status_code}" \
                                                                 f" Url: {self.url}"

    def return_response(self, response_string):
        try:
            self.rs_json = json.loads(response_string)
        except ValueError as e:
            self.rs_json = response_string
        return self.rs_json

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = self.return_response(rs_api.text)
        #self.rs_json = rs_api.json()
        self.assert_status_code()

        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = self.return_response(rs_api.text)
        #self.rs_json = rs_api.json()
        self.assert_status_code()

        return self.rs_json

    def put(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.put(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = self.return_response(rs_api.text)
        #self.rs_json = rs_api.json()
        self.assert_status_code()

        return self.rs_json
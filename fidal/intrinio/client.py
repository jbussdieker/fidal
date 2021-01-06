import logging
import os
import requests

class Client:
    def __init__(self):
        self.base_url = "https://api-v2.intrinio.com"
        self.token = os.environ.get("INTRINIO_KEY", "")
        self._session = None

    @property
    def session(self):
        if self._session == None:
            self._session = requests.session()
        return self._session

    def _validate_response(self, response):
        if response.status_code != requests.codes.ok:
            raise Exception("Error Response")

    def request(self, endpoint, params={}):
        params.update({"api_key": self.token})
        url = "/".join([self.base_url, endpoint])
        response = self.session.get(url=url, params=params)
        self._validate_response(response)
        return response.json()

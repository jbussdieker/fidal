import logging
import os
import requests

class Client:
    def __init__(self):
        self.base_url = "https://api.polygon.io"
        self.version = "v2"
        self.token = os.environ.get("POLYGON_KEY", "")
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
        params.update({"apiKey": self.token})
        url = "/".join([self.base_url, self.version, endpoint])
        response = self.session.get(url=url, params=params)
        self._validate_response(response)
        return response.json()

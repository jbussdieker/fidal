import logging
import os
import requests

class Client:
    def __init__(self):
        self.base_url = "https://paper-api.alpaca.markets"
        self.version = "v2"
        self.key_id = os.environ.get("APCA_API_KEY_ID", "")
        self.secret_key = os.environ.get("APCA_API_SECRET_KEY", "")
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
        url = "/".join([self.base_url, self.version, endpoint])
        response = self.session.get(url=url, params=params, headers={
            "APCA-API-KEY-ID": self.key_id,
            "APCA-API-SECRET-KEY": self.secret_key})
        self._validate_response(response)
        return response.json()

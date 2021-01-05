import logging
import os
import requests

class Client:
    def __init__(self):
        self.base_url = "https://cloud.iexapis.com"
        self.version = "stable"
        self.token = os.environ.get("IEX_TOKEN", "")
        self._session = None

    @property
    def session(self):
        if self._session == None:
            self._session = requests.session()
        return self._session

    def _log_messages(self, response):
        key = "iexcloud-messages-used"
        msg = "N/A"
        if key in response.headers:
            msg = response.headers[key]
        logging.warning("MESSAGES USED: %s" % msg)

    def _validate_response(self, response):
        if response.status_code != requests.codes.ok:
            raise Exception("Error Response")
        if response.text == "Unknown symbol":
            raise Exception("Unknown symbol")

    def request(self, endpoint, params={}):
        params.update({"token": self.token})
        url = "/".join([self.base_url, self.version, endpoint])
        response = self.session.get(url=url, params=params)
        self._log_messages(response)
        self._validate_response(response)
        json_response = response.json(
            parse_int=None, parse_float=None
        )
        if isinstance(json_response, str) and ("Error Message" in json_response):
            raise Exception("Error Message")
        return json_response

import unittest
from unittest.mock import MagicMock, patch

from iex.client import Client
import requests

class TestClient(unittest.TestCase):
    def run(self, result=None):
        with patch('logging.warning') as mock_logging:
            with patch('requests.session') as mock_session:
                self.mock_session = mock_session
                self.mock_logging = mock_logging
                self.session = MagicMock()
                self.mock_session.return_value = self.session
                self.response = MagicMock(status_code=requests.codes.ok, text="[]", headers={})
                self.session.get.return_value = self.response
                self.response.json.return_value = []
                self.client = Client()
                super().run(result)

    def test_request(self):
        self.response.json.return_value = [{}, {}]
        resp = self.client.request("ref-data/iex/symbols")
        self.assertEqual(len(resp), 2)

    def test_request_messages_used_logging(self):
        self.response.headers = {"iexcloud-messages-used": "10"}
        resp = self.client.request("ref-data/iex/symbols")
        self.mock_logging.assert_called_once_with("MESSAGES USED: 10")

    def test_request_error_code_handling(self):
        self.response.status_code = -1
        self.assertRaises(Exception, self.client.request, "ref-data/iex/symbols")

    def test_request_unknown_symbol_handling(self):
        self.response.text = "Unknown symbol"
        self.assertRaises(Exception, self.client.request, "ref-data/iex/symbols")

    def test_request_error_message_handling(self):
        self.response.json.return_value = "Error Message: Blah blah"
        self.assertRaises(Exception, self.client.request, "ref-data/iex/symbols")

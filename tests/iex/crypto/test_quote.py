import unittest
from unittest.mock import MagicMock, patch

from tests.helper import get_vcr
from fidal.iex.crypto.quote import fetch

vcr = get_vcr("iex/crypto/quote")

class TestIEXCryptoQuote(unittest.TestCase):
    @vcr.use_cassette()
    def test_fetch(self):
        with patch('logging.debug') as mock_logging:
            resp = fetch("BTCUSD")
            self.assertEqual(len(resp), 11)
            mock_logging.assert_called_once_with("MESSAGES USED: 2")

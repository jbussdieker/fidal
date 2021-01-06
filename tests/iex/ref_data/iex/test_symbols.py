import unittest
from unittest.mock import MagicMock, patch

from tests.helper import get_vcr
from fidal.iex.ref_data.iex.symbols import fetch

vcr = get_vcr('iex/ref_data/iex/symbols')

class TestIEXRefDataIEXSymbols(unittest.TestCase):
    @vcr.use_cassette()
    def test_fetch(self):
        with patch('logging.debug') as mock_logging:
            resp = fetch()
            self.assertEqual(len(resp), 9546)
            mock_logging.assert_called_once_with("MESSAGES USED: 0")

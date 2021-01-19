import unittest
from unittest.mock import MagicMock, patch

from tests.helper import get_vcr
from fidal.iex.time_series import fetch

vcr = get_vcr('iex/time_series')

class TestIEXTimeSeries(unittest.TestCase):
    @vcr.use_cassette()
    def test_fetch(self):
        with patch('logging.debug') as mock_logging:
            resp = fetch()
            self.assertEqual(len(resp), 92)
            mock_logging.assert_called_once_with("MESSAGES USED: 0")

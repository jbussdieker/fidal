import unittest
import vcr
import requests

from unittest.mock import MagicMock, patch

from fin.intrinio.companies import fetch

iexvcr = vcr.VCR(path_transformer=vcr.VCR.ensure_suffix('.yaml'),
                 cassette_library_dir='tests/fixtures/cassettes/intrinio/companies',
                 decode_compressed_response=True,
                 filter_query_parameters=['api_key'])

class TestIntrinioCompanies(unittest.TestCase):
    @iexvcr.use_cassette()
    def test_fetch(self):
        resp = fetch()
        self.assertEqual(len(resp), 2)

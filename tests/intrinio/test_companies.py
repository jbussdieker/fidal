import unittest

from tests.helper import get_vcr
from fidal.intrinio.companies import fetch

vcr = get_vcr("intrinio/companies")

class TestIntrinioCompanies(unittest.TestCase):
    @vcr.use_cassette()
    def xtest_fetch(self):
        resp = fetch()
        self.assertEqual(len(resp), 2)

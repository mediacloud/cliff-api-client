import unittest
import os
from api import Cliff
from dotenv import load_dotenv

# load env-vars from .env file if there is one
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
test_env = os.path.join(basedir, '.env')
if os.path.isfile(test_env):
    load_dotenv(dotenv_path=os.path.join(basedir, '.env'), verbose=True)

GEONAME_LONDON_UK = 2643743
GEONAME_LONDERRY_NH = 5088905


class BasicCliffTest(unittest.TestCase):
    # A basic set of test cases to make sure the API can pull from the server correctly.

    def setUp(self):
        self._url = os.getenv("CLIFF_URL")
        self._cliff = Cliff(self._url)

    def test_parse_text(self):
        results = self._cliff.parse_text("This is about Einstien at the IIT in New Delhi.")
        results = results['results']
        self.assertEqual(len(results['organizations']), 1)
        self.assertEqual(len(results['places']['mentions']), 1)
        self.assertEqual(results['places']['mentions'][0]['id'], 1261481)
        self.assertEqual(len(results['people']), 1)

    def test_extract_content(self):
        test_url = "https://www.foxnews.com/us/temple-university-stands-by-marc-lamont-hill-after-cnn-fires-him-for-anti-israel-remarks"
        results = self._cliff.extract_content(test_url)
        results = results['results']
        self.assertEqual(test_url, results['url'])
        self.assertTrue(len(results['text']) > 100)

    def test_geonames_lookup(self):
        results = self._cliff.geonames_lookup(4943351)
        self.assertEqual(results['id'], 4943351)
        self.assertEqual(results['lon'], -71.09172)
        self.assertEqual(results['lat'], 42.35954)
        self.assertEqual(results['name'], "Massachusetts Institute of Technology")
        self.assertEqual(results['parent']['name'], "City of Cambridge")
        self.assertEqual(results['parent']['parent']['name'], "Middlesex County")
        self.assertEqual(results['parent']['parent']['parent']['name'], "Massachusetts")
        self.assertEqual(results['parent']['parent']['parent']['parent']['name'], "United States")

    def test_local_replacements(self):
        replacements = {
            'Londonderry': 'London',
        }
        # make sure non-replaced fetches the city in the UK
        results = self._cliff.parse_text("This is about London.")['results']
        mention = results['places']['mentions'][0]
        self.assertEqual(GEONAME_LONDON_UK, mention['id'])
        # now see if it gets the city with replacements
        replacing_cliff = Cliff(self._url, text_replacements=replacements)
        results = replacing_cliff.parse_text("This is about London.")['results']
        replaced_mention = results['places']['mentions'][0]
        self.assertEqual(GEONAME_LONDERRY_NH, replaced_mention['id'])

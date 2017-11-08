import unittest
import ConfigParser
from api import Cliff

GEONAME_LONDON_UK = 2643743
GEONAME_LONDERRY_NH = 5088905


class BasicCliffTest(unittest.TestCase):
    # A basic set of test cases to make sure the API can pull from the server correctly.

    def setUp(self):
        self._config = ConfigParser.ConfigParser()
        self._config.read('settings.config')
        self._cliff = Cliff(self._config.get('cliff', 'url'))

    def test_parse_text(self):
        results = self._cliff.parse_text("This is about Einstien at the IIT in New Delhi.")['results']
        self.assertEqual(len(results['organizations']), 1)
        self.assertEqual(len(results['places']['mentions']), 1)
        self.assertEqual(results['places']['mentions'][0]['id'], 1261481)
        self.assertEqual(len(results['people']), 1)

    def test_extract_content(self):
        test_url = "http://www.foxnews.com/sports/2017/10/16/national-anthem-protests-florida-man-takes-boycott-jags-and-nfl-message-to-sky.html"
        results = self._cliff.extract_content(test_url)
        results = results['results']
        self.assertEqual(test_url, results['url'])
        self.assertTrue(len(results['title']) > 50)
        self.assertTrue(len(results['text']) > 100)

    def test_geonames_lookup(self):
        results = self._cliff.geonames_lookup(4943351)
        self.assertEqual(results['id'], 4943351)
        self.assertEqual(results['lon'], -71.09172)
        self.assertEqual(results['lat'], 42.35954)
        self.assertEqual(results['name'], "Massachusetts Institute of Technology")
        self.assertEqual(results['parent']['name'], "Middlesex County")
        self.assertEqual(results['parent']['parent']['name'], "Massachusetts")

    def test_local_replacements(self):
        replacements = {
            'Londonderry': 'London',
        }
        # make sure non-replaced fetches the city in the UK
        results = self._cliff.parse_text("This is about London.")['results']
        mention = results['places']['mentions'][0]
        self.assertEqual(GEONAME_LONDON_UK, mention['id'])
        # now see if it gets the city with replacements
        replacing_cliff = Cliff(self._config.get('cliff', 'url'), text_replacements=replacements)
        results = replacing_cliff.parse_text("This is about London.")['results']
        replaced_mention = results['places']['mentions'][0]
        self.assertEqual(GEONAME_LONDERRY_NH, replaced_mention['id'])

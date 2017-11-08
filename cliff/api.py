import logging
import json
import requests


class Cliff:
    """Make requests to a CLIFF geo-parsing / NER server"""

    PARSE_TEXT_PATH = "/cliff-2.4.1/parse/text"
    PARSE_NLP_JSON_PATH = "/cliff-2.4.1/parse/json"
    PARSE_SENTENCES_PATH = "/cliff-2.4.1/parse/sentences"
    GEONAMES_LOOKUP_PATH = "/cliff-2.4.1/geonames"
    EXTRACT_TEXT_PATH = "/cliff-2.4.1/extract"

    JSON_PATH_TO_ABOUT_COUNTRIES = 'results.places.about.countries'

    STATUS_OK = "ok"

    def __init__(self, host, port, text_replacements=None):
        self._log = logging.getLogger(__name__)
        self._host = host
        self._port = int(port)
        self._replacements = text_replacements if text_replacements is not None else {}
        self._log.info("initialized CLIFF @ %s:%d", self._host, self._port)

    def parse_text(self, text, demonyms=False):
        cleaned_text = self._get_replaced_text(text)
        return self._parse_query(self.PARSE_TEXT_PATH, cleaned_text, demonyms)

    def parse_sentences(self, json_object, demonyms=False):
        return self._parse_query(self.PARSE_SENTENCES_PATH, json.dumps(json_object), demonyms)

    def geonames_lookup(self, geonames_id):
        return self._query(self.GEONAMES_LOOKUP_PATH, {'id': geonames_id})['results']

    def extract_content(self, url):
        # uses the boilerpipe engine
        return self._get_query(self.EXTRACT_TEXT_PATH, {'url': url})

    def _demonyms_text(self, demonyms=False):
        return "true" if demonyms else "false"

    def _url_to(self, path):
        return self._host+":"+str(self._port)+path

    def _get_replaced_text(self, text):
        replaced_text = text
        for replace, find in self._replacements.items():
            replaced_text = text.replace(find, replace)
        return replaced_text

    def _parse_query(self, path, text, demonyms=False):
        payload = {'q': text, 'replaceAllDemonyms': self._demonyms_text(demonyms)}
        self._log.debug("Querying %r (demonyms=%r)", path, demonyms)
        return self._query(path, payload)
    
    def _query(self, path, args):
        try:
            url = self._url_to(path)
            r = requests.post(url, data=args)
            self._log.debug('CLIFF says %r', r.content)
            return r.json()
        except requests.exceptions.RequestException as e:
            self._log.exception(e)
        return ""

    def _get_query(self, path, args):
        try:
            url = self._url_to(path)
            r = requests.get(url, params=args)
            self._log.debug('CLIFF says %r', r.content)
            return r.json()
        except requests.exceptions.RequestException as e:
            self._log.exception(e)
        return ""

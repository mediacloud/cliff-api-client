import logging
import json
import requests

DEFAULT_TIMEOUT = 30

class Cliff:
    # Make requests to a CLIFF geo-parsing / NER server

    PARSE_TEXT_PATH = "/cliff-2.6.1/parse/text"
    PARSE_NLP_JSON_PATH = "/cliff-2.6.1/parse/json"
    PARSE_SENTENCES_PATH = "/cliff-2.6.1/parse/sentences"
    GEONAMES_LOOKUP_PATH = "/cliff-2.6.1/geonames"
    EXTRACT_TEXT_PATH = "/cliff-2.6.1/extract"

    GERMAN = "DE";
    SPANISH = "ES";
    ENGLISH = "EN";

    JSON_PATH_TO_ABOUT_COUNTRIES = 'results.places.about.countries'

    STATUS_OK = "ok"

    def __init__(self, url, text_replacements=None, timeout=DEFAULT_TIMEOUT):
        self._log = logging.getLogger(__name__)
        self._url = url
        self._timeout = timeout
        self._replacements = text_replacements if text_replacements is not None else {}
        self._log.info("initialized CLIFF @ {}".format(url))

    def parse_text(self, text, demonyms=False, language=ENGLISH):
        cleaned_text = self._get_replaced_text(text)
        return self._parse_query(self.PARSE_TEXT_PATH, cleaned_text, demonyms, language)

    def parse_sentences(self, json_object, demonyms=False, language=ENGLISH):
        return self._parse_query(self.PARSE_SENTENCES_PATH, json.dumps(json_object), demonyms, language)

    def geonames_lookup(self, geonames_id):
        return self._query(self.GEONAMES_LOOKUP_PATH, {'id': geonames_id})['results']

    def extract_content(self, url):
        # uses the boilerpipe engine
        return self._get_query(self.EXTRACT_TEXT_PATH, {'url': url})

    def _demonyms_text(self, demonyms=False):
        return "true" if demonyms else "false"

    def _url_to(self, path):
        return "{}{}".format(self._url, path)

    def _get_replaced_text(self, text):
        replaced_text = text
        for replace, find in self._replacements.items():
            replaced_text = text.replace(find, replace)
        return replaced_text

    def _parse_query(self, path, text, demonyms=False, language=ENGLISH):
        payload = {'q': text, 'replaceAllDemonyms': self._demonyms_text(demonyms), 'language': language}
        self._log.debug("Querying %r (demonyms=%r)", path, demonyms)
        return self._query(path, payload)

    def _query(self, path, args):
        url = self._url_to(path)
        r = requests.post(url, data=args, timeout=self._timeout)
        self._log.debug('CLIFF says %r', r.content)
        return r.json()

    def _get_query(self, path, args):
        try:
            url = self._url_to(path)
            r = requests.get(url, params=args)
            self._log.debug('CLIFF says %r', r.content)
            return r.json()
        except requests.exceptions.RequestException as e:
            self._log.exception(e)
        return ""

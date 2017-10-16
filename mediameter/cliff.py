import logging, json
import requests

class Cliff():
    """Make requests to a CLIFF geo-parsing / NER server"""

    PARSE_TEXT_PATH = "/cliff-2.4.1/parse/text"
    PARSE_NLP_JSON_PATH = "/cliff-2.4.1/parse/json"
    PARSE_SENTENCES_PATH = "/cliff-2.4.1/parse/sentences"
    GEONAMES_LOOKUP_PATH = "/cliff-2.4.1/geonames"
    EXTRACT_TEXT_PATH = "/cliff-2.4.1/extract"

    JSON_PATH_TO_ABOUT_COUNTRIES = 'results.places.about.countries'

    STATUS_OK = "ok"

    def __init__(self, host, port, text_replacements={}):
        self._log = logging.getLogger(__name__)
        self._host = host
        self._port = int(port)
        self._replacements = text_replacements
        self._log.info("initialized CLIFF @ %s:%d", self._host, self._port)

    def parseText(self, text, demonyms=False):
        cleaned_text = self._getReplacedText(text)
        return self._parseQuery(self.PARSE_TEXT_PATH, cleaned_text , demonyms)

    def parseSentences(self, json_object, demonyms=False):
        return self._parseQuery(self.PARSE_SENTENCES_PATH, json.dumps(json_object), demonyms)

    def parseNlpJson(self, json_object, demonyms=False):
        return self._parseQuery(self.PARSE_NLP_JSON_PATH, json.dumps(json_object), demonyms)

    def geonamesLookup(self, geonames_id):
        return self._query(self.GEONAMES_LOOKUP_PATH, {'id': geonames_id})['results']

    def extractContent(self, url):
        return self._getQuery(self.EXTRACT_TEXT_PATH, {'url': url})

    def _demonymsText(self, demonyms=False):
        return "true" if demonyms else "false"

    def _urlTo(self, path):
        return self._host+":"+str(self._port)+path

    def _getReplacedText(self, text):
        replaced_text = text
        for replace, find in self._replacements.items():
            replaced_text = text.replace(find, replace)
        return replaced_text

    def _parseQuery(self, path, text, demonyms=False):
        payload = {'q': text, 'replaceAllDemonyms': self._demonymsText(demonyms)}
        self._log.debug("Querying %r (demonyms=%r)", path, demonyms)
        return self._query(path,payload)
    
    def _query(self, path, args):
        try:
            url = self._urlTo(path)
            r = requests.post(url, data=args)
            self._log.debug('CLIFF says %r', r.content)
            return r.json()
        except requests.exceptions.RequestException as e:
            self._log.exception(e)
        return ""

    def _getQuery(self, path, args):
        try:
            url = self._urlTo(path)
            r = requests.get(url, params=args)
            self._log.debug('CLIFF says %r', r.content)
            return r.json()
        except requests.exceptions.RequestException as e:
            self._log.exception(e)
        return ""

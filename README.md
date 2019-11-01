Media CLoud CLIFF API Client
===========================

This is a simple Python client for the [Media Cloud CLIFF-CLAVIN geocoder](http://cliff.mediacloud.org).

Usage
-----

If you just want to use this library to talk to a CLIFF server you have running somewhere, 
first install it

```
pip install mediacloud-cliff
```

Then instantiate and use it like this:

```python
from cliff.api import Cliff
my_cliff = Cliff('http://myserver.com:8080')
my_cliff.parse_text("This is about Einstien at the IIT in New Delhi.")
```

This will return results like this:
```json
{
  "results": {
    "organizations": [
      {
        "count": 1,
        "name": "IIT"
      }
    ],
    "places": {
      "focus": {
        "cities": [
          {
            "id": 1261481,
            "lon": 77.22445,
            "name": "New Delhi",
            "score": 1,
            "countryGeoNameId": "1269750",
            "countryCode": "IN",
            "featureCode": "PPLC",
            "featureClass": "P",
            "stateCode": "07",
            "lat": 28.63576,
            "stateGeoNameId": "1273293",
            "population": 317797
          }
        ],
        "states": [
          {
            "id": 1273293,
            "lon": 77.1,
            "name": "National Capital Territory of Delhi",
            "score": 1,
            "countryGeoNameId": "1269750",
            "countryCode": "IN",
            "featureCode": "ADM1",
            "featureClass": "A",
            "stateCode": "07",
            "lat": 28.6667,
            "stateGeoNameId": "1273293",
            "population": 16787941
          }
        ],
        "countries": [
          {
            "id": 1269750,
            "lon": 79,
            "name": "Republic of India",
            "score": 1,
            "countryGeoNameId": "1269750",
            "countryCode": "IN",
            "featureCode": "PCLI",
            "featureClass": "A",
            "stateCode": "00",
            "lat": 22,
            "stateGeoNameId": "",
            "population": 1173108018
          }
        ]
      },
      "mentions": [
        {
          "id": 1261481,
          "lon": 77.22445,
          "source": {
            "charIndex": 37,
            "string": "New Delhi"
          },
          "name": "New Delhi",
          "countryGeoNameId": "1269750",
          "countryCode": "IN",
          "featureCode": "PPLC",
          "featureClass": "P",
          "stateCode": "07",
          "confidence": 1,
          "lat": 28.63576,
          "stateGeoNameId": "1273293",
          "population": 317797
        }
      ]
    },
    "people": [
      {
        "count": 1,
        "name": "Einstien"
      }
    ]
  },
  "status": "ok",
  "milliseconds": 22,
  "version": "2.5.0"
}
```

You can also just get info from the GeoNames database inside CLIFF:
```python
from cliff.api import Cliff
my_cliff = Cliff('http://myserver.com:8080')
my_cliff.geonames_lookup(4943351)
```

This will give you results like this:
```json
{
  "results": {
    "id": 4943351,
    "lon": -71.09172,
    "name": "Massachusetts Institute of Technology",
    "countryGeoNameId": "6252001",
    "countryCode": "US",
    "featureCode": "SCH",
    "featureClass": "S",
    "parent": {
      "id": 4943909,
      "lon": -71.39184,
      "name": "Middlesex County",
      "countryGeoNameId": "6252001",
      "countryCode": "US",
      "featureCode": "ADM2",
      "featureClass": "A",
      "parent": {
        "id": 6254926,
        "lon": -71.10832,
        "name": "Massachusetts",
        "countryGeoNameId": "6252001",
        "countryCode": "US",
        "featureCode": "ADM1",
        "featureClass": "A",
        "parent": {
          "id": 6252001,
          "lon": -98.5,
          "name": "United States",
          "countryGeoNameId": "6252001",
          "countryCode": "US",
          "featureCode": "PCLI",
          "featureClass": "A",
          "stateCode": "00",
          "lat": 39.76,
          "stateGeoNameId": "",
          "population": 310232863
        },
        "stateCode": "MA",
        "lat": 42.36565,
        "stateGeoNameId": "6254926",
        "population": 6433422
      },
      "stateCode": "MA",
      "lat": 42.48555,
      "stateGeoNameId": "6254926",
      "population": 1503085
    },
    "stateCode": "MA",
    "lat": 42.35954,
    "stateGeoNameId": "6254926",
    "population": 0
  },
  "status": "ok",
  "version": "2.5.0"
}
```

Development
-----------

If you want to work on this API client, then first clone [the source repo from GitHub](https://github.com/mitmedialab/CLIFF-API-Client)
and install the dependencies
```
nmake install
```

Then copy `settings.config.sample` to `settings.config` and put in the url and port of your CLIFF 
server.  Now you should be able to develop!

## Distribution

1. Run `make test` to make sure all the test pass
2. Update the version number in `cliff/__init__.py`
3. Make a brief note in the version history section below about the changes
4. Run `make build-release` to create an install package
5. Run `make release-test` to upload it to PyPI's test platform
6. Run `make release` to upload it to PyPI


Version History
---------------

* __v2.5.0__: upgrade to CLIFF v2.5.0 (and keep version numbers roughly in sync)
* __v2.1.0__: upgrade to CLIFF v2.4.2
* __v2.0.2__: update examples in readme file
* __v2.0.1__: init with url instead of host/port
* __v2.0.0__: move to mediacloud naming, underscored method names, remove deprecated NLP endpoint
* __v1.4.0__: upgrade to CLIFF v2.4.1, add support for extractContent endpoint
* __v1.3.1__: updates for python3
* __v1.3.0__: updates for python3, support for client-side text replacements
* __v1.2.0__: points at CLIFF v2.3.0 (updates Stanford NER & has new plugin architecture)
* __v1.1.0__: points at CLIFF v2.2.0 (adds ancestry to `geonamesLookup` helper)
* __v1.0.2__: first release to PyPI


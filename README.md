MediaMeter CLIFF API Client
===========================

This is a simple Python client for the [MediaMeter CLIFF-CLAVIN geocoder](http://cliff.mediameter.org).

Usage
-----

If you just want to use this library to talk to a CLIFF server you have running somewhere, 
first install it

```
pip install mediameter-cliff
```

Then instantiate and use it like this:

```python
from mediameter.cliff import Cliff
my_cliff = Cliff('http://myserver.com',8080)
my_cliff.parseText("This is about Einstien at the IIT in New Delhi.")
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
  "version": "2.1.1"
}
```

You can also just get info from the GeoNames database inside CLIFF:
```python
from mediameter.cliff import Cliff
my_cliff = Cliff('http://myserver.com',8080)
my_cliff.geonamesLookup(4943351)
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
    "stateCode": "MA",
    "lat": 42.35954,
    "stateGeoNameId": "6254926",
    "population": 0
  },
  "status": "ok",
  "version": "2.1.1"
}
```

Development
-----------

If you want to work on this API client, then first clone this repo and install the dependencies
```
pip install -r requirements.pip
```

Then copy `settings.config.sample` to `settings.config` and put in the url and port of your CLIFF 
server.  Now you should be able to develop!

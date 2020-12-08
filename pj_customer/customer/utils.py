import requests

from django.conf import settings

GOOGLE_GEOCODING_API = 'https://maps.googleapis.com/maps/api/geocode/json'


def get_coordinates_from_address_info(address_info: dict, silent: bool = False) -> dict:
    """
    Util Function to extract latitude and longitude from data returned by Geocoding API.
    Returns:
        Dictionary with the follow structure:
        {
           "lat" : 37.4267861,
           "lng" : -122.0806032
        }
    """
    try:
        results = address_info['results']
        address = results[0]
        geo_data = address['geometry']
        return geo_data['location']
    except (KeyError, IndexError):
        if silent:
            return {}
        raise


def get_address_info(address: str, silent: bool = False) -> dict:
    """
    Function to get address information using google Geocoding API
    Returns:
        Example api response.
        {
            "results" : [
              {
                 "address_components" : [
                    {
                       "long_name" : "1600",
                       "short_name" : "1600",
                       "types" : [ "street_number" ]
                    },
                    {
                       "long_name" : "Amphitheatre Parkway",
                       "short_name" : "Amphitheatre Pkwy",
                       "types" : [ "route" ]
                    },
                    {
                       "long_name" : "Mountain View",
                       "short_name" : "Mountain View",
                       "types" : [ "locality", "political" ]
                    },
                    {
                       "long_name" : "Santa Clara County",
                       "short_name" : "Santa Clara County",
                       "types" : [ "administrative_area_level_2", "political" ]
                    },
                    {
                       "long_name" : "California",
                       "short_name" : "CA",
                       "types" : [ "administrative_area_level_1", "political" ]
                    },
                    {
                       "long_name" : "United States",
                       "short_name" : "US",
                       "types" : [ "country", "political" ]
                    },
                    {
                       "long_name" : "94043",
                       "short_name" : "94043",
                       "types" : [ "postal_code" ]
                    }
                 ],
                 "formatted_address" : "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA",
                 "geometry" : {
                    "location" : {
                       "lat" : 37.4267861,
                       "lng" : -122.0806032
                    },
                    "location_type" : "ROOFTOP",
                    "viewport" : {
                       "northeast" : {
                          "lat" : 37.4281350802915,
                          "lng" : -122.0792542197085
                       },
                       "southwest" : {
                          "lat" : 37.4254371197085,
                          "lng" : -122.0819521802915
                       }
                    }
                 },
                 "place_id" : "ChIJtYuu0V25j4ARwu5e4wwRYgE",
                 "plus_code" : {
                    "compound_code" : "CWC8+R3 Mountain View, California, United States",
                    "global_code" : "849VCWC8+R3"
                 },
                 "types" : [ "street_address" ]
              }
           ],
           "status" : "OK"
        }
    """
    api_key = settings.GOOGLE_API_KEY
    url = f'{GOOGLE_GEOCODING_API}?address={address}&key={api_key}'
    try:
        response = requests.get(
            url,
            timeout=60,
        )
        return response.json()
    except (requests.ConnectionError, ValueError):
        if silent:
            return {}
        raise

import json

import requests

class Location:
    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    def get_latitude(self):
        return self.__latitude

    def get_longitude(self):
        return self.__longitude

    def __str__(self):
        return f"{self.__latitude},{self.__longitude}"


class GoogleMapsRepository:
    _baseUrl = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    _key = "AIzaSyAxfoBZfNuymxhvaXt90SCuZ_Ta_r2kXx0";

    def getRestaurants(self, location: Location, radius: int):
        header = {
            "Accept": "application/json"
        }
        url = f"{self._baseUrl}?location={location}&type=restaurant&radius={radius}&key={self._key}"
        result = requests.get(url, header)
        if (result.ok):
            with open("result.json", "a") as writer:
                writer.write(json.dumps(result.json()))


def main():
    repository = GoogleMapsRepository()
    repository.getRestaurants(Location(56.007876, 37.865488), 1500)


if __name__ == '__main__':
    main()
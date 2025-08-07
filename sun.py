"""
SUN
"""

from astral.geocoder import all_locations, database
from astral.location import LocationInfo
from astral.sun import sun
from astral import Observer
from pprint import pprint
from datetime import date
from astral.sun import elevation, azimuth

import pytz

class PlanetSun:

    def __init__(self, name, region, tz, lat, lon):
        self.city = LocationInfo(name, region, tz, lat, lon)
            

    def sun_rise_and_set(self):
        observer = Observer(latitude=self.city.latitude,longitude=self.city.longitude,elevation=0)
        day_info = sun(observer,date.today(),tzinfo=self.city.tzinfo)
        pprint(day_info)
        


a = PlanetSun('New York', 'United States', 'America/New_York', 40.7128, -74.0060)
a.sun_rise_and_set()


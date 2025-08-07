"""
hora calculation
"""
from datetime import datetime,timedelta
import math
import pdb
import constants

class Hora:
    def __init__(self):
        pass

    def list_hora(self, sunrise_current_day, sunrise_next_day):
        hora_start = sunrise_current_day 
        total_duration = ( sunrise_next_day - sunrise_current_day ) / 24
        total_duration_sec =  total_duration.total_seconds()
        day_of_the_week = int(sunrise_current_day.strftime("%w"))

        #pdb.set_trace()

        while hora_start  < sunrise_next_day :
            from_timestamp = hora_start.replace(microsecond= 0)
            to_timestamp = (hora_start + timedelta(seconds = total_duration_sec)).replace(microsecond=0)
            print(f'Hora of {constants.PLANET_HORA[day_of_the_week]}:  From {from_timestamp} to {to_timestamp}')
            hora_start = hora_start + timedelta(seconds = total_duration_sec)
            day_of_the_week+=5
            if day_of_the_week > 6:
                day_of_the_week = day_of_the_week - 7

    def get_hora_of_planet(self, sunrise_current_day, sunrise_next_day, hora_time):
        counter = 1 
        hora_start = sunrise_current_day 
        total_duration = ( sunrise_next_day - sunrise_current_day ) / 24
        total_duration_sec =  total_duration.total_seconds()
        day_of_the_week = int(sunrise_current_day.strftime("%w"))

        while hora_start  < sunrise_next_day :
            from_timestamp = hora_start.replace(microsecond= 0)
            to_timestamp = (hora_start + timedelta(seconds = total_duration_sec)).replace(microsecond=0)

            if from_timestamp <= hora_time <= to_timestamp:
                return constants.PLANET_HORA[day_of_the_week]
            hora_start = hora_start + timedelta(seconds = total_duration_sec)
            day_of_the_week+=5
            if day_of_the_week > 6:
                day_of_the_week = day_of_the_week - 7

sunrise_current_day = datetime(2025,8,10,6,14,55)
sunrise_next_day = datetime(2025,8,11,6,15,11)
find_hora_in = datetime(2025,8,10,22,30,11)

hora_listing = Hora()

hora_listing.list_hora(sunrise_current_day, sunrise_next_day)
planet = hora_listing.get_hora_of_planet(sunrise_current_day, sunrise_next_day,find_hora_in)
if planet != "":
    print(f'\n\n\n\n {find_hora_in }Belongs to the {planet}')
else:
    print(f'unable to find! please check time')
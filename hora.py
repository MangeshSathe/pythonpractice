"""
hora calculation
"""


from datetime import datetime,timedelta
day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
planet_hora = ['Sun','Moon','Mars','Mercury','Jupiter','Venus','Saturn']
counter = 1 
day_night = 'Day'

sunrise_current_day = datetime(2025,8,10,6,15,55)
sunrise_next_day = datetime(2025,8,11,6,15,11)
hora_start = sunrise_current_day 
total_duration = ( sunrise_next_day - sunrise_current_day ) / 24
total_duration_sec =  total_duration.total_seconds()

day_of_the_week = int(sunrise_current_day.strftime("%w"))

while hora_start < sunrise_next_day:
    if counter > 12:
        day_night = 'Night'
    print(f'{day_night} hora of {planet_hora[day_of_the_week]}:  From {hora_start} to {hora_start + timedelta(seconds = total_duration_sec)}')
    hora_start = hora_start + timedelta(seconds = total_duration_sec)
    counter+=1
    day_of_the_week+=5
    if day_of_the_week > 6:
        day_of_the_week = day_of_the_week - 7
import datetime
from weather import weather, unit

def getCurrentTime(time):
    time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return time


def getWeathertemp(temp):
    weather = Weather(unit=Unit.Celcius)
    
    location = weather.lookup_by_location('Melbourne')
    temp = lookup.temp
    
    return(temp.text)

def getWeatherHumid(humidity):

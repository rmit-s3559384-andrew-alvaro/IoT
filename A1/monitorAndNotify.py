import datetime
from sense_hat import SenseHat

def getCurrentTime(time):
    time = datetime.datetime.fromtimestamp(
    int(time)
    ).strftime('%I:%M %p')

    return time
    print(time)


# OR
# sense = VirtualSenseHat.getSenseHat(False)
def getWeatherTemp(): 
   sense = VirtualSenseHat.getSenseHat()
   temperature = sense.get_temperature()
   sense.show_message('Temperature: {0:0.1f} *C'.format(temperature))
   return temperature
def getWeatherHumid():
    sense = VirtualSenseHat.getSenseHat()
    humidity = sense.get_humidity()
    sense.show_message('Humidity: {0:0.0f}%'.format(humidity))
    return humidity
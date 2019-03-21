import datetime
from virtual_sense_hat import VirtualSenseHat
 
def getCurrentTime():
    getTime = datetime.datetime.now().strftime('%I:%M %p')
    sense.show_message('Time: {0:0.1f}'.format(getTime))
    return getTime
    print(getTime)

getCurrentTime()
# OR
# sense = VirtualSenseHat.getSenseHat(False)
def getWeatherTemp(): 
   sense = VirtualSenseHat.getSenseHat()
   temperature = sense.get_temperature()
   sense.show_message('Temperature: {0:0.1f} *C'.format(temperature))
   return temperature

getWeatherTemp()
def getWeatherHumid():
    sense = VirtualSenseHat.getSenseHat()
    humidity = sense.get_humidity()
    sense.show_message('Humidity: {0:0.0f}%'.format(humidity))
    return humidity

getWeatherHumid()
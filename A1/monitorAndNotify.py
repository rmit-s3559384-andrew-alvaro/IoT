import datetime
from virtual_sense_hat import VirtualSenseHat
 
def getCurrentTime():
    sense = VirtualSenseHat.getSenseHat()
    timestamp = datetime.datetime.now().strftime('%I:%M %p')
    sense.show_message('Time: %s' % timestamp)
    print("Time:", timestamp)
getCurrentTime()

def getWeatherTemp(): 
   sense = VirtualSenseHat.getSenseHat()
   temperature = sense.get_temperature()
   sense.show_message('Temperature: {0:0.1f} *C'.format(temperature))
   print("Temperature:", temperature)
getWeatherTemp()

def getWeatherHumid():
    sense = VirtualSenseHat.getSenseHat()
    humidity = sense.get_humidity()
    sense.show_message('Humidity: {0:0.0f}%'.format(humidity))
    print("Humidity:", humidity)
getWeatherHumid()
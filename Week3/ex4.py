from virtual_sense_hat import VirtualSenseHat

sense = VirtualSenseHat.getSenseHat()
# OR
# sense = VirtualSenseHat.getSenseHat(False)

temperature = sense.get_temperature()
sense.show_message('Temperature: {0:0.1f} *C'.format(temperature))

humidity = sense.get_humidity()
sense.show_message('Humidity: {0:0.0f}%'.format(humidity))

sense.clear()

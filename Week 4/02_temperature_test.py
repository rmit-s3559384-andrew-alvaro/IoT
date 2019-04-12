from virtual_sense_hat import VirtualSenseHat

sense = VirtualSenseHat.getSenseHat()

temperature = sense.get_temperature()
sense.show_message("Temp: {0:0.1f} *c".format(temperature), scroll_speed = 0.05)

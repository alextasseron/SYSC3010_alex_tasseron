import sense_hat
from time import sleep

sense = sense_hat.SenseHat()

blue = (0,0,255)

white = (0,0,0)

sense.show_message("NORESSAT REDNAXELA", 0.1, blue)

sense.clear()
import sense_hat
from time import sleep

sense = sense_hat.SenseHat()

red = (255,0,0)

white = (0,0,0)

sense.show_message("ALEXANDER TASSERON", 0.1, red)

sense.clear()
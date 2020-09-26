import sense_hat
from time import sleep

sense = sense_hat.SenseHat()

toggle = sense_hat.ACTION_PRESSED

R = (255,0,0)
B = (0,0,255)
X = (0,0,0)

a_initial = [
    X, X, X, R, R, X, X, X,
    X, X, R, X, X, R, X, X,
    X, R, X, X, X, X, R, X,
    X, R, X, X, X, X, R, X,
    X, R, R, R, R, R, R, X,
    X, R, X, X, X, X, R, X,
    X, R, X, X, X, X, R, X,
    R, R, R, X, X, R, R, R,
]

t_initial = [
    X, B, B, B, B, B, B, X,
    X, B, B, B, B, B, B, X,
    X, X, X, B, B, X, X, X,
    X, X, X, B, B, X, X, X,
    X, X, X, B, B, X, X, X,
    X, X, X, B, B, X, X, X,
    X, X, X, B, B, X, X, X,
    X, X, X, B, B, X, X, X,
]

cur = 0

while True:
    
    for event in sense.stick.get_events():
        
        if event.action == toggle:
            if cur == 0:
                sense.set_pixels(a_initial)
                cur = 1
            elif cur == 1:
                sense.set_pixels(t_initial)
                cur = 2
            else:
                sense.set_pixels(a_initial)
                cur = 1

  
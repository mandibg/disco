
from sense_hat import *
from time import sleep
sense = SenseHat()

b = (196, 196, 188)
r = (250, 40, 40)
w = (250, 250, 250)
p = (250, 135, 246)
y = (255, 252, 69)


rock = [
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
]

rock2 = [
b, b, r, b, b, r, b, b,
b, b, r, b, b, r, b, b,
b, b, r, b, b, r, b, b,
b, b, r, r, r, r, b, b,
b, b, r, r, r, r, b, b,
b, b, r, r, r, r, b, b,
b, b, r, r, r, r, b, b,
b, b, b, b, b, b, b, b,
]

classical = [
p, p, p, p, p, p, p, p,
w, w, w, w, w, w, w, w,
p, p, p, p, p, p, p, p,
w, w, w, w, w, w, w, w,
p, p, p, p, p, p, p, p,
w, w, w, w, w, w, w, w,
p, p, p, p, p, p, p, p,
w, w, w, w, w, w, w, w,
]

classical2 = [
w, w, w, w, w, w, w, w,
p, p, p, p, p, p, p, p,
w, w, w, w, w, w, w, w,
p, p, p, p, p, p, p, p,
w, w, w, w, w, w, w, w,
p, p, p, p, p, p, p, p,
w, w, w, w, w, w, w, w,
p, p, p, p, p, p, p, p,
]

dance = [
y, y, y, y, y, y, y, y,
y, y, y, y, y, y, y, y,
y, r, y, y, y, y, r, y,
y, y, y, y, y, y, y, y,
y, r, y, y, y, y, r, y,
y, r, y, y, y, y, r, y,
y, r, r, r, r, r, r, y,
y, y, y, y, y, y, y, y,
]

dance2 = [
y, y, y, y, y, y, y, y,
y, y, y, y, y, y, y, y,
y, r, y, y, y, y, r, y,
y, y, y, y, y, y, y, y,
y, y, r, r, r, r, y, y,
y, y, r, y, y, r, y, y,
y, y, r, r, r, r, y, y,
y, y, y, y, y, y, y, y,
]

sense.clear()

while True:
    e = sense.stick.wait_for_event()
    if e.direction == DIRECTION_UP:
        sense.set_pixels(dance)
        sleep(0.1)
        sense.set_pixels(dance2)
        sleep(0.1)
    if e.direction == DIRECTION_DOWN:
        sense.set_pixels(rock)
        sleep(0.5)
        sense.set_pixels(rock2)
        sleep(0.5)
    if e.direction == DIRECTION_LEFT:
        sense.set_pixels(classical)
        sleep(2)
        sense.set_pixels(classical2)
        sleep(2)
 


    

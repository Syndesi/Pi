# This script need pigpio for operating.

import pigpio
import time

pi = pigpio.pi()

var red = 0
var green = 0
var blue = 0

def color(red2, green2, blue2):
  red = red2
  green = green2
  blue = blue2

def update():
  pi.set_PWM_dutycycle(27, red)
  pi.set_PWM_dutycycle(22, green)
  pi.set_PWM_dutycycle(17, blue)

color(0, 0, 0)
time.sleep(0.1)

var = 1
while var == 1 :
  color(255, 255, 255)
  time.sleep(0.1)
  color(0, 0, 0)
  time.sleep(0.1)

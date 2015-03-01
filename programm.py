# This script need pigpio for operating.

import pigpio
import time

pi = pigpio.pi()

red = 0
green = 0
blue = 0

def color(red2, green2, blue2):
  red = red2
  green = green2
  blue = blue2

def update():
  pi.set_PWM_dutycycle(27, red)
  pi.set_PWM_dutycycle(22, green)
  pi.set_PWM_dutycycle(17, blue)
  print(red, ", ", green, ", ", blue)

color(0, 0, 0)
pi.set_PWM_dutycycle(22, 255)
pi.set_PWM_dutycycle(22, 0)
time.sleep(0.1)

var = 1
while var == 1 :
  color(255, 255, 255)
  update()
  time.sleep(0.1)
  color(0, 0, 0)
  update()
  time.sleep(0.1)

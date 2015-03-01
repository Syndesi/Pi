# This script need pigpio for operating.

import pigpio
import time

pi = pigpio.pi()

red = 0
green = 0
blue = 0

def color(var1, var2, var3):
  red = var1
  green = var2
  blue = var3
  print red

def update():
  pi.set_PWM_dutycycle(27, red)
  pi.set_PWM_dutycycle(22, green)
  pi.set_PWM_dutycycle(17, blue)
  print red

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

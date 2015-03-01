# This script need pigpio for operating.

import pigpio
import time

pi = pigpio.pi()

n = 255
blue = 0
for i in range(1,n+1):
  blue = blue + 1
  pi.set_PWM_dutycycle(17, blue)
  time.sleep(0.01)

blue = 255
for i in range(1,n+1):
  blue = blue - 1
  pi.set_PWM_dutycycle(17, blue)
  time.sleep(0.01)

color(255, 255, 255)
time.sleep(0.1)
color(0, 0, 0)

def color(red, green, blue):
  pi.set_PWM_dutycycle(27, red)
  pi.set_PWM_dutycycle(22, green)
  pi.set_PWM_dutycycle(17, blue)
  return true

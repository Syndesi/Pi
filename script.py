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

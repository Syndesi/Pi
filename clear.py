# This script need pigpio for operating.

import pigpio
import time
import math

pi = pigpio.pi()

def color(red, green, blue):
  pi.set_PWM_dutycycle(27, red)
  pi.set_PWM_dutycycle(22, green)
  pi.set_PWM_dutycycle(17, blue)

color(0, 0, 0)

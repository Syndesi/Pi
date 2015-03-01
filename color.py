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
sleep(0.1)
color(0, 0, 2)
sleep(0.1)
color(0, 0, 4)
sleep(0.1)
color(0, 0, 8)
sleep(0.1)
color(0, 0, 16)
sleep(0.1)
color(0, 0, 32)
sleep(0.1)
color(0, 0, 64)
sleep(0.1)
color(0, 0, 128)
sleep(0.1)
color(0, 0, 255)
sleep(0.1)
color(0, 0, 0)
sleep(0.1)
color(255, 255, 255)
sleep(0.1)
color(0, 0, 0)
sleep(0.1)

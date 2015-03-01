# This script need pigpio for operating.

import pigpio
import time

pi = pigpio.pi()

def color(red, green, blue):
  pi.set_PWM_dutycycle(27, red)
  pi.set_PWM_dutycycle(22, green)
  pi.set_PWM_dutycycle(17, blue)


color(0, 0, 0)
time.sleep(0.1)
color(0, 0, 2)
time.sleep(0.1)
color(0, 0, 4)
time.sleep(0.1)
color(0, 0, 8)
time.sleep(0.1)
color(0, 0, 16)
time.sleep(0.1)
color(0, 0, 32)
time.sleep(0.1)
color(0, 0, 64)
time.sleep(0.1)
color(0, 0, 128)
time.sleep(0.1)
color(0, 0, 255)
time.sleep(0.1)
color(0, 0, 0)
time.sleep(0.1)
color(255, 255, 255)
time.sleep(0.1)
color(0, 0, 0)
time.sleep(0.1)

# This script need pigpio for operating.

import pigpio
import time

pi = pigpio.pi()

pi.set_PWM_dutycycle(17, 255)

time.sleep(0.2)

pi.set_PWM_dutycycle(17, 128)

time.sleep(0.2)

pi.set_PWM_dutycycle(17, 64)

time.sleep(0.2)

pi.set_PWM_dutycycle(17, 32)

time.sleep(0.2)

pi.set_PWM_dutycycle(17, 16)

# This script need pigpio for operating.

import pigpio

pi = pigpio.pi()

pi.set_PWM_dutycycle(17, 255)

sleep(1000)

pi.set_PWM_dutycycle(17, 128)

sleep(1000)

pi.set_PWM_dutycycle(17, 64)

sleep(1000)

pi.set_PWM_dutycycle(17, 32)

sleep(1000)

pi.set_PWM_dutycycle(17, 16)

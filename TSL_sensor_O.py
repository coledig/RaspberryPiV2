import board
import busio
import adafruit_tsl2561
import time
import datetime

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the TSL2561 instance, passing in the I2C bus
tsl = adafruit_tsl2561.TSL2561(i2c)

# Enable the light sensor
tsl.enable = True

# Set gain 0=1x, 1=16x
tsl.gain = 0

# Set integration time (0=13.7ms, 1=101ms, 2=402ms, or 3=manual)
tsl.integration_time = 1

broadband = tsl.broadband
infrared = tsl.infrared

# Get computed lux value (tsl.lus can return None or a float)
lux = tsl.lux

# Print chip info / results
##print("Gain = {}".format(tsl.gain))
##print("Integration time = {}".format(tsl.integration_time ))

##print("Broadband = {}".format(broadband))
##print("Infrared = {}".format(infrared))
##print("Lux = {}".format(lux))




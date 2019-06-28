import time
import board
import busio
import adafruit_si7021
import datetime

# Create library object using our Bus I2C part
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

#while True:
##print("Temperature: %0.1f C" % sensor.temperature)
##print("Humidity: %0.1f %%" % sensor.relative_humidity)
##time.sleep(2)


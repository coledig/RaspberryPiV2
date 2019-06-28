# Does not work, wiring error pops up.
# Might have to download circuitpython library??

import board
import busio
import adafruit_mpl3115a2
import time
import datetime

i2c = busio.I2C(board.SCL, board.SDA)

sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)

while True:
    pressure = sensor.pressure
    print("Pressure: {0:0.2f} pascals".format(pressure))
    altitude = sensor.altitude
    print("Altitude: {0:0.2f} meters".format(altitude))
    temperature = sensor.temperature
    print("Temperature: {0:0.2f} C".format(temperature))
    time.sleep(1.0)


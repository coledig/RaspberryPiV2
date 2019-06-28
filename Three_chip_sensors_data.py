# This is for data to be stored into a csv with a timestamp that will run
# inside of the PIR sensor.

import time
import datetime

for x in range(3):

    from TSL_sensor_O import *
    from New_MPL import *
    from Si7021_sensor_O import *

    date = datetime.datetime.now().strftime("%m_%_d_%Y_%H_%M_%S")
    f = open("3chip_data.csv","a")
        
    f.write("\n" + date + ",")
        
    #MPL
    f.write("%.2f C," %cTemp)
    f.write("%.2f F," %fTemp)
    #f.write("%.2f m," %altitude)
    f.write("%.2f kPa," %pressure)

    #Si7021
    f.write("%0.1f C," % sensor.temperature)
    f.write("%0.1f %%," % sensor.relative_humidity)
            
    #TSL
    f.write("{},".format(broadband))
    f.write("{},".format(infrared))
    f.write("{}".format(lux))

    time.sleep(1)

    f.close()

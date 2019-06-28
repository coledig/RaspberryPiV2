# This is for data to be stored into a csv with a timestamp that will run
# through cronjob.

import time
import datetime

for x in range(3):

    date = datetime.datetime.now().strftime("%m_%_d_%Y_%H_%M_%S")
    
    from TSL_sensor_O import *
    from New_MPL import *
    from Si7021_sensor_O import *

    #f = open("New_All_chip_data.csv","a")
    
    output=""
    
    output+=(" " + date + ",")
        
    #MPL
    output+=("%.2f C," %cTemp)
    output+=("%.2f F," %fTemp)
    output+=("%.2f kPa," %pressure)

    #Si7021
    output+=("%0.1f C," % sensor.temperature)
    output+=("%0.1f %%," % sensor.relative_humidity)
            
     #TSL
    output+=("{},".format(broadband))
    output+=("{},".format(infrared))
    output+=("{}".format(lux))

    #f.close()

    time.sleep(1)

    print(output)


from sense_hat import SenseHat
import time
from pymongo import MongoClient
from datetime import datetime
sense = SenseHat()
sense.clear()
client = MongoClient()
db = client['iot_project']
while True:
    pressure = sense.get_pressure()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    orientation = sense.get_orientation()
    sense.show_message("Pressure: %.2f" % pressure)
    sense.show_message("Temp: %.2f" % temp)
    sense.show_message("Humidity: %.2f" % humidity)
    sense.show_message("Orientation: %s" % orientation)
    db.sensor_data.insert_one(
        {"createdAt": datetime.now(), "pressure": pressure, "temp": temp, "humidity": humidity, "orientation": orientation})
    sense.clear()

    time.sleep(5)
    print(temp)
    print(pressure)

import natureremo
import os
import csv

acccess_token = "hogehoge"
natureremo = natureremo.NatureRemo(acccess_token)

time = natureremo.get_time()
temperture = natureremo.get_temperture()
humidity = natureremo.get_humidity()
hue = natureremo.get_hue()

if os.path.exists("data.csv"):
    with open("data.csv", mode='a') as data:
        w_data = csv.writer(data)
        w_data.writerow([time, temperture, humidity, hue])
else:
    with open("data.csv", mode='w') as data:
        w_data = csv.writer(data)
        w_data.writerow(["time", "temperture", "humidity", "hue"])
        w_data.writerow([time, temperture, humidity, hue])

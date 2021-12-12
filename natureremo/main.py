import natureremo
import os
import csv

acccess_token = "hogehoge"
natureremo = natureremo.NatureRemo(acccess_token)

time = natureremo.get_time()
temperture = natureremo.get_temperture()
humidity = natureremo.get_humidity()
hue = natureremo.get_hue()

cwd_path = os.getcwd()

if os.path.exists(cwd_path + "/data.csv"):
    with open(cwd_path + "/data.csv", mode='a') as data:
        w_data = csv.writer(data)
        w_data.writerow([time, temperture, humidity, hue])
else:
    with open(cwd_path + "/data.csv", mode='w') as data:
        w_data = csv.writer(data)
        w_data.writerow(["time", "temperture", "humidity", "hue"])
        w_data.writerow([time, temperture, humidity, hue])

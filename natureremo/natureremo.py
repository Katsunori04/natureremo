from remo import NatureRemoAPI
from pytz import timezone


class NatureRemo:

    # アクセストークンを引数として渡す
    def __init__(self, access_token):
        self.api = NatureRemoAPI(access_token)

    def get_devices(self):
        return self.api.get_devices()

    def get_temperture(self):
        tempeture = [
            dev.newest_events['te'].val for dev in self.get_devices()]
        return tempeture[1]

    def get_humidity(self):
        humidity = self.get_devices()[1].newest_events['hu'].val
        return humidity

    def get_hue(self):
        hue = self.get_devices()[1].newest_events['il'].val
        return hue

    def get_time(self):
        time = self.get_devices()[1].newest_events['hu'].created_at

        # JSTに変換し返す
        return time.astimezone(timezone('Asia/Tokyo'))

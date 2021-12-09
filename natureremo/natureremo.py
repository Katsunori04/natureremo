from remo import NatureRemoAPI


class NatureRemo:
    def __init__(self, access_token):
        self.api = NatureRemoAPI(access_token)

    def get_devices(self):
        return self.api.get_devices()

    def get_temperture(self):
        tempetures = [
            dev.newest_events['te'].val for dev in self.get_devices()]
        return tempetures

    def get_humidity(self):
        return 0

    def get_hue(self):
        return 0

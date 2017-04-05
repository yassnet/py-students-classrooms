from src.lat_long_to_utm import LLtoUTM


class Position:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

        self.zone, self.easting, self.northing = LLtoUTM(23, latitude, longitude)

        self.x = self.easting
        self.y = self.northing

from lib.geographic_utm_converter import geographic_to_utm


class Position:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

        self.zone, self.easting, self.northing = geographic_to_utm(23, latitude, longitude)

        self.x = self.easting
        self.y = self.northing

from lib.geographic_utm_converter import geographic_to_utm

# @author Yassir Aguila
# @version $Revision: 1.0 $ $Date: 2017-04-05
#
# Position model class


class Position:
    
    REFERENCE_ELLIPSOID = 23

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

        # Tuple resulting of conversion
        self.zone, self.easting, self.north = geographic_to_utm(self.REFERENCE_ELLIPSOID, latitude, longitude)

        # X coordinate projected
        self.x = self.easting

        # Y coordinate projected
        self.y = self.north

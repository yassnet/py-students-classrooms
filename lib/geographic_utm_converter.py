from math import pi, sin, cos, tan, sqrt

# Authors: Han Ul Yoon <hyoon24@uiuc.edu>, Chuck Gantz <chuck.gantz@globalstar.com>, Russ Nelson <nelson@crynwr.com>

# http://robotics.ai.uiuc.edu/~hyoon24/LatLongUTMconversion.py
# Geographic - UTM and UTM - Geographic conversions
# Reference ellipsoids derived from Peter H. Dana's website-
# http://www.utexas.edu/depts/grg/gcraft/notes/datum/elist.html
# Department of Geography, University of Texas at Austin
# Internet: pdana@mail.utexas.edu (3/22/95)

# Source
# Defense Mapping Agency. 1987b. DMA Technical Report: Supplement to Department of Defense World Geodetic System
# 1984 Technical Report. Part I and II. Washington, DC: Defense Mapping Agency


# definitions for lat/long to UTM and UTM to lat/lng conversions
DEG_TO_RADIANS = pi / 180.0
RADIANS_TO_DEGREES = 180.0 / pi

EQUATORIAL_RADIUS = 2
ECCENTRICITY_SQUARED = 3

ELLIPSOID = [
    #  id, Ellipsoid name, Equatorial Radius, square of eccentricity
    # first once is a placeholder only, To allow array indices to match id numbers
    [-1, "Placeholder", 0, 0],
    [1, "Airy", 6377563, 0.00667054],
    [2, "Australian National", 6378160, 0.006694542],
    [3, "Bessel 1841", 6377397, 0.006674372],
    [4, "Bessel 1841 (Nambia] ", 6377484, 0.006674372],
    [5, "Clarke 1866", 6378206, 0.006768658],
    [6, "Clarke 1880", 6378249, 0.006803511],
    [7, "Everest", 6377276, 0.006637847],
    [8, "Fischer 1960 (Mercury] ", 6378166, 0.006693422],
    [9, "Fischer 1968", 6378150, 0.006693422],
    [10, "GRS 1967", 6378160, 0.006694605],
    [11, "GRS 1980", 6378137, 0.00669438],
    [12, "Helmert 1906", 6378200, 0.006693422],
    [13, "Hough", 6378270, 0.00672267],
    [14, "International", 6378388, 0.00672267],
    [15, "Krassovsky", 6378245, 0.006693422],
    [16, "Modified Airy", 6377340, 0.00667054],
    [17, "Modified Everest", 6377304, 0.006637847],
    [18, "Modified Fischer 1960", 6378155, 0.006693422],
    [19, "South American 1969", 6378160, 0.006694542],
    [20, "WGS 60", 6378165, 0.006693422],
    [21, "WGS 66", 6378145, 0.006694542],
    [22, "WGS-72", 6378135, 0.006694318],
    [23, "WGS-84", 6378137, 0.00669438]
]


def geographic_to_utm(reference_ellipsoid, latitude, longitude):
    # def geographic_to_utm(int reference_ellipsoid, const double latitude, const double longitude)
    # returns: (tuple) char utm_zone, double utm_easting, double utm_north

    # This function converts latitude and longitude to UTM coordinates.  Equations from USGS Bulletin 1532
    # East Longitudes are positive, West longitudes are negative.
    # North latitudes are positive, South latitudes are negative
    # Latitude and longitude are in decimal degrees

    a = ELLIPSOID[reference_ellipsoid][EQUATORIAL_RADIUS]
    ecc_squared = ELLIPSOID[reference_ellipsoid][ECCENTRICITY_SQUARED]
    k0 = 0.9996

    # Make sure the longitude is between -180.00 .. 179.9
    long_temp = (longitude + 180) - int((longitude + 180) / 360) * 360 - 180  # -180.00 .. 179.9

    lat_rad = latitude * DEG_TO_RADIANS
    long_rad = long_temp * DEG_TO_RADIANS

    zone_number = get_zone_number(latitude, long_temp)

    long_origin = (zone_number - 1) * 6 - 180 + 3  # +3 puts origin in middle of zone
    long_origin_rad = long_origin * DEG_TO_RADIANS

    # compute the UTM Zone from the latitude and longitude
    utm_zone = "%d%c" % (zone_number, _utm_letter_designator(latitude))

    ecc_prime_squared = ecc_squared / (1 - ecc_squared)
    N = a / sqrt(1 - ecc_squared * sin(lat_rad) * sin(lat_rad))
    T = tan(lat_rad) * tan(lat_rad)
    C = ecc_prime_squared * cos(lat_rad) * cos(lat_rad)
    A = cos(lat_rad) * (long_rad - long_origin_rad)

    M = a * ((1
              - ecc_squared / 4
              - 3 * ecc_squared * ecc_squared / 64
              - 5 * ecc_squared * ecc_squared * ecc_squared / 256) * lat_rad
             - (3 * ecc_squared / 8
                + 3 * ecc_squared * ecc_squared / 32
                + 45 * ecc_squared * ecc_squared * ecc_squared / 1024) * sin(2 * lat_rad)
             + (15 * ecc_squared * ecc_squared / 256 + 45 * ecc_squared * ecc_squared * ecc_squared / 1024) * sin(
        4 * lat_rad)
             - (35 * ecc_squared * ecc_squared * ecc_squared / 3072) * sin(6 * lat_rad))

    utm_easting = (k0 * N * (A + (1 - T + C) * A * A * A / 6
                             + (5 - 18 * T + T * T + 72 * C - 58 * ecc_prime_squared) * A * A * A * A * A / 120)
                   + 500000.0)

    utm_north = (k0 * (M + N * tan(lat_rad) * (A * A / 2 + (5 - T + 9 * C + 4 * C * C) * A * A * A * A / 24
                                               + (61
                                                  - 58 * T
                                                  + T * T
                                                  + 600 * C
                                                  - 330 * ecc_prime_squared) * A * A * A * A * A * A / 720)))

    if latitude < 0:
        utm_north = utm_north + 10000000.0  # 10000000 meter offset for southern hemisphere
    return utm_zone, utm_easting, utm_north


def utm_to_geographic(reference_ellipsoid, north, easting, zone):
    # void utm_to_geographic(int reference_ellipsoid, const double north, const double easting, const char* zone)
    # returns: (tuple) double latitude, double longitude

    # Converts UTM coordinates to lat/long.  Equations from USGS Bulletin 1532
    # East Longitudes are positive, West longitudes are negative.
    # North latitudes are positive, South latitudes are negative
    # latitude and Long are in decimal degrees.

    k0 = 0.9996
    a = ELLIPSOID[reference_ellipsoid][EQUATORIAL_RADIUS]
    ecc_squared = ELLIPSOID[reference_ellipsoid][ECCENTRICITY_SQUARED]
    e1 = (1 - sqrt(1 - ecc_squared)) / (1 + sqrt(1 - ecc_squared))

    x = easting - 500000.0  # remove 500,000 meter offset for longitude
    y = north

    zone_letter = zone[-1]
    zone_number = int(zone[:-1])
    if not zone_letter >= 'N':
        y -= 10000000.0  # remove 10,000,000 meter offset used for southern hemisphere

    long_origin = (zone_number - 1) * 6 - 180 + 3  # +3 puts origin in middle of zone

    ecc_prime_squared = ecc_squared / (1 - ecc_squared)

    m = y / k0
    mu = m / (
        a * (
            1 - ecc_squared / 4 - 3 * ecc_squared * ecc_squared / 64 - 5 *
            ecc_squared * ecc_squared * ecc_squared / 256))

    phi1_rad = (mu + (3 * e1 / 2 - 27 * e1 * e1 * e1 / 32) * sin(2 * mu)
                + (21 * e1 * e1 / 16 - 55 * e1 * e1 * e1 * e1 / 32) * sin(4 * mu)
                + (151 * e1 * e1 * e1 / 96) * sin(6 * mu))

    n1 = a / sqrt(1 - ecc_squared * sin(phi1_rad) * sin(phi1_rad))
    t1 = tan(phi1_rad) * tan(phi1_rad)
    c1 = ecc_prime_squared * cos(phi1_rad) * cos(phi1_rad)
    r1 = a * (1 - ecc_squared) / pow(1 - ecc_squared * sin(phi1_rad) * sin(phi1_rad), 1.5)
    d = x / (n1 * k0)

    latitude = phi1_rad - (n1 * tan(phi1_rad) / r1) * (
        d * d / 2 - (5 + 3 * t1 + 10 * c1 - 4 * c1 * c1 - 9 * ecc_prime_squared) *
        d * d * d * d / 24
        +
        (61 + 90 * t1 + 298 * c1 + 45 * t1 * t1 - 252 * ecc_prime_squared - 3 * c1 * c1) *
        d * d * d * d * d * d / 720)
    latitude = latitude * RADIANS_TO_DEGREES

    longitude = (d - (1 + 2 * t1 + c1) * d * d * d / 6 + (
        5 - 2 * c1 + 28 * t1 - 3 * c1 * c1 + 8 * ecc_prime_squared + 24 * t1 * t1)
                 * d * d * d * d * d / 120) / cos(phi1_rad)
    longitude = long_origin + longitude * RADIANS_TO_DEGREES
    return latitude, longitude


def get_zone_number(latitude, long_temp):
    # Returns: int
    # Determine zone number given latitude and longitude

    zone_number = int((long_temp + 180) / 6) + 1

    if (56.0 <= latitude < 64) and (3.0 <= long_temp < 12):
        zone_number = 32

    # Special zones for Svalbard
    if 72.0 <= latitude < 84:
        if 0.0 <= long_temp < 9:
            zone_number = 31
        elif 9.0 <= long_temp < 21:
            zone_number = 33
        elif 21.0 <= long_temp < 33:
            zone_number = 35
        elif 33.0 <= long_temp < 42:
            zone_number = 37
    return zone_number


def _utm_letter_designator(latitude):
    # This function determines the correct UTM letter designator for the given latitude
    # returns 'Z' if latitude is outside the UTM limits of 84N to 80S

    if 84 >= latitude >= 72:
        return 'X'
    elif 72 > latitude >= 64:
        return 'W'
    elif 64 > latitude >= 56:
        return 'V'
    elif 56 > latitude >= 48:
        return 'U'
    elif 48 > latitude >= 40:
        return 'T'
    elif 40 > latitude >= 32:
        return 'S'
    elif 32 > latitude >= 24:
        return 'R'
    elif 24 > latitude >= 16:
        return 'Q'
    elif 16 > latitude >= 8:
        return 'P'
    elif 8 > latitude >= 0:
        return 'N'
    elif 0 > latitude >= -8:
        return 'M'
    elif -8 > latitude >= -16:
        return 'L'
    elif -16 > latitude >= -24:
        return 'K'
    elif -24 > latitude >= -32:
        return 'J'
    elif -32 > latitude >= -40:
        return 'H'
    elif -40 > latitude >= -48:
        return 'G'
    elif -48 > latitude >= -56:
        return 'F'
    elif -56 > latitude >= -64:
        return 'E'
    elif -64 > latitude >= -72:
        return 'D'
    elif -72 > latitude >= -80:
        return 'C'
    else:
        return 'Z'  # if the Latitude is outside the UTM limits


if __name__ == '__main__':
    (z, e, n) = geographic_to_utm(23, 40 + (6 + 18.3591 / 60) / 60, -(88 + (13 + 9.52349 / 60) / 60))
    print(z, e, n)
    print(utm_to_geographic(23, e, n, z))

from geopy.distance import geodesic

HOME_LOCATION = (28.6139,77.2090)

SAFE_RADIUS = 500

def check_geofence(lat,lon):

    current = (lat,lon)

    distance = geodesic(
        HOME_LOCATION,
        current
    ).meters

    if distance > SAFE_RADIUS:
        return True

    return False
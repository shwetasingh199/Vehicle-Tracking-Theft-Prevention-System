from geopy.distance import geodesic


def calculate_route_distance(df):

    total_distance = 0

    for i in range(len(df)-1):

        p1 = (
            df.iloc[i]["Latitude"],
            df.iloc[i]["Longitude"]
        )

        p2 = (
            df.iloc[i+1]["Latitude"],
            df.iloc[i+1]["Longitude"]
        )

        total_distance += geodesic(
            p1,
            p2
        ).km

    return round(total_distance, 2)
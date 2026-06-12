import folium
from geopy.distance import geodesic


def create_route_map(vehicle_df):

    vehicle_df = vehicle_df.reset_index(drop=True)

    route_points = list(
        zip(
            vehicle_df["Latitude"],
            vehicle_df["Longitude"]
        )
    )

    center = route_points[0]

    m = folium.Map(
        location=center,
        zoom_start=14
    )

    # Route line

    folium.PolyLine(
        route_points,
        weight=5,
        color="blue"
    ).add_to(m)

    # Start marker

    folium.Marker(
        route_points[0],
        popup="START",
        icon=folium.Icon(
            color="green",
            icon="play"
        )
    ).add_to(m)

    # End marker

    folium.Marker(
        route_points[-1],
        popup="END",
        icon=folium.Icon(
            color="red",
            icon="stop"
        )
    ).add_to(m)

    # Checkpoints

    for idx, point in enumerate(route_points):

        folium.CircleMarker(
            location=point,
            radius=5,
            popup=f"Point {idx+1}",
            color="blue",
            fill=True
        ).add_to(m)

    return m
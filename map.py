import folium
import json

# Load branch data from the JSON file
with open("branches.json", "r") as file:
    branches = json.load(file)

# Create a folium map centered on Ethiopia with a zoom level focused on the whole country
branch_map = folium.Map(location=[9.145, 40.489], zoom_start=6, tiles="OpenStreetMap")

# Function to add markers to the map for all branches
def add_all_branches():
    for branch in branches:
        latitude = float(branch["latitude"])
        longitude = float(branch["longitude"])

        # Add marker with popup and label
        marker = folium.Marker(
            location=[latitude, longitude],
            popup=f"<strong>{branch['branch_name']}</strong>",
            tooltip=branch['branch_name']
        )
        marker.add_to(branch_map)

        # Adding the label to the marker to always be visible
        folium.map.Marker(
            location=[latitude + 0.01, longitude],  # Slightly adjust for visibility
            icon=folium.DivIcon(
                icon_size=(150, 36),
                icon_anchor=(7, 8),
                # html=f'<div style="font-size: 12pt; color: black; font-weight: bold;">{branch["branch_name"]}</div>'
            )
        ).add_to(branch_map)

# Add all branch markers to the map
add_all_branches()

# Save the map to an HTML file
branch_map.save("ethiopia_osm_map_with_all_branches.html")
print("Map saved as 'ethiopia_osm_map_with_all_branches.html'.")

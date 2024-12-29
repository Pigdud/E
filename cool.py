import streamlit as st
from streamlit_folium import st_folium
import folium
import os

# Title
st.title("""
**Welcome to my website!!!**
:orange["section"]
""")

# Map Header
st.header('''
:blue[Smart city solution]
Below is my smart city map! Click on the markers to see details about the infrastructures.
''')

# Define bounds for your custom map
bounds = [[40, -75], [35, -70]]  # Replace with actual bounds of your map

# Create a Folium map with no tiles (no background map)
city_map = folium.Map(location=[37.5, -72.5], zoom_start=5, crs="Simple", tiles=None)

# Add your custom map image as an overlay
folium.raster_layers.ImageOverlay(
    image="comp project.png",  # Path to your map image
    bounds=bounds,
    opacity=0.8,    
).add_to(city_map)

# Infrastructure details
infrastructures = [
    {
        "name": "Trash to Electricity",
        "location": [38.5, -74],
        "details": "With this, we can solve our trash problem and produce a lot of electricity.",
        "imagee" : "trashtoe.png"
    },
    {
        "name": "Desalination",
        "location": [35.8, -74],
        "details": "With this, we can turn seawater into drinking water, creating unlimited water resources.",
        "imagee": "Desalination.png"
    },
    {
        "name": "Maglev",
        "location": [39.5, -71],
        "details": "We can save resources with this type of railway.",
        "imagee": "railroad.png"
    },
    {
        "name": "Power Tree",
        "location": [36, -71],
        "details": "These trees receive signals from space and transform them to our devices.",
        "imagee": "tree.png"
    },  
    {
        "name": "Power Path",
        "location": [37.5, -72],
        "details": "When people walk on it, it generates energy.",
        "imagee": "powerpath.png"
    },
    {
        "name": "Smart Apartment",
        "location": [35.5, -70.5],
        "details": "These apartments have solar panels and use water from desalination.",
        "imagee": "apt.png"
    }
]

# Add markers with clickable popups
for infra in infrastructures:    


    html = f"""
    <b style="font-size: 16px;">{infra['name']}</b><br>
    <p style="font-size: 14px;">{infra['details']}</p>\
    <img src="trashtoe.png" alt="{infra['name']}" width="250" height="250"></img>
    """
    
    iframe = folium.IFrame(html, width=300, height=350)
    popup = folium.Popup(iframe, max_width=250)
    
    # Add the marker to the map
    folium.Marker(
        location=infra["location"],
        popup=popup,
        tooltip=infra["name"]  # Text that appears on hover
    ).add_to(city_map)

# Display the map in Streamlit
st_folium(city_map, width=700, height=500)
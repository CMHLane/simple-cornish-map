# TD2 - Datavizz sous Python

# 1 - GIF

# 1 Images fournies

import imageio.v2 as imageio
import os
MainDir = "C:/Users/UTILISATEUR/Desktop/SD3/S5/Enseignements/SAE5-EMS-01/Etude_stat_voitElec2040-SP/DataForTP_20231022/AralSeaDrying"
files = os.listdir(MainDir)
Output_file = "C:/Users/UTILISATEUR/Desktop/SD3/S5/Enseignements/SAE5-EMS-01/Etude_stat_voitElec2040-SP/mygif.gif"
images_path = [os.path.join(MainDir,file) for file in files]
images = []
for img in images_path:
    images.append(imageio.imread(img))
imageio.mimsave(Output_file, images, fps=4,loop=10)
# Défaut majeur : Les images ne comportent pas toutes l'année
# Les années : 1994,2004,2014,2022
# Message : dessechement de la mer sur une longue période
# Loop : nb répétitions
# Fps : vitesse

# 2 Mes images

MainDir = "C:/Users/UTILISATEUR/Desktop/SD3/S5/Enseignements/SAE5-EMS-01/Etude_stat_voitElec2040-SP/test"
files = os.listdir(MainDir)
Output_file = "C:/Users/UTILISATEUR/Desktop/SD3/S5/Enseignements/SAE5-EMS-01/Etude_stat_voitElec2040-SP/MYmygif.gif"
images_path = [os.path.join(MainDir,file) for file in files]
images = []
for img in images_path:
    images.append(imageio.imread(img))
imageio.mimsave(Output_file, images, fps=4,loop=10)

# 2 - Cartes interactives

# 1 Chargement librairies et données

import folium
from folium import plugins
from folium.plugins import BeautifyIcon
import pandas as pd
import webbrowser
import numpy as np
from folium.plugins import FloatImage
from folium.features import DivIcon

F_in_StationLocations = "C:/Users/UTILISATEUR/Desktop/SD3\S5/Enseignements/SAE5-EMS-01/Etude_stat_voitElec2040-SP/DataForTP_20231022/StationsLocation.xlsx"
F_out = "C:/Users/UTILISATEUR/Desktop/SD3/S5/Enseignements/SAE5-EMS-01/Etude_stat_voitElec2040-SP/ManausMap.html"
df_StationsLocation = pd.read_excel(F_in_StationLocations)
df_StationsLocation.columns = ['Label', 'Lat', 'Lon']
df_airport=pd.DataFrame(data=np.array([[-3.15,-59.9833]]),columns=['latitude','longitude'])

# 2 Carte basique

study_zone_map = folium.Map(location=[-3.1190, -60.0217],tiles = 'OpenStreetMap',width="100%",height="100%",)
study_zone_map.save(F_out)

webbrowser.open(F_out)

# W et H à 100 % pour plein écran
# Pays : Brézil

# folium.Map()
 # |  Parameters
 # |  ----------
 # |  location: tuple or list, default None
 # |      Latitude and Longitude of Map (Northing, Easting).
 # |  width: pixel int or percentage string (default: '100%')
 # |      Width of the map.
 # |  height: pixel int or percentage string (default: '100%')
 # |      Height of the map.
 # |  tiles: str or TileLayer or :class:`xyzservices.TileProvider`, default 'OpenStreetMap'
 # |      Map tileset to use. Can choose from a list of built-in tiles,
 # |      pass a :class:`xyzservices.TileProvider`,
 # |      pass a custom URL, pass a TileLayer object,
 # |      or pass `None` to create a map without tiles.
 # |      For more advanced tile layer options, use the `TileLayer` class.
 # |  min_zoom: int, optional, default 0
 # |      Minimum allowed zoom level for the tile layer that is created.
 # |      Filled by xyzservices by default.
 # |  max_zoom: int, optional, default 18
 # |      Maximum allowed zoom level for the tile layer that is created.
 # |      Filled by xyzservices by default.
 # |  zoom_start: int, default 10
 # |      Initial zoom level for the map.
 # |  attr: string, default None
 # |      Map tile attribution; only required if passing custom tile URL.
 # |  crs : str, default 'EPSG3857'
 # |      Defines coordinate reference systems for projecting geographical points
 # |      into pixel (screen) coordinates and back.
 # |      You can use Leaflet's values :
 # |      * EPSG3857 : The most common CRS for online maps, used by almost all
 # |      free and commercial tile providers. Uses Spherical Mercator projection.
 # |      Set in by default in Map's crs option.
 # |      * EPSG4326 : A common CRS among GIS enthusiasts.
 # |      Uses simple Equirectangular projection.
 # |      * EPSG3395 : Rarely used by some commercial tile providers.
 # |      Uses Elliptical Mercator projection.
 # |      * Simple : A simple CRS that maps longitude and latitude into
 # |      x and y directly. May be used for maps of flat surfaces
 # |      (e.g. game maps). Note that the y axis should still be inverted
 # |      (going from bottom to top).
 # |  control_scale : bool, default False
 # |      Whether to add a control scale on the map.
 # |  prefer_canvas : bool, default False
 # |      Forces Leaflet to use the Canvas back-end (if available) for
 # |      vector layers instead of SVG. This can increase performance
 # |      considerably in some cases (e.g. many thousands of circle
 # |      markers on the map).
 # |  no_touch : bool, default False
 # |      Forces Leaflet to not use touch events even if it detects them.
 # |  disable_3d : bool, default False
 # |      Forces Leaflet to not use hardware-accelerated CSS 3D
 # |      transforms for positioning (which may cause glitches in some
 # |      rare environments) even if they're supported.
 # |  zoom_control : bool or position string, default True
 # |      Display zoom controls on the map. The default `True` places it in the top left corner.
 # |      Other options are 'topleft', 'topright', 'bottomleft' or 'bottomright'.
 # |  font_size : int or float or string (default: '1rem')
 # |      The font size to use for Leaflet, can either be a number or a
 # |      string ending in 'rem', 'em', or 'px'.
 # |  **kwargs
 # |      Additional keyword arguments are passed to Leaflets Map class:
 # |      https://leafletjs.com/reference.html#map
 # |
 # |  Returns
 # |  -------
 # |  Folium Map Object

# Base maps :
#  |      - "OpenStreetMap"
#  |      - "CartoDB Positron"
#  |      - "CartoDB Voyager"

# 3 Ajouter élements

# 3.1 Marqueurs

icon_star = BeautifyIcon(icon='star', inner_icon_style='color:black;font-size:15px;',background_color='transparent', border_color='transparent',)
# add the icon to the map
folium.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],tooltip="Click me!",popup='Airport in the Popup',icon=icon_star,).add_to(study_zone_map)
# Etoile ajoutée
study_zone_map.save(F_out)
webbrowser.open(F_out)

# 3.2 Cercles

folium.Circle(location=[df_StationsLocation['Lat'][0],df_StationsLocation['Lon'][1]],tooltip="Click me!",popup=df_StationsLocation['Label'][0],color='crimson',fill=True,radius=15).add_to(study_zone_map)
# Point rouge INPA
study_zone_map.save(F_out)
webbrowser.open(F_out)

folium.map.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],icon=DivIcon(icon_size=(150,36),icon_anchor=(0,0),html='Airport in the map',)).add_to(study_zone_map)
# Marqueur avion : aéroport

study_zone_map.save(F_out)
webbrowser.open(F_out)

# 3.3 Labels

folium.map.Marker(location=[df_airport.latitude.values,df_airport.longitude.values],icon=DivIcon(icon_size=(150,36),icon_anchor=(0,0),html='Airport in the map',)).add_to(study_zone_map)

study_zone_map.save(F_out)
webbrowser.open(F_out)

# 3.4 Boucle pour 6 points de collecte

for i in range(len(df_StationsLocation)):
  folium.Circle(location=[df_StationsLocation['Lat'][i],df_StationsLocation['Lon'][i]],color='crimson',fill=True,radius=15).add_to(study_zone_map)
  folium.map.Marker(location=[df_StationsLocation['Lat'][i],df_StationsLocation['Lon'][i]],icon=DivIcon(icon_size=(150,36),icon_anchor=(0,0),html=df_StationsLocation['Label'][i],)).add_to(study_zone_map)

study_zone_map.save(F_out)
webbrowser.open(F_out)

# 3.5 Ajout mini carte

minimap = plugins.MiniMap(zoom_level_offset=-7)
study_zone_map.add_child(minimap)

study_zone_map.save(F_out)
webbrowser.open(F_out)

# 3.6 Légende

legend_html = '''
<div style="position: fixed; top: 50px; left: 50px; z-index: 9999;
background-color: white; border:2px solid grey; border-radius:3px; padding: 10px;">
&nbsp;<i class="fa-solid fa-church" style="color:blue"></i><span> &nbsp; Places to
see </span><br>
&nbsp;<i class="fa-solid fa-umbrella-beach" style="color:green"></i><span> &nbsp;
Beach</span><br>
&nbsp;<i class="fa fa-star" style="color:black"></i><span> &nbsp; Meteorological
station</span><br>
&nbsp;<i class="fa-solid fa-circle" style="color:red"></i><span> &nbsp; River
sample</span><br>
</div>
'''
study_zone_map.get_root().html.add_child(folium.Element(legend_html))

study_zone_map.save(F_out)
webbrowser.open(F_out)
# Element html css ajouté

# 3.7 Echelle

study_zone_map.control_scale = True

study_zone_map.save(F_out)
webbrowser.open(F_out)

# Flèche nord
north_arrow_url ='https://upload.wikimedia.org/wikipedia/commons/8/84/North_Pointer.svg'
# Add the north arrow image to the map
FloatImage(north_arrow_url,bottom=75, left=85,scale=0.2).add_to(study_zone_map)

study_zone_map.save(F_out)
webbrowser.open(F_out)

# 4 Github

# 5 Carte perso

S_in = "C:/Users/UTILISATEUR/Desktop/SD3/S5/Enseignements/SAE5-EMS-01/Etude_stat_voitElec2040-SP/schools.xlsx"
S_out = "C:/Users/UTILISATEUR/Desktop/SD3/S5/Enseignements/SAE5-EMS-01/Etude_stat_voitElec2040-SP/schools.html"
df_schools = pd.read_excel(S_in)
print(df_schools)
#                   Label      Lat     Lon       declat     declon
# 0        Truro Hospital  50.2661 -5.0922   50°15'58"N  5°05'32"W
# 1  Summer Court School   50.3694 -4.0922   50°22'10"N  4°57'57"W
# 2      Trewirgie School  50.2294 -5.9658   50°13'46"N  5°13'42"W
# 3        Bolitho School  50.1200 -5.5475  50°07'12"N   5°32'51"W

# 2 Carte basique

zone_map = folium.Map(location=[50.15, -5.35],tiles = 'OpenStreetMap',width="100%",height="100%",)
zone_map.save(S_out)

webbrowser.open(S_out)

for i in range(len(df_schools)):
    if df_schools['Label'][i] == "Truro Hospital":
        folium.Marker(
            location=[df_schools['Lat'][i], df_schools['Lon'][i]],
            icon=folium.Icon(color="black", icon="star", prefix="fa"),
            popup=f"<b>{df_schools['Label'][i]}</b>"
        ).add_to(zone_map)
    else:
        folium.Circle(
            location=[df_schools['Lat'][i], df_schools['Lon'][i]],
            color='crimson',
            fill=True,
            fill_opacity=0.6,
            radius=1000
        ).add_to(zone_map)

        folium.Marker(
            location=[df_schools['Lat'][i], df_schools['Lon'][i]],
            icon=DivIcon(
                icon_size=(600, 200),
                icon_anchor=(0, 0),
                html=f'<div style="font-size: 12px; color: black;">{df_schools["Label"][i]}</div>',
            )
        ).add_to(zone_map)
zone_map.save(S_out)

webbrowser.open(S_out)

# Flèche nord
north_arrow_url ='https://upload.wikimedia.org/wikipedia/commons/8/84/North_Pointer.svg'
# Add the north arrow image to the map
FloatImage(north_arrow_url,bottom=65, left=75,scale=0.2).add_to(zone_map)

zone_map.save(S_out)
webbrowser.open(S_out)

zone_map.add_child(minimap)

zone_map.save(S_out)

webbrowser.open(S_out)

legend_html0 = '''
<div style="position: fixed; top: 50px; left: 50px; z-index: 9999;
background-color: white; border:2px solid grey; border-radius:3px; padding: 10px;">
&nbsp;<i class="fa fa-star" style="color:black"></i><span> &nbsp; Truro Hospital</span><br>
&nbsp;<i class="fa fa-circle" style="color:red"></i><span> &nbsp; Schools</span><br>
</div>
'''
zone_map.get_root().html.add_child(folium.Element(legend_html0))
zone_map.save(S_out)

webbrowser.open(S_out)
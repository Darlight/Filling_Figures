"""
Universidad del Valle de Guatemala
Gráficas por computadora
Seccion 10
Lic. Dennis Aldana
Mario Perdomo
18029

Lab1.py
Proposito: Mostrar los poligonos rellenados en el renderer
"""
from tezt import Render, GREEN, BLUE, RED, WHITE


bitmap = Render()
print(bitmap.glInit())
bitmap.glCreateWindow()

# Polygon 1
polygon = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]
bitmap.drawPolygon(polygon)

# Polygon 2
polygon = [(321, 335), (288, 286), (339, 251), (374, 302)]
bitmap.drawPolygon(polygon)
# Polygon 3
polygon = [(377, 249), (411, 197), (436, 249)]
bitmap.drawPolygon(polygon)

#bitmap.glColor(255,0,0)
#bitmap.inundation(168, 379, WHITE, RED)
# Polygon 4
polygon = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180)]
bitmap.drawPolygon(polygon)

# Polygon 5
polygon = [(682, 175), (708, 120), (735, 148), (739, 170)]
bitmap.drawPolygon(polygon)

#Star
bitmap.glColor(255,0,0)
bitmap.inundation(168, 379, WHITE, RED)
bitmap.inundation(182, 332, WHITE, RED)

# Square
#bitmap.inundation(330, 200, WHITE, RED)

#Triangle
#bitmap.inundation(379, 248, WHITE, BLUE)

#Tea server

#Hole





bitmap.glFinish('out.bmp')
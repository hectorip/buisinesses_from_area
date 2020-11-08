from shapely.geometry import Point, Polygon
from poly import polygon, poly2
pt = Point(19.3518607, -99.10016619999999)
poly = Polygon(poly2)
print(poly.contains(pt))
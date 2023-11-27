from classes.check import Check
from classes.polygon import Polygon
from classes.render import Render
from classes.point import Point


old_points = []

polygon_size = int(input("Please set a size of polygon (just a count of segments).\n"))
# I`ve added 1 to duplication of first point, because the polygon must be closed.
for i in range(polygon_size + 1):
    point = input("Please input a point`s coordinates. Example - 1,1.\n").split(",")
    old_points.append(Point(float(point[0]), float(point[1])))

old_points_as_list_of_tuple = [point.convert() for point in old_points]
print(old_points_as_list_of_tuple)

segment_i = int(
    input(
        f"Please input segment index. In your case it would be from 0 to {len(old_points) - 2}\n"
    )
)
offset = float(input(f"Please input offset.\n"))
Check(old_points_as_list_of_tuple, segment_i).check_points_lst()
polygon = Polygon(old_points, offset, segment_i)
new_vert = polygon.segment_offset()
render = Render(old_points_as_list_of_tuple, new_vert)
render.render_overlay()
render.render_subplot()

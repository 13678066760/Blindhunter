import numpy as np

dref = 10


class Point:
    def __init__(self, y, x):
        self.y = int(y)
        self.x = int(x)

    def __repr__(self):
        return f"Point(y={self.y}, x={self.x})"


def find_ref_point(a: Point, b: Point, ref=dref):
    x_a, y_a = a.x, a.y
    x_b, y_b = b.x, b.y
    x_c = x_b + ref

    if y_b == y_a:
        return Point(y_a, x_c)

    y_c = y_a + (x_c - x_a) * (y_b - y_a) / (x_b - x_a)
    return Point(y_c, x_c)


def sort_points_by_slope(points, ref_point):
    def slope(point):
        dx = point.x - ref_point.x
        dy = point.y - ref_point.y
        if dx == 0:
            return float('inf')  # 对于 x 为零的情况，斜率为正无穷大
        return dy / dx

    return sorted(points, key=slope)


def sort_points_by_x_slope(points, ref_point):
    def slope(point):
        dx = point.x - ref_point.x
        dy = point.y - ref_point.y
        if dx == 0:
            return float('inf')  # 对于 x 为零的情况，斜率为正无穷大
        return dy / dx

    return sorted(points, key=lambda point: (point.x, slope(point)))


class Object:
    def __init__(self, x, y, z, w, h, d):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.h = h
        self.d = d

    def to_plane(self, plane):
        global coords
        if plane == 'xy':
            coords = [Point(self.y - self.d / 2, self.x - self.w / 2),
                      Point(self.y - self.d / 2, self.x + self.w / 2),
                      Point(self.y + self.d / 2, self.x + self.w / 2),
                      Point(self.y + self.d / 2, self.x - self.w / 2)]
        elif plane == 'xz':
            coords = [Point(self.z - self.h / 2, self.x - self.w / 2),
                      Point(self.z - self.h / 2, self.x + self.w / 2),
                      Point(self.z + self.h / 2, self.x + self.w / 2),
                      Point(self.z + self.h / 2, self.x - self.w / 2)]
        elif plane == 'yz':
            coords = [Point(self.z - self.h / 2, self.y - self.d / 2),
                      Point(self.z - self.h / 2, self.y + self.d / 2),
                      Point(self.z + self.h / 2, self.y + self.d / 2),
                      Point(self.z + self.h / 2, self.y - self.d / 2)]
        return coords


class Occluder(Object):
    def __init__(self, x, y, z, w, h, d):
        super().__init__(x, y, z, w, h, d)


class Sensor:
    def __init__(self, x, y, z, d_max, theta_h, theta_v):
        self.x = x
        self.y = y
        self.z = z
        self.d_max = d_max
        self.theta_h = np.radians(theta_h)
        self.theta_v = np.radians(theta_v)

    def to_plane_xy(self):
        apex = (self.x, self.y)
        left_x = right_x = self.x + self.d_max
        left_y = self.y - self.d_max * np.tan(self.theta_h / 2)
        right_y = self.y + self.d_max * np.tan(self.theta_h / 2)
        left_base = (left_x, left_y)
        right_base = (right_x, right_y)
        return apex, left_base, right_base

    def xy_colluded(self, occluder: Occluder):
        if occluder.x <= self.x:
            return None
        points = occluder.to_plane('xy')
        apex, left_base, right_base = self.to_plane_xy()
        target_points = sort_points_by_slope(points, Point(apex[1], apex[0]))
        cur_points = sort_points_by_x_slope(points, Point(apex[1], apex[0]))
        left_ref = find_ref_point(Point(apex[1], apex[0]), Point(left_base[1], left_base[0]),
                                  ref=cur_points[3].x + dref - self.d_max)
        right_ref = find_ref_point(Point(apex[1], apex[0]), Point(right_base[1], right_base[0]),
                                   ref=cur_points[3].x + dref - self.d_max)

        extended_points = [find_ref_point(Point(apex[1], apex[0]), target_points[0]),
                           find_ref_point(Point(apex[1], apex[0]), target_points[3])]
        if extended_points[1].y < left_ref.y or extended_points[0].y > right_ref.y:
            return None

        return [extended_points[0], extended_points[1], target_points[3],
                cur_points[3], target_points[0]]


class WShape:
    def __init__(self, v1, v2, v3, v4, v5):
        self.vertices = [v1, v2, v3, v4, v5]
        self.segments = [
            (v1, v2),
            (v2, v3),
            (v3, v4),
            (v4, v5),
            (v5, v1)
        ]

    def is_point_inside(self, point):
        x, y = point.x, point.y
        num_vertices = len(self.vertices)
        count = 0

        for i in range(num_vertices):
            x1, y1 = self.vertices[i].x, self.vertices[i].y
            x2, y2 = self.vertices[(i + 1) % num_vertices].x, self.vertices[(i + 1) % num_vertices].y

            if y1 <= y < y2 or y2 <= y < y1:
                intersect_x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                if intersect_x > x:
                    count += 1

        return count % 2 == 1

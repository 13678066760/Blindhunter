import matplotlib.pyplot as plt
import numpy as np
import occcluded_area

plt.figure(figsize=(10, 10))

for y in range(51):
    plt.plot([0, 50], [y, y], color='gray', linewidth=0.5)
    plt.plot([y, y], [0, 50], color='gray', linewidth=0.5)

# 初始帧
occluder = occcluded_area.Occluder(10, 30, 0, 2, 2, 2)
sensor = occcluded_area.Sensor(0, 25, 0, 40, 45, 45)
occluder_coords = occluder.to_plane('xy')
result = sensor.xy_colluded(occluder)
points_to_bold = [(0, 25), (9, 24), (22, 24)]
red_num = 1

for point in points_to_bold:
    x, y = point
    plt.scatter([y], [x], color='red', alpha= red_num * 0.3, s=100, zorder=5)
    red_num += 1

for point in occluder_coords:
    x, y = point.x, point.y
    plt.scatter([y], [x], color='orange', s=100, zorder=5, alpha=0.3)

for point in result:
    x, y = point.x, point.y
    plt.scatter([y], [x], color='blue', s=100, zorder=5)

rects = []
rect = []
v1 = result[0]
v2 = result[1]
v3 = result[2]
v4 = result[3]
v5 = result[4]
w_shape = occcluded_area.WShape(v1, v2, v3, v4, v5)

for i in range(51):
    for j in range(51):
        test_point = occcluded_area.Point(i, j)
        if w_shape.is_point_inside(test_point):
            rects.append(test_point)

x, y = occluder_coords[0].x, occluder_coords[0].y
plt.fill_between([y, y + 1], x, x + 1, color='orange', alpha=0.2)
plt.fill_between([y + 1, y + 2], x + 1, x + 2, color='orange', alpha=0.2)
plt.fill_between([y + 1, y + 2], x, x + 1, color='orange', alpha=0.2)
plt.fill_between([y, y + 1], x + 1, x + 2, color='orange', alpha=0.2)

for rect in rects:
    x, y = rect.x, rect.y
    plt.fill_between([y, y + 1], x, x + 1, color='green', alpha=0.5)

plt.plot([points_to_bold[0][1], result[0].y], [points_to_bold[0][0], result[0].x], linestyle='--', color='gray', label='虚线')
plt.plot([points_to_bold[0][1], result[1].y], [points_to_bold[0][0], result[1].x],  linestyle='--', color='gray', label='虚线')

# 第二帧
occluder = occcluded_area.Occluder(15, 27, 0, 2, 2, 2)
sensor = occcluded_area.Sensor(9, 24, 0, 40, 45, 45)
occluder_coords = occluder.to_plane('xy')
result = sensor.xy_colluded(occluder)

for point in occluder_coords:
    x, y = point.x, point.y
    plt.scatter([y], [x], color='orange', s=100, zorder=5, alpha=0.6)

for point in result:
    x, y = point.x, point.y
    plt.scatter([y], [x], color='blue', s=100, zorder=5)

rects = []
rect = []
v1 = result[0]
v2 = result[1]
v3 = result[2]
v4 = result[3]
v5 = result[4]
w_shape = occcluded_area.WShape(v1, v2, v3, v4, v5)

for i in range(51):
    for j in range(51):
        test_point = occcluded_area.Point(i, j)
        if w_shape.is_point_inside(test_point):
            rects.append(test_point)

x, y = occluder_coords[0].x, occluder_coords[0].y
plt.fill_between([y, y + 1], x, x + 1, color='orange', alpha=0.4)
plt.fill_between([y + 1, y + 2], x + 1, x + 2, color='orange', alpha=0.4)
plt.fill_between([y + 1, y + 2], x, x + 1, color='orange', alpha=0.4)
plt.fill_between([y, y + 1], x + 1, x + 2, color='orange', alpha=0.4)

for rect in rects:
    x, y = rect.x, rect.y
    plt.fill_between([y, y + 1], x, x + 1, color='green', alpha=0.5)

plt.plot([points_to_bold[1][1], result[0].y], [points_to_bold[1][0], result[0].x], linestyle='--', color='gray', label='虚线')
plt.plot([points_to_bold[1][1], result[1].y], [points_to_bold[1][0], result[1].x],  linestyle='--', color='gray', label='虚线')

# 第三帧
occluder = occcluded_area.Occluder(24, 27, 0, 2, 2, 2)
sensor = occcluded_area.Sensor(22, 24, 0, 40, 45, 45)
occluder_coords = occluder.to_plane('xy')
result = sensor.xy_colluded(occluder)

for point in occluder_coords:
    x, y = point.x, point.y
    plt.scatter([y], [x], color='orange', s=100, zorder=5, alpha=0.9)

for point in result:
    x, y = point.x, point.y
    plt.scatter([y], [x], color='blue', s=100, zorder=5)

rects = []
rect = []
v1 = result[0]
v2 = result[1]
v3 = result[2]
v4 = result[3]
v5 = result[4]
w_shape = occcluded_area.WShape(v1, v2, v3, v4, v5)

for i in range(51):
    for j in range(51):
        test_point = occcluded_area.Point(i, j)
        if w_shape.is_point_inside(test_point):
            rects.append(test_point)

x, y = occluder_coords[0].x, occluder_coords[0].y
plt.fill_between([y, y + 1], x, x + 1, color='orange', alpha=0.6)
plt.fill_between([y + 1, y + 2], x + 1, x + 2, color='orange', alpha=0.6)
plt.fill_between([y + 1, y + 2], x, x + 1, color='orange', alpha=0.6)
plt.fill_between([y, y + 1], x + 1, x + 2, color='orange', alpha=0.6)

for rect in rects:
    x, y = rect.x, rect.y
    plt.fill_between([y, y + 1], x, x + 1, color='green', alpha=0.5)

plt.plot([points_to_bold[2][1], result[0].y], [points_to_bold[2][0], result[0].x], linestyle='--', color='gray', label='虚线')
plt.plot([points_to_bold[2][1], result[1].y], [points_to_bold[2][0], result[1].x],  linestyle='--', color='gray', label='虚线')


# 设置坐标轴的范围
plt.xlim(0, 50)
plt.ylim(0, 50)

# 设置坐标轴刻度
plt.xticks(np.arange(0, 51, step=1))
plt.yticks(np.arange(0, 51, step=1))

# 设置网格线
plt.grid(which='both', color='gray', linestyle='-', linewidth=0.5)


# 批注
plt.plot([0.80], [1.02], marker='s', markersize=10, color='green', transform=plt.gca().transAxes, clip_on=False)
plt.text(0.82, 1.02, 'Occlude Area', color='green', verticalalignment='center', transform=plt.gca().transAxes, clip_on=False)
plt.plot([0.80], [1.05], marker='s', markersize=10, color='red', transform=plt.gca().transAxes, clip_on=False)
plt.text(0.82, 1.05, 'Camera', color='red', verticalalignment='center', transform=plt.gca().transAxes, clip_on=False)
plt.plot([0.80], [1.08], marker='s', markersize=10, color='orange', transform=plt.gca().transAxes, clip_on=False)
plt.text(0.82, 1.08, 'Occluder', color='orange', verticalalignment='center', transform=plt.gca().transAxes, clip_on=False)
plt.plot([0.80], [1.11], marker='s', markersize=10, color='blue', transform=plt.gca().transAxes, clip_on=False)
plt.text(0.82, 1.11, 'Edge Points', color='blue', verticalalignment='center', transform=plt.gca().transAxes, clip_on=False)
plt.show()

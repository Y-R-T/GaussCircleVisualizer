import math
import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.colors as mcolors
import numpy as np

def generate_points_in_region(max_x):
    """
    生成满足 0 < y < x 的所有整数点
    """
    points = []
    for x in range(1, max_x + 1):
        for y in range(1, x):
            points.append((x, y))
    return points

def distance_from_origin(point):
    """
    计算点到原点 (0, 0) 的欧几里得距离
    """
    x, y = point
    return math.hypot(x, y)

def angle_from_xaxis(point):
    """
    计算点相对于 x 轴(正向)的极角, 范围 [0, 2π)
    """
    x, y = point
    angle = math.atan2(y, x)
    if angle < 0:
        angle += 2 * math.pi
    return angle

def group_points_by_distance(points, tol=1e-5):
    """
    将点按到原点距离分组, 返回:
    {
       distance1: [ (x1,y1), (x2,y2), ... ],
       distance2: [ (x3,y3), ... ],
       ...
    }
    并确保距离的分组具有精度容忍度
    """
    dist_dict = defaultdict(list)
    for p in points:
        d = distance_from_origin(p)
        # 通过四舍五入处理浮点数精度问题
        d_rounded = round(d / tol) * tol
        dist_dict[d_rounded].append(p)
    # 按距离从小到大排序
    sorted_distances = sorted(dist_dict.keys())
    return dist_dict, sorted_distances

def assign_colors(sorted_distances, dist_dict):
    """
    为每个具有多个点的距离分配颜色，返回：
    distance_to_color: { distance: color }
    """
    # 识别需要上色的距离
    color_distances = [d for d in sorted_distances if len(dist_dict[d]) >= 2]
    
    num_colors = len(color_distances)
    if num_colors == 0:
        return {}
    
    # 使用离散色图
    cmap = plt.get_cmap('tab20')
    if num_colors > cmap.N:
        cmap = plt.get_cmap('hsv')  # 如果颜色数量超过tab20，使用hsv
    colors = cmap(np.linspace(0, 1, num_colors))
    
    distance_to_color = {}
    for idx, d in enumerate(color_distances):
        distance_to_color[d] = colors[idx]
    
    return distance_to_color

def plot_arc(ax, center, radius, start_angle, end_angle, color, linewidth=2):
    """
    在ax上绘制从start_angle到end_angle的圆弧
    """
    theta = np.linspace(start_angle, end_angle, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    ax.plot(x, y, color=color, linewidth=linewidth)

def plot_connections(ax, dist_dict, sorted_distances, distance_to_color):
    """
    绘制点之间的连接：
    - 对于具有多个点的距离组，使用圆弧连接，并赋予相同颜色。
    - 对于唯一距离的点，按距离顺序用黑色直线连接。
    - 不同距离组之间不连接。
    """
    # 分离唯一距离点和多点距离组
    unique_points = []
    multiple_groups = []
    for d in sorted_distances:
        points = dist_dict[d]
        if len(points) == 1:
            unique_points.append(points[0])
        else:
            multiple_groups.append((d, points))
    
    # 按距离排序唯一距离点
    unique_points_sorted = sorted(unique_points, key=lambda p: distance_from_origin(p))
    
    # 绘制唯一距离点的黑色直线连接
    if unique_points_sorted:
        x_unique = [p[0] for p in unique_points_sorted]
        y_unique = [p[1] for p in unique_points_sorted]
        ax.plot(x_unique, y_unique, color='black', linestyle='-', linewidth=1, label='Unique Distance Connections')
        ax.scatter(x_unique, y_unique, color='black', zorder=5)
    
    # 绘制多点距离组的圆弧连接
    for d, points in multiple_groups:
        # 按极角排序
        points_sorted = sorted(points, key=lambda p: angle_from_xaxis(p))
        angles = [angle_from_xaxis(p) for p in points_sorted]
        radius = d
        color = distance_to_color.get(d, 'black')
        
        # 连接相邻点使用圆弧
        for i in range(len(points_sorted)):
            p1 = points_sorted[i]
            p2 = points_sorted[(i + 1) % len(points_sorted)]  # 环状连接
            angle1 = angle_from_xaxis(p1)
            angle2 = angle_from_xaxis(p2)
            
            # 确保从angle1到angle2的最短路径
            delta_angle = angle2 - angle1
            if delta_angle <= -math.pi:
                angle2 += 2 * math.pi
            elif delta_angle > math.pi:
                angle2 -= 2 * math.pi
            
            plot_arc(ax, (0,0), radius, angle1, angle2, color, linewidth=2)
        
        # 绘制散点，赋予颜色
        x_vals = [p[0] for p in points_sorted]
        y_vals = [p[1] for p in points_sorted]
        ax.scatter(x_vals, y_vals, color=color, zorder=5)
    
def plot_grid_and_boundaries(ax, points, max_coord):
    """
    绘制y=0和y=x的边界线
    """
    ax.plot([0, max_coord], [0, 0], 'k--', label='y=0')
    ax.plot([0, max_coord], [0, max_coord], 'k--', label='y=x')

def create_legend(ax, distance_to_color):
    """
    创建颜色图例，仅展示存在相同距离的格点
    """
    handles = []
    labels = []
    for d, color in distance_to_color.items():
        handles.append(plt.Line2D([], [], color=color, linewidth=2))
        labels.append(f'd = {d:.2f}')
    if handles:
        ax.legend(handles, labels, title='Distances with ≥2 points', loc='upper right')
    else:
        ax.legend()

def main():
    # 预设最大x值
    max_x = 20  # 根据需要调整
    
    # 生成整数点
    points = generate_points_in_region(max_x)
    
    # 按距离分组
    dist_dict, sorted_distances = group_points_by_distance(points)
    
    # 分配颜色，仅对存在多个点的距离赋色
    distance_to_color = assign_colors(sorted_distances, dist_dict)
    
    # 设置绘图
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 绘制连接
    plot_connections(ax, dist_dict, sorted_distances, distance_to_color)
    
    # 绘制原点
    ax.scatter(0, 0, color='black', s=50, label='Origin (0,0)', zorder=5)
    
    # 绘制边界线
    max_coord = max(max([p[0] for p in points], default=1),
                    max([p[1] for p in points], default=1)) + 1
    plot_grid_and_boundaries(ax, points, max_coord)
    
    # 设置坐标轴
    ax.set_xlim(0, max_coord)
    ax.set_ylim(0, max_coord)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('整数点连接图：同距离点用圆弧连接，其他点按距离排序用黑色直线连接')
    ax.grid(True)
    ax.set_aspect('equal', 'box')
    
    # 创建图例
    create_legend(ax, distance_to_color)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import math
from collections import defaultdict

def generate_integer_points(max_x):
    """
    生成满足 0 < y < x 且x、y为整数的点
    """
    points = []
    for x in range(1, max_x + 1):
        for y in range(1, x):
            points.append((x, y))
    return points

def compute_distance(point):
    """
    计算点到原点的欧几里得距离
    """
    return math.hypot(point[0], point[1])

def sort_points_by_distance(points):
    """
    按距离从小到大排序点
    """
    return sorted(points, key=compute_distance)

def plot_polyline(sorted_points):
    """
    绘制从原点开始，按照排序顺序连接的折线，
    仅当两个连续点的距离不同时时绘制连接线
    """
    # 包含原点
    polyline_points = [(0, 0)] + sorted_points
    distances = [compute_distance(p) for p in polyline_points]
    
    # 准备绘图数据
    x_vals = []
    y_vals = []
    segments = []

    for i in range(1, len(polyline_points)):
        prev_point = polyline_points[i - 1]
        current_point = polyline_points[i]
        prev_distance = distances[i - 1]
        current_distance = distances[i]
        
        # 添加当前点到列表
        x_vals.append(current_point[0])
        y_vals.append(current_point[1])
        
        # 如果距离不同，则添加线段
        if current_distance != prev_distance:
            segments.append((prev_point, current_point))
        else:
            # 距离相同，不连接线
            pass

    # 开始绘图
    plt.figure(figsize=(10, 10))
    
    # 绘制所有点，包括原点
    all_x = [p[0] for p in polyline_points]
    all_y = [p[1] for p in polyline_points]
    plt.scatter(all_x, all_y, color='red', label='Points')
    
    # 绘制连接线
    for seg in segments:
        x_values = [seg[0][0], seg[1][0]]
        y_values = [seg[0][1], seg[1][1]]
        plt.plot(x_values, y_values, color='blue')
    
    # 绘制y=0和y=x的边界（可选）
    max_coord = max(all_x + all_y) + 1
    plt.plot([0, max_coord], [0, 0], 'k--', label='y=0')  # y=0
    plt.plot([0, max_coord], [0, max_coord], 'g--', label='y=x')  # y=x
    
    plt.title('按距离排序的连续折线（相同距离的点不连接）')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def main():
    # 预设最大x值
    max_x = 20  # 您可以根据需要调整这个值
    
    # 生成整数点
    points = generate_integer_points(max_x)
    
    # 按距离排序
    sorted_points = sort_points_by_distance(points)
    
    # 绘制折线
    plot_polyline(sorted_points)

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import math
from itertools import combinations

def generate_integer_points(max_x):
    """
    生成满足 0 < y < x 且x、y为整数的点
    """
    points = []
    for x in range(1, max_x + 1):
        for y in range(1, x):
            points.append((x, y))
    return points

def compute_distances(points):
    """
    计算每个点到原点的距离
    """
    return [(point, math.hypot(point[0], point[1])) for point in points]

def find_closest_pair(points_with_distances):
    """
    找到距离原点最近的两个点
    """
    sorted_points = sorted(points_with_distances, key=lambda x: x[1])
    if len(sorted_points) < 2:
        return None
    return sorted_points[0][0], sorted_points[1][0]

def plot_points_and_connections(points, connections):
    """
    绘制点和连接线
    """
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]
    
    plt.figure(figsize=(8, 8))
    plt.scatter(x_vals, y_vals, color='blue')
    
    # 绘制连接线
    for conn in connections:
        x_values = [conn[0][0], conn[1][0]]
        y_values = [conn[0][1], conn[1][1]]
        plt.plot(x_values, y_values, color='red')
    
    # 绘制y=0和y=x的边界（可选）
    plt.plot([0, max(x_vals)+1], [0, 0], 'k--')  # y=0
    plt.plot([0, max(x_vals)+1], [0, max(x_vals)+1], 'k--')  # y=x
    
    plt.title('整数点及其连接')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def main():
    # 预设最大x值
    max_x = 20  # 您可以根据需要调整这个值
    
    # 生成整数点
    points = generate_integer_points(max_x)
    
    # 计算距离
    points_with_distances = compute_distances(points)
    
    # 按距离排序
    sorted_points = sorted(points_with_distances, key=lambda x: x[1])
    
    # 连接点：依次每两个最近的点连接
    connections = []
    used = set()
    for i in range(0, len(sorted_points)-1, 2):
        p1 = sorted_points[i][0]
        p2 = sorted_points[i+1][0]
        connections.append((p1, p2))
    
    # 绘图
    plot_points_and_connections(points, connections)

if __name__ == "__main__":
    main()

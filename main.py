import matplotlib.pyplot as plt
import math

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
    绘制从原点开始，按照排序顺序连接的折线
    """
    # 包含原点
    polyline = [(0, 0)] + sorted_points
    
    x_vals = [p[0] for p in polyline]
    y_vals = [p[1] for p in polyline]
    
    plt.figure(figsize=(10, 10))
    
    # 绘制折线
    plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='blue', label='Polyline')
    
    # 绘制所有点
    plt.scatter(x_vals, y_vals, color='red')
    
    # 绘制y=0和y=x的边界（可选）
    plt.plot([0, max(x_vals)+1], [0, 0], 'k--', label='y=0')  # y=0
    plt.plot([0, max(x_vals)+1], [0, max(x_vals)+1], 'g--', label='y=x')  # y=x
    
    plt.title('按距离排序的连续折线')
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

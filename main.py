import math
import matplotlib.pyplot as plt
from collections import defaultdict

def generate_points_in_region(max_x):
    """
    生成满足 0 < y < x 的所有整数点
    """
    points = []
    for x in range(1, max_x+1):
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
    return math.atan2(y, x)  # atan2返回[-π, π], 但排序即可

def group_points_by_distance(points):
    """
    将点按到原点距离分组, 返回:
    {
       distance1: [ (x1,y1), (x2,y2), ... ],
       distance2: [ (x3,y3), ... ],
       ...
    }
    同时记录距离的有序列表
    """
    dist_dict = defaultdict(list)
    for p in points:
        d = distance_from_origin(p)
        dist_dict[d].append(p)
    # 按距离从小到大排序
    sorted_distances = sorted(dist_dict.keys())
    return dist_dict, sorted_distances

def plot_same_distance_lines(dist_dict, sorted_distances):
    """
    - 对每个距离 d, 如果有多个点, 则按极角排序后相互连线并上色.
    - 如果仅有单个点, 则不连线且用默认颜色(如黑色).
    - 不同距离之间不连线.
    """
    plt.figure(figsize=(10, 10))
    
    # 准备一个简易的调色板, 如果有大量距离, 可考虑使用colormap
    colors = ["blue", "red", "green", "orange", "purple", "brown", 
              "pink", "gray", "olive", "cyan"]
    
    # 先收集所有点, 用于确定绘图范围
    all_points = []
    for dist in sorted_distances:
        all_points.extend(dist_dict[dist])
    max_coord = 1
    if all_points:
        max_coord = max(max(p[0] for p in all_points),
                        max(p[1] for p in all_points)) + 1
    
    # 画出原点
    plt.scatter([0], [0], color='k', label='Origin (0,0)')
    
    color_idx = 0  # 用来在颜色列表中循环
    
    for d in sorted_distances:
        points_d = dist_dict[d]
        if len(points_d) == 1:
            # 仅一个点, 不连线, 用黑色
            x0, y0 = points_d[0]
            plt.scatter([x0], [y0], color='k')
        else:
            # 2 个或以上点, 排序后连线, 并上色
            # 先按极角排序
            points_d_sorted = sorted(points_d, key=angle_from_xaxis)
            
            # 为这组距离选一个颜色
            c = colors[color_idx % len(colors)]
            color_idx += 1
            
            # 连线(不首尾闭合), 并用同一种颜色标记
            # 如果想首尾闭合, 可再补一个首尾连接
            for i in range(len(points_d_sorted) - 1):
                p1 = points_d_sorted[i]
                p2 = points_d_sorted[i+1]
                plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color=c, linewidth=2)
            
            # 将所有该组点画上散点 (同色)
            xvals = [p[0] for p in points_d_sorted]
            yvals = [p[1] for p in points_d_sorted]
            plt.scatter(xvals, yvals, color=c)
    
    # 画上 y=0 和 y=x 的边界线 (可选)
    plt.plot([0, max_coord], [0, 0], 'k--', label='y=0')
    plt.plot([0, max_coord], [0, max_coord], 'k--', label='y=x')
    
    plt.axis('equal')
    plt.xlim(0, max_coord)
    plt.ylim(0, max_coord)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("相同距离的点相互连接，不同距离不连线\n仅当同一距离点数≥2时才上色并连线")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    max_x = 20  # 可根据需要调整
    points = generate_points_in_region(max_x)
    
    # 按距离分组
    dist_dict, sorted_distances = group_points_by_distance(points)
    
    # 绘图
    plot_same_distance_lines(dist_dict, sorted_distances)

if __name__ == "__main__":
    main()

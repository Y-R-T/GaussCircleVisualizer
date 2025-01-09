
# GaussCircleVisualizer

![GaussCircleVisualizer 横幅](https://github.com/yourusername/GaussCircleVisualizer/blob/main/banner.png)
![GaussCircleVisualizer Banner](https://github.com/yourusername/GaussCircleVisualizer/blob/main/banner.png)

## 概述 | Overview

**GaussCircleVisualizer** 是一个基于 Python 的工具，旨在探索和可视化以原点为中心的圆内整数格点的分布。本项目深入研究经典的 [高斯圆问题](https://zh.wikipedia.org/wiki/%E9%AB%98%E6%96%AF%E5%9C%86%E9%97%AE%E9%A2%98) 通过生成格点，根据它们到原点的欧几里得距离进行分组，并提供这些分布的直观可视化表示。

**GaussCircleVisualizer** is a Python-based tool designed to explore and visualize the distribution of integer lattice points within a circle centered at the origin. This project delves into the classic [Gauss Circle Problem](https://en.wikipedia.org/wiki/Gauss_circle_problem) by generating lattice points, grouping them based on their Euclidean distances from the origin, and providing insightful visual representations of these distributions.

## 功能 | Features

- **整数格点生成 | Integer Lattice Point Generation**: 生成所有在指定区域内的整数点 \((x, y)\)（满足 \(0 < y < x\)）。
  
  **Integer Lattice Point Generation**: Generates all integer points \((x, y)\) within a specified region (\(0 < y < x\)).

- **距离计算与分组 | Distance Calculation & Grouping**: 计算每个点到原点的欧几里得距离，并将具有相同或近似距离的点分组。
  
  **Distance Calculation & Grouping**: Computes the Euclidean distance of each point from the origin and groups points with identical or near-identical distances.

- **动态可视化 | Dynamic Visualization**:
  - **圆弧连接 | Circular Connections**: 使用彩色圆弧连接位于同一半径上的点，突出它们的角度分布。
    
    **Circular Connections**: Connects points that lie on the same circle with colored arcs, highlighting their angular distribution.
  
  - **顺序连接 | Sequential Connections**: 使用黑色直线按距离递增顺序连接具有唯一距离的点，并对其进行标注。
    
    **Sequential Connections**: Links points with unique distances using black lines, ordered by increasing distance, and labels them for easy reference.

- **可自定义参数 | Customizable Parameters**: 调整最大坐标值，切换连接线和标签的可见性等。
  
  **Customizable Parameters**: Adjust the maximum coordinate value, toggle visibility of connection lines and labels, and more.

- **交互式绘图 | Interactive Plotting**: 利用 `matplotlib` 提供交互式和高质量的可视化输出。
  
  **Interactive Plotting**: Utilizes `matplotlib` for interactive and high-quality visual outputs.

## 目录 | Table of Contents

- [安装 | Installation](#安装-installation)
- [使用方法 | Usage](#使用方法-usage)
- [示例 | Examples](#示例-examples)
- [贡献 | Contributing](#贡献-contributing)
- [许可证 | License](#许可证-license)
- [鸣谢 | Acknowledgements](#鸣谢-acknowledgements)

## 安装 | Installation

### 前提条件 | Prerequisites

- Python 3.7 或更高版本 | Python 3.7 or higher
- [pip](https://pip.pypa.io/en/stable/)

### 步骤 | Steps

1. **克隆仓库 | Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/GaussCircleVisualizer.git
   cd GaussCircleVisualizer
   ```

2. **创建虚拟环境（可选，但推荐） | Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用: venv\Scripts\activate
   ```

3. **安装所需依赖 | Install Required Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *如果没有提供 `requirements.txt`，请手动安装依赖：*

   *If `requirements.txt` is not provided, install dependencies manually:*

   ```bash
   pip install matplotlib numpy
   ```

## 使用方法 | Usage

运行主脚本以生成并可视化格点：

Run the main script to generate and visualize the lattice points:

```bash
python gauss_circle_visualizer.py
```

### 命令行参数 | Command-Line Arguments

*目前，脚本使用预定义参数。未来的更新可能包括命令行参数支持以增强自定义功能。*

*Currently, the script uses predefined parameters. Future updates may include command-line argument support for enhanced customization.*

### 自定义 | Customization

在 `gauss_circle_visualizer.py` 脚本中，您可以调整以下参数：

Within the `gauss_circle_visualizer.py` script, you can adjust parameters such as:

- **`max_x`**: 定义生成格点的最大 x 坐标值。
  
  **`max_x`**: Defines the maximum x-coordinate for generating lattice points.

- **`show_lines`**: 切换是否显示黑色顺序连接线。
  
  **`show_lines`**: Toggle the visibility of black sequential connection lines.

- **`show_numbers`**: 切换是否在点上显示编号。
  
  **`show_numbers`**: Toggle the visibility of point labels.

*Example snippet:*

```python
def main(show_lines=True, show_numbers=True):
    max_x = 20  # 根据需要调整
    ...
```

*Example snippet:*

```python
def main(show_lines=True, show_numbers=True):
    max_x = 20  # Adjust as needed
    ...
```

## 示例 | Examples

![GaussCircleVisualizer 示例](https://github.com/yourusername/GaussCircleVisualizer/blob/main/example_plot.png)
![GaussCircleVisualizer Example](https://github.com/yourusername/GaussCircleVisualizer/blob/main/example_plot.png)

*上述图像展示了在区域 \(0 < y < x\) 内的格点，具有相同距离的点通过彩色圆弧连接，具有唯一距离的点通过黑色直线连接并进行编号。*

*The above image showcases lattice points within the region \(0 < y < x\), with points sharing the same distance from the origin connected by colored arcs, and unique-distance points connected sequentially with black lines and labeled.*

## 贡献 | Contributing

欢迎贡献！无论是报告错误、建议功能，还是提交 Pull Request，您的参与都非常重要。

Contributions are welcome! Whether it's reporting bugs, suggesting features, or submitting pull requests, your involvement is highly appreciated.

### 贡献步骤 | Steps to Contribute

1. **Fork 仓库 | Fork the Repository**

2. **创建功能分支 | Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **提交您的更改 | Commit Your Changes**

   ```bash
   git commit -m "Add your detailed description"
   ```

4. **推送到分支 | Push to the Branch**

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **打开 Pull Request | Open a Pull Request**

## 许可证 | License

本项目采用 [GNU 通用公共许可证 v3.0](LICENSE)。

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## 鸣谢 | Acknowledgements

- **卡尔·弗里德里希·高斯**: 为高斯圆问题奠定了基础。(这真的需要吗???)
  
  **Carl Friedrich Gauss**: For the foundational Gauss Circle Problem. (Is this really needed???)

- **Matplotlib & NumPy**: 数据可视化和数值计算的关键库。
  
  **Matplotlib & NumPy**: Essential libraries for data visualization and numerical computations.

- **OpenAI ChatGPT**: 协助项目文档和描述。
  
  **OpenAI ChatGPT**: Assisted in project documentation and description.

# fishbot_description

一个基于 ROS 2 的机器人 URDF 描述功能包，用于可视化一个由圆柱体和立方体组成的简易机器人模型（base_link 和 imu_link）。

---

## 📦 功能包简介

- **功能包名称**：`fishbot_description`
- **构建类型**：`ament_cmake`
- **包含内容**：
  - URDF 模型文件：`urdf/first_robot.urdf`
  - Launch 启动文件：`launch/display_robot.launch.py`
- **作用**：通过 `robot_state_publisher` 和 `joint_state_publisher` 发布机器人模型及 TF 变换，并在 RViz2 中显示。

---

## ✅ 依赖项

运行本功能包前，请确保已安装以下 ROS 2 软件包：
## ✅ 依赖项
```bash
sudo apt install ros-${ROS_DISTRO}-robot-state-publisher
sudo apt install ros-${ROS_DISTRO}-joint-state-publisher
sudo apt install ros-${ROS_DISTRO}-rviz2
```
---

## 🚀 编译与运行
1. Ubuntu环境下 下载本工程
```bash
cd ~
git clone https://github.com/NovusNexion/ros2_robot_ws.git
cd ~/ros2_robot_ws/src
```
2. 编译功能包
```bash
cd ~/ros2_robot_ws
colcon build --packages-select fishbot_description
source install/setup.bash
```
3. 启动显示节点
```bash
ros2 launch fishbot_description display_robot.launch.py
```
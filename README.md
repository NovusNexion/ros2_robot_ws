# ROS2 机器人定义

1. RViz显示机器人
一个基于 ROS 2 的机器人 URDF 描述功能包，用于可视化一个由圆柱体和立方体组成的简易机器人模型（base_link 和 imu_link）。

2. Gazebo显示机器人
一个基于 ROS 2 的机器人 URDF 描述功能包，用于可视化一个包括万向轮、底盘、立柱、双臂，以及激光雷达、摄像头、里程计的机器人模型。

---

## 📦 简单机器人URDF功能包简介

- **功能包名称**：`fishbot_description`
- **构建类型**：`ament_cmake`
- **包含内容**：
  - URDF 模型文件：`urdf/first_robot.urdf`
  - Launch 启动文件：`launch/display_robot.launch.py`
- **作用**：通过 `robot_state_publisher` 和 `joint_state_publisher` 发布机器人模型及 TF 变换，并在 RViz2 中显示。


## ✅ 依赖项

运行本功能包前，请确保已安装以下 ROS 2 软件包：
```bash
sudo apt install ros-${ROS_DISTRO}-robot-state-publisher
sudo apt install ros-${ROS_DISTRO}-joint-state-publisher
sudo apt install ros-${ROS_DISTRO}-rviz2
```


## 🚀 编译与运行
1. Ubuntu环境下 下载本工程
```bash
cd ~
git clone git@github.com:NovusNexion/ros2_robot_ws.git
#git clone https://github.com/NovusNexion/ros2_robot_ws.git
cd ~/ros2_robot_ws/src
```
2. 编译功能包
```bash
cd ~/ros2_robot_ws
colcon build --packages-select fishbot_description
source install/setup.bash
```
3. 在RViz显示机器人
```bash
cd ~/ros2_robot_ws
source install/setup.bash
ros2 launch fishbot_description display_robot.launch.py
```

---

## 📦 Gazebo仿真环境机器人URDF功能包简介

- **功能包名称**：`gazebo_bot_description`
- **构建类型**：`ament_cmake`
- **包含内容**：
  - URDF 模型文件：`urdf/gazebo_robot.urdf`
  - Launch 启动文件：`launch/spawn_robot.launch.py`
- **作用**：通过，并在 GAZEBO 中显示。

## ✅ 依赖项

1. ROS 2 与 Gazebo 桥接集成
```bash
sudo apt-get install ros-jazzy-ros-gz
```
2. 安装 gz-harmonic（与 ROS 2 Jazzy 兼容）
安装Gazebo 模拟器本体尚未安装。ros-jazzy-ros-gz 只提供了桥接功能，
需要添加 Gazebo 官方软件源并安装 gz-harmonic（与 ROS 2 Jazzy 兼容）。
2.1. 安装必要工具（如果尚未安装）
2.2. 下载并添加 Gazebo 的 GPG 密钥
2.3. 添加 Gazebo 稳定版软件源（适用于 Ubuntu 24.04 Noble）
2.4. 更新软件包列表
2.5. 安装 Gazebo Harmonic（包含 gz 命令和模拟器）

```bash
sudo apt update
sudo apt install curl lsb-release gnupg

sudo curl -sSL https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] https://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

sudo apt update

sudo apt install gz-harmonic
```

3. 安装后验证
3.1 检查 gz 命令是否可用,应输出 /usr/bin/gz
3.2 启动 Gazebo 图形界面,如果弹出 3D 窗口，则安装成功

```bash
which gz
gz sim
```


## 🚀 gazebo_bot_description 功能包编译与运行
1. 编译功能包
```bash
cd ~/ros2_robot_ws
colcon build --packages-select gazebo_bot_description
source install/setup.bash
```
2. 在Gazebo仿真环境中显示机器人
```bash
cd ~/ros2_robot_ws
source install/setup.bash
ros2 launch gazebo_bot_description spawn_robot.launch.py

```
import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('gazebo_bot_description')
    urdf_file = os.path.join(pkg_share, 'urdf', 'gazebo_robot.urdf')

    # 1. 启动 Gazebo（自动启动桥接）
    start_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': '-r empty.sdf'
        }.items()
    )

    # 2. 生成机器人模型（自动处理 URDF→SDF 转换）
    spawn_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_spawn_model.launch.py'
            )
        ),
        launch_arguments={
            'file': urdf_file,
            'entity_name': 'first_robot',
            'x': '0.0', 'y': '0.0', 'z': '0.0',
            'roll': '0.0', 'pitch': '0.0', 'yaw': '0.0'
        }.items()
    )

    return LaunchDescription([
        start_gazebo,
        spawn_robot
    ])

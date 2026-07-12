import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # 指定 URDF 文件绝对路径（按实际修改）
    urdf_file = os.path.expanduser('~/gazeborobot.urdf')
    
    # 启动 Gazebo 空世界（可换成其他世界）
    start_gazebo = ExecuteProcess(
        cmd=['gz', 'sim', '-r', 'empty.sdf'],
        output='screen'
    )

    # 使用 gz spawn 命令加载 URDF
    spawn_robot = ExecuteProcess(
        cmd=['gz', 'servicereq', '/world/default/create',
             '--timeout', '3000',
             '--req', f'{{"sdf": "{urdf_file}"}}'],
        output='screen'
    )
    # 或者使用 ros_gz_sim 自带的 spawn 节点：
    # spawn_robot = Node(
    #     package='ros_gz_sim',
    #     executable='spawn_entity.py',
    #     arguments=['-entity', 'first_robot', '-file', urdf_file],
    #     output='screen'
    # )

    return LaunchDescription([
        start_gazebo,
        spawn_robot
    ])

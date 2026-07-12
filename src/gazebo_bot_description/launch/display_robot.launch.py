import launch
import launch_ros
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # 获取功能包安装路径，拼接默认 URDF 文件路径
    urdf_tutorial_path = get_package_share_directory('gazebo_bot_description')
    default_model_path = urdf_tutorial_path + '/urdf/gazebo_robot.urdf'

    # 声明可修改的 model 参数
    action_declare_arg_mode_path = DeclareLaunchArgument(
        name='model',
        default_value=str(default_model_path),
        description='URDF 的绝对路径'
    )

    # 通过 cat 命令读取 URDF 文件内容
    robot_description = launch_ros.parameter_descriptions.ParameterValue(
        Command(['cat ', LaunchConfiguration('model')]),
        value_type=str
    )

    # robot_state_publisher 节点，发布 TF
    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )

    # joint_state_publisher 节点，发布关节状态（固定关节无变化，但必须有）
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
    )

    # RViz 可视化节点
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
    )

    return launch.LaunchDescription([
        action_declare_arg_mode_path,
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node
    ])

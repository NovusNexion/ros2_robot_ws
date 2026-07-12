cmake_minimum_required(VERSION 3.8)
project(gazebo_bot_description)

# 查找 ament_cmake 构建工具（必须）
find_package(ament_cmake REQUIRED)

# 安装 launch 和 urdf 目录到 share 空间
install(DIRECTORY launch urdf
    DESTINATION share/${PROJECT_NAME}
)

# 导出构建类型（必须）
ament_package()

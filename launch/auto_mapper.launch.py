from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Declare the launch arguments
    map_path_arg = DeclareLaunchArgument(
        "map_path",
        default_value='/Humble/maps',
        description="Map file path",
    )

    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true'
    )

    map_topic_arg = DeclareLaunchArgument(
        'map_topic',
        default_value='/projected_map',
        description='Topic for the map that auto_mapper will subscribe to.'
    )

    pose_topic_arg = DeclareLaunchArgument(
        'pose_topic',
        default_value='/dlio/odom_node/pose',
        description='Topic for the robot pose that auto_mapper will subscribe to.'
    )

    # Get the launch configurations
    map_path = LaunchConfiguration("map_path")
    use_sim_time = LaunchConfiguration('use_sim_time')
    map_topic = LaunchConfiguration('map_topic')
    pose_topic = LaunchConfiguration('pose_topic')

    auto_mapper_node = Node(
        package="auto_mapper",
        executable="auto_mapper",
        name="auto_mapper",
        parameters=[
            {"map_path": map_path},
            {'use_sim_time': use_sim_time},
            {'map_topic': map_topic},
            {'pose_topic': pose_topic}
        ],
        output="screen"
    )

    return LaunchDescription([
        map_path_arg,
        use_sim_time_arg,
        map_topic_arg,
        pose_topic_arg,
        auto_mapper_node
    ])

import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # Get the package path
    pkg_share = get_package_share_directory(
        'mct342_robot_description'
    )

    # Path to the URDF file
    urdf_file = os.path.join(
        pkg_share,
        'urdf',
        'robot_arm_urdf.urdf'
    )

    # Read the URDF file
    with open(urdf_file, 'r') as file:
        robot_description = file.read()

    return LaunchDescription([

        # Publish the robot description and transforms
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{
                'robot_description': robot_description
            }]
        ),

        # Publish joint states
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),

        # Display the robot in RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2'
        ),
    ])

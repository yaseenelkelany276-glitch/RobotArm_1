from launch import LaunchDescription

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os





def generate_launch_description():

    package_dir = get_package_share_directory('Lab_3')

    urdf_file = os.path.join(

        package_dir, 'urdf', 'robot_arm_urdf.urdf'

    )



    return LaunchDescription([

        Node(

            package='robot_state_publisher',

            executable='robot_state_publisher',

            arguments=[urdf_file],

            output='screen'

        ),



        Node(

            package='joint_state_publisher_gui',

            executable='joint_state_publisher_gui',

            output='screen'

        ),



        Node(

            package='rviz2',

            executable='rviz2',

            output='screen'

        )

    ])

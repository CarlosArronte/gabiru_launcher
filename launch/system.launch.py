from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gabiru_best_path',
            executable='best_path_node',
            name='best_path_node',
            output='screen'
        ),
        Node(
            package='gabiru_track',
            executable='segmentation_node',
            name='segmentation_node',
            output='screen'
        ),
        Node(
            package='gabiru_optimizer',
            executable='pso_optimizer_node',
            name='pso_optimizer_node',
            output='screen'
        )
    ])
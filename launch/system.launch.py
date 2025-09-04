from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Ruta para configuración de RViz (opcional, crea este archivo si lo necesitas)
    rviz_config_path = os.path.join(
        get_package_share_directory('gabiru_control'), 'rviz', 'turtlebot_config.rviz'
    )

    return LaunchDescription([
        # Lanzar Gazebo con TurtleBot3
        ExecuteProcess(
            cmd=['ros2', 'launch', 'turtlebot3_gazebo', 'turtlebot3_world.launch.py'],
            output='screen',
            env={'TURTLEBOT3_MODEL': 'burger'}  # Cambia a 'waffle' si usas Waffle
        ),
        # Lanzar RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path] if os.path.exists(rviz_config_path) else []
        ),
        # Nodo BestPath
        Node(
            package='gabiru_best_path',
            executable='best_path_node',
            name='best_path_node',
            output='screen'
        ),
        # Nodo Segmentation
        Node(
            package='gabiru_track',
            executable='segmentation_node',
            name='segmentation_node',
            output='screen'
        ),
        # Nodo PSO Optimizer
        Node(
            package='gabiru_optimizer',
            executable='pso_optimizer_node',  # Corregido de 'pso_node'
            name='pso_optimizer_node',
            output='screen'
        ),
        # Nodo Pure Pursuit
        Node(
            package='gabiru_control',
            executable='pure_pursuit_node',
            name='pure_pursuit_node',
            output='screen',
            parameters=[
                {'wheelbase': 0.16}  # TurtleBot3 Burger (0.33 para Waffle)
            ]
        )
    ])
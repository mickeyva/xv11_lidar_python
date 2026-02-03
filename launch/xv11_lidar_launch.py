#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    port = LaunchConfiguration('port', default='/dev/ttyACM0')
    frame_id = LaunchConfiguration('frame_id', default='laser')
    
    return LaunchDescription([

        
        DeclareLaunchArgument(
            'port',
            default_value=port,
            description='Specifying usb port to connected lidar'),
        
        DeclareLaunchArgument(
            'frame_id',
            default_value=frame_id,
            description='Specifying frame_id of lidar'),

        Node(
            package='xv11_lidar_python',
            executable='xv11_lidar',
            name='xv11_lidar',
            parameters=[{'port': port,
                         'frame_id': frame_id}],
            output='screen'),
    ])

<launch>
  <node name="xv11_lidar"          pkg="xv11_lidar_python"  type="xv11_lidar" output="screen">
  <param name="serial_port"         type="string" value="/dev/ttyACM0"/>
  <param name="serial_baudrate"     type="int"    value="115200"/>
  <param name="frame_id"            type="string" value="laser"/>
  </node>
</launch>

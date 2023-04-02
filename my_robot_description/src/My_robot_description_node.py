#!/usr/bin/env python
import rospy
import time
import signal
import std_msgs
import tf2_msgs
# from sensor_msgs_msg import tf2_sensor_msgs
# from nav_msgs.msg import Odometry
from geometry_msgs import Quaternion
from sensor_msgs_msg import JointState
from sensor_msgs_msg import robot_joint_state
from tf import TransformBroadcaster


pub_tf_broadcast = rospy.Publisher('/robot/JointState', JointState, queue_size=10)

# string[] name         JointState
# float64[] position
# float64[] velocity
# float64[] effort
#geometry_msgs/TransformStamped[] transforms
 #nome do pub (tem de ser igual)(topic  ,                           variavel , queue size)              )
 #distance = *string child dummy <-> outras especies
  
def cbTransformar(msg):
  Juntas = JointState()
  pub_tf_broadcast.publish(JointState)

def main():
  tf2_msgs/TFMessage
#   geometry_msgs/TransformStamped[]
#   std_msgs/Header header
# string child_frame_id
# geometry_msgs/Transform transform

  rospy.init_node('tf', anonymous=True)
  #rospy.Subscriber('pasta/topico' , modulo,  callback)
  rospy.Subscriber('/tf_joint_broadcast', TFMessage, cbTransformar)
  b = TransformBroadcaster()
    
translation = (0.0, 0.0, 0.0)
rotation = (0.0, 0.0, 0.0, 1.0)
rate = rospy.Rate(5)  # 5hz
    
x, y = 0.0, 0.0
  
while not rospy.is_shutdown():
  if x >= 2:
      x, y = 0.0, 0.0 
  
  x += 0.1
  y += 0.1
  
  translation = (x, y, 0.0)
  
  #                                                   MODELO vs   WORLD
  b.sendTransform(translation, rotation, Time.now(), 'my_robot', '/my_robot.world')
  rate.sleep() 
  
  if __name__ == '__main__':
      
    rospy.spin()

#  void My_robot_description::run(){
    
# #     ros::Rate go(100);

# #     while (ros::ok()){
# #         tf::TransformBroadcaster broadcaster;    
# #         broadcaster.sendTransform( // isto ta mal, preciso de saber a posicao deles a toda a hora -
# #                                 tf::StampedTransform(       // q1 q2 q3 q4
# #                                 tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0.1, 0.0, 0.2)),
# #                                 ros::Time::now(),"base_link", "base"));    
# #         ros::spinOnce();
# #         go.sleep();
# #     }

# if __name__ == '__main__':
#     main()

# # My_robot_description::My_robot_description():n("~") {
# #     std::string ns = ros::this_node::getNamespace();

# #     // Subscribers
# #     subJointState           = n.subscribe(ns + "/robot_joint_state", 10, &My_robot_description::cbPosicaoJunta, this);

# #     // Service Clients
# #     // srvClientArming    = n.serviceClient < mavros_msgs::CommandBool > (ns + "/mavros/cmd/arming");

# #     // Publishers  ja tenho o robot state publisher e robot joint state
# #     // pubMoveVel          = n.advertise < geometry_msgs::TwistStamped > (ns + "/mavros/setpoint_velocity/cmd_vel", 10);

# #     // Variables

# #     // Parameters
# #     // n.param<double>("paramTakeOffAltitude",  paramTakeOffAltitude, 10.0);

# #     ros_utils::ROS_PRINT(ros_utils::WHITE_BOLD, "MY ROBOT READY");
# # }


# # void My_robot_description::run(){
    
# #     ros::Rate go(100);

# #     while (ros::ok()){
# #         tf::TransformBroadcaster broadcaster;    
# #         broadcaster.sendTransform( // isto ta mal, preciso de saber a posicao deles a toda a hora -
# #                                 tf::StampedTransform(       // q1 q2 q3 q4
# #                                 tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0.1, 0.0, 0.2)),
# #                                 ros::Time::now(),"base_link", "base"));    
# #         ros::spinOnce();
# #         go.sleep();
# #     }


# # }


# # /*
# # funcao
# # void My_robot_description::changeToGuidedMode(){
# #     mavros_msgs::SetMode heifuSetMode;
# #     heifuSetMode.request.base_mode   = 0;
# #     heifuSetMode.request.custom_mode = "GUIDED";

# #     if (srvClientSetMode.call(heifuSetMode) && heifuSetMode.response.mode_sent)
# #         ROS_INFO("GUIDED enabled");
# #     else
# #         ROS_ERROR("Failed to set GUIDED");
# # }
# # */
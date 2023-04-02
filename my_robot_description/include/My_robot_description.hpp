#ifndef MY_ROBOT_DESCRIPTION_HPP
#define MY_ROBOT_DESCRIPTION_HPP

#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <ros_utils/Console.h>
#include <my_robot_description/My_robot_description.hpp>

namespace MR
{
    class My_robot_description
    {
    public:

        My_robot_description ();
        virtual ~My_robot_description (){};

        void run();

    private:
        ros::NodeHandle n;

        // Subscribers
        // ros::Subscriber subXBoxTakeOff;


        // Services Clients
        // ros::ServiceClient srvClientArming;

        // Publishers
        // ros::Publisher pubMoveVel;

        // TF relation
        // tf::TransformListener tfListener;

        // Parameters
        // double paramTakeOffAltitude;     

        // Variables

        // Functions
        // void cbTakeOff(const std_msgs::EmptyConstPtr& msg);
    };

}

#endif

Hello there!
This is a pretty old project from my part, where I had to develop a robotic arm in a simulator called Gazebo, which is used for planning and simulating the behavior of our vehicles!

All the plugins and configurations can be found in a file in the Unified Robotic Description Format (URDF), which is an XML file used by Robot Operating System to describe all the elements of the robot. 
It then gets translated into a Simulation Descriptive Format (SDF) mostly for the Gazebo simulation environment.
 

In it's totality, this file contains the folowing elements:
•	<robot> - root element;
    o	<link> - defines a link within it's own frame;
    o	<joint> - Obligatory definition of a junction;
    o	<transmission> Enables the movement of motors and joints;
    o	<gazebo> - Simulation extensions.


In this directory there are 2 different files, these being:
1 - "my_robot" which contains only the launch file that I use to spawn the simulator environment and also the robot itself! It basically does it all.
2 - "my_robot_description" which contains all the information regarding the robotic arm. This being all the configuration files for each segment of the arm

In all honesty I am in need to remind myself how to summon this robot in a windows environment.
But being plain and simple, you only need to have access to the Gazebo Simulator and all that needs to be done is to call the launch file inside of "my_robot".

It was mostly an academic project that was pretty much left in the dust, and with it my dreams of working with robotic arms :( 

Anyways if you're curious about this project you can contact me, no charges!

Hoped you enjoyed looking through my files, and have a nice day!

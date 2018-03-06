
# [JdeRobot - Universidad Rey Juan Carlos](http://jderobot.org)

[Back to catalogue](../README.md#jderobot-universidad-rey-juan-carlos)

JdeRobot is a software development framework for robotics and computer
vision applications. These domains include sensors, actuators, and intelligent software in between. It has been designed to help in programming such intelligent
software. It is written in C++, Python and JavaScript, and provides a distributed component-based programming environment where the robotic application is made up of a collection of several concurrent asynchronous components. Each component may run in different computers and they are connected using ICE
communication middleware or ROS. JdeRobot is based on ROS and uses ROS drivers.

Real robots like TurtleBot, drones (ArDrone, 3DR solo) and real sensors like color cameras, RGBD cameras (Kinect1, Kinect2, Xtion), RPLidar, laser are supported. And their corresponding ones in Gazebo simulator, including also a Formula1 and autonomous cars.

Getting sensor measurements is as simple as calling a local function, and ordering motor commands as easy as calling another local function. The platform attaches those calls to the remote invocation on the components connected to the sensor
or the actuator devices. Those local functions build the Hardware Abstraction Layer API. The robotic application gets the sensor readings and orders the actuator commands using such HAL to unfold its behavior.

JdeRobot include many tools: (a) JdeRobot-Academy, a suite for teaching robotics and computer vision, with 20 motivating exercises; (b) VisualStates, for visual creation of automata that control robot behavior; (c) Scratch2JdeRobot, for programming advanced robots with a full visual language; (d) robot teleoperators, even with web technologies; (e) a tuner for color filters, etc.

# Application Instructions

* Twitter: We welcome students to contact relevant mentors before submitting their application into GSoC official website.

Requirements:
- Git experience
- C++ and Python programming experience (depending on the project)

Programming tests
The JdeRobot organization will prepare three small coding tests (standalone exercise or bug fix) before accepting any candidate proposal.

Send us your CV
Through email, to jmplaza AT gsyc.es AND franciscomiguel.rivas AT urjc.es AND almartinflorido AT gmail.com AND edupergar AT gmail.com

Template
After doing the programming test, just send us this template with the requested information.
1. Contact details
Name and surname:
Country:
Email:
Public repository/ies:
Personal blog (optional):
Twitter/Identica/LinkedIn/others:

2. Your idea
Title
Brief description of the idea
The state of the software BEFORE your GSoC.
The addition that your project will bring to the software.

3. Timeline
Now split your project idea in smaller tasks. Quantify the time you think each task needs. Finally, draw a tentative project plan (timeline) including the dates covering all period of GSoC.

4. Studies
What is your School and degree?
Would your application contribute to your ongoing studies/degree? If so, how?
# Turtlesim Numbers

First clone the catkin_ws into your working directory

```Shell
mkdir wkdir
cd wrkdir
git clone https://github.com/ShivamMalhotra1994/turtlesim_numbers.git
```
Now source the setup.bash for every terminal
```Shell
cd catkin_ws
source devel/setup.bash
```
Now finally run each of the nodes in different terminal. Remember to source the setup
```Shell
roscore
rosrun turtlesim turtlesim_node
rosrun turtlesim_numbers numbers_server.py
rosrun turtlesim_numbers numbers_client.py
```
Rerun the turtlesim node to print a new number each time.

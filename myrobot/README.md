# Create a build directory and compile the plugin
```
$ mkdir build
$ cd build
$ cmake ..
$ make # You might get errors if your system is not up to date!
$ export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:/home/path/to/build
```

# Open your world file and attach the plugin to it
```
$ cd /home/workspace/myrobot/world/
$ code myworld.world
```
Copy below code 
```
<plugin name="hello" filename="libhello.so"/>
```

Paste under 
```
<world name="default">
```

# Launch the world file in Gazebo to load both the world and the plugin
```
$ cd /home/workspace/myrobot/world/
$ gazebo myworld --verbose
```
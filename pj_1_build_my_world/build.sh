if [ -d "build" ]; then
    rm -rf build
fi
mkdir build
cd build
cmake ..
make
if [[ ":$GAZEBO_PLUGIN_PATH:" != *":$(pwd):"* ]]; then
    export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:$(pwd)
fi
cd ..
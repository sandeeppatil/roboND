# Useful Commands
## Gazebo Harmonic
| Command | Description |
| ------- | ----------- |
| `gz sim` | Open Gazebo simulator |
| `killall gzserver` | If the Gazebo is stuck and not opening |
---------------
- To Add existing Gazebo Models from local dir: [src](https://gazebosim.org/docs/latest/fuel_insert/)
```
-- Add your model directory as a resource with export GZ_SIM_RESOURCE_PATH=~/my-local-models/
-- Open the Gazebo Simulator and add the Resource Spawner Plugin, the model should now show up under your local resources.
```

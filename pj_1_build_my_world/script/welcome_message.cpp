#include <gazebo/gazebo.hh>

namespace gazebo
{
    // Create a class that inherits from WorldPlugin
    class WelcomeMessage: public WorldPlugin
    {
        // Constructor to initialize the plugin
        public: WelcomeMessage() : WorldPlugin()
        {
            printf("Welcome to the world of Gazebo!\n");
        }

        // Load function is called by Gazebo when the plugin is inserted into simulation
        public: void Load(physics::WorldPtr _world, sdf::ElementPtr _sdf)
        {
        }
    };
    // Register this plugin with the simulator
    GZ_REGISTER_WORLD_PLUGIN(WelcomeMessage)
} // namespace gazebo
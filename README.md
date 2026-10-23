Joints
1 Base joint
2 Shoulder joint
3 Shoulder twist joint
4 Elbow joint
5 Arm Twist Joint
6 Wrist joint
7 Grip joint

DH Parameters of Armeo Power:
joint a          d          alpha      offset
1     -0.0000,   0.0000,     1.5708,   -0.0000
2      0.0000,   0.0000,    -1.5708,    3.1416
3     -0.0000,   0.2490,     1.5708,   -0.0000
4     -0.0000,  -0.0000,    -1.5708,   -0.0000
5      0.0000,   0.2520,     1.5708,    0.0000
6      0.0840,  -0.0000,     0.0000,    1.5708

Note that:
- Joint 6 alpha was unable to be determined due to the model not giving end effector rotation, and as such has been locked to 0.0
- Joint 7 (grip joint) does not contribute to end effector
- These were generated using a least squares optimizer using the joint angles, end effector position and jacobian as inputs. (see armeo_examples/tools/dh_estimator.py)
- These dh parameters result in a euclidean distance error of: `avg: 5.37e-06, min: 2.15e-06, max: 5.04e-04` Tested on the samples in `data/dh_param_est_error_improved.csv`

## Related Repositories

| Repository | Description |
|------------|-------------|
| [xpctarget_api_cpp](https://github.com/nathant127/xpctarget_api_cpp) | C++ library (derived from MathWorks' `xpcapi`) used by both the examples and the ROS driver to communicate with the ARMEO Power robot |
| [armeo_ros_driver](https://github.com/nathant127/armeo_ros_driver) | ROS 2 driver for the ARMEO Power robot |
| [armeo_msgs](https://github.com/nathant127/armeo_msgs) | A set of msgs for the armeo ros driver |
| [armeo_examples](https://github.com/nathant127/armeo_examples) | A simple set of examples for controlling the ARMEO Power robot |
| [armeo_re](https://github.com/ashquarky/armeo-re) | Repository that this project is based on, documentation |
| [armeo_xpc](https://github.com/ashquarky/armeo_xpc) | Repository that this project is based on, retrieves signals from the armeo power using ros2 on windows |

### Testing / Legacy

| Repository | Description |
|------------|-------------|
| [armeo_xpc_wine](https://github.com/nathant127/armeo_xpc_wine) | Old repository used for initial testing and development, running MathWorks' `xpcapi` library under Wine |

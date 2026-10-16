Joints:
Base joint
Shoulder joint
Shoulder twist joint
Elbow joint
Arm Twist Joint
Wrist joint
Grip joint

DH Parameters of Armeo Power:
joint a          d          alpha      offset
1    -0.0000    -0.0001     1.5703    -0.0016
2    -0.0008    -0.0027     1.5677     0.0018
3    -0.0004     0.2522     1.5634    -3.1419
4     0.0003     0.0011    -1.5665    -0.0007
5    -0.0000     0.2487     1.5641     0.0041
6     0.0604    -0.1167     3.6046     2.3425
7    -0.0001    -0.1311     4.1266     0.5968

After plugging these dh parameters back in, fkine was performed and the resultant end effector position was compared to the real position
The error was: avg: 0.0012018069427291887, min: 1.91432e-05, max: 0.00445708

## Related Repositories

| Repository | Description |
|------------|-------------|
| [xpctarget_api_cpp](https://github.com/nathant127/xpctarget_api_cpp) | C++ library (derived from MathWorks' `xpcapi`) used by both the examples and the ROS driver to communicate with the ARMEO Power robot |
| [armeo_ros_driver](https://github.com/nathant127/armeo_ros_driver) | ROS 2 driver for the ARMEO Power robot |
| [armeo_examples](https://github.com/nathant127/armeo_examples) | A simple set of examples for controlling the ARMEO Power robot |

### Testing / Legacy

| Repository | Description |
|------------|-------------|
| [armeo_xpc_wine](https://github.com/nathant127/armeo_xpc_wine) | Old repository used for initial testing and development, running MathWorks' `xpcapi` library under Wine |

# Operation Mode: Mobilization

Mobilization mode is a control mode that allows the user to input a set of targets for each joint individually, which will then be executed by the model without any continuous input required. The control system will continuously loop through the given targets until told to stop. During this mode, the robot joint are rigid and will not move when force is applied to them.

The system seems to generate its own trajectories using a method similar to jtraj from Peter Corke's Robotics Toolbox, each movement starts out slow, speeds up and then slows down.

## Important parameters

| Parameter name | Parameter Dimensions | Parameter Description |
|----------------|----------------------|-----------------------|
|Input/OperationMode/Mobilization/FixedTrajectory/Joint<1-7>/Target<1-20> | [1,2] | Allows setting a numbered target joint angle (rad), and a time duration for the movement to take (seconds) 20 targets for each joint |
|Input/OperationMode/Mobilization/FixedTrajectory/Joint<1-7>/NumOfTargets | [1,1] | Allows setting the number of targets for the mode to use |
|Input/OperationMode/Mobilization/Record | [1,1] | Unknown purpose, likely allows recording robot movements as a set of targets |
|Input/OperationMode/Mobilization/Replay | [1,1] | Starts / Stops the execution of the targets, 0 -> Stop 1 -> Start |
|Input/OperationMode/Mobilization/ReplaySpeed | [1,1] | A global speed modifier for execution, 1.0 means to run at normal speed, 0.5 would make targets run at half speed, 2.0 means double speed |

## Description

Mobilization mode provides a set of 20 target parameters and a parameter to set the number of targets for each joint. This means that each joint can recieve a different number of targets, and the duration for each target and joint can be different.

Once the target parameters are set, the replay speed can be set to determine a global speed modifier for all targets, and then finally when ready the replay parameter is used to start and stop the movement

Some small example psudeo code is shown below:

```cpp
// Ensure replay is off before entering mobilization mode
setParam(Replay, 0.0);
// Change to mobilization mode
setParam(OperationMode, 2);
// Set the targets to move joint 1 between joint angle 0.5 -> 1.2 with a 1 Second duration for each movement
setParam(Joint1/Target1, [0.5, 1.0])
setParam(Joint1/Target1, [1.2, 1.0])
setParam(Joint1/NumOfTargets, 2)

// Set replay speed to normal time scale
setParam(ReplaySpeed, 1.0);
// Start movements
setParam(Replay, 1.0);

// Do anything else you want
while (some_cond) {

}

// Stop Movements
setParam(Replay, 0.0);
```

A working C++ example can be found in armeo_examples:
[Working C++ Example](https://github.com/nathant127/armeo_examples/blob/main/src/test_traj.cpp)




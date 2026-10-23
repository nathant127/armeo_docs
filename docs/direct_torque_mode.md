# Operation Mode: Direct Torque

Direct Torque mode is a mode that allows joint space torque control, in other words it allows you to directly send torques to the motors. This makes direct torque mode one of the most useful modes, in addition during direct torque mode the joints of the Armeo have much lower resistance, allowing them to be easily moved by a user.

## Important parameters

| Parameter name | Parameter Dimensions | Parameter Description |
|----------------|----------------------|-----------------------|
|Input/OperationMode/DirectTorqueMode/Torque<1-7> | [1,1] | Allows setting a torque for each joint |

## Description

Directo Torque mode allows you to set the torque applied to each joint, which will then be continuously set to the motor

Some small example psudeo code is shown below:

```cpp
// Change to direct torque mode
setParam(OperationMode, 10);

// Applies a constant torque of 3 Nm to joint 1 and 4 Nm to joint 2
setParam(Torque1, 3);
setParam(Torque2, 4);

sleep(2000);
// Applies a constant torque of 1.5 Nm to joint 1 and 1 Nm to joint 2
setParam(Torque1, 1.5);
setParam(Torque2, 1);

sleep(2000);

// Sets torque back to 0
setParam(Torque1, 0);
setParam(Torque2, 0);

```

A working C++ example can be found in armeo_examples:
[Working C++ Example](https://github.com/nathant127/armeo_examples/blob/main/src/teleop.cpp)
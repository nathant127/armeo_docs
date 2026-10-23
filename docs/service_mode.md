# Operation Mode: Service Mode

Service mode was not fully explored, but it provides a number of modes that make the Armeo perform hardcoded movements at a constant velocity, these were not very useful but are documented here anyway.

## Important parameters

| Parameter name | Parameter Dimensions | Parameter Description |
|----------------|----------------------|-----------------------|
|Input/OperationMode/ServiceMode/DesiredDq | [1,1] | Likely sets some kind of constant velocity for some of the modes |
|Input/OperationMode/ServiceMode/DesiredTorque | [1,1] | Likely sets some kind of torque for some of the modes |
|Input/OperationMode/ServiceMode/ServiceOption | [1,1] | The type of movement to perform (allows values 0-7) |
|Input/OperationMode/ServiceMode/TestJoint | [1,1] | Only used for some modes, allows changing what joint the movement is performed on |

## Description

This mode was not fully explored, but each option was breifly tested and the results of that test are in the table below:

| Service Option | Movement Performed | Test Joint Param Works |
|----------------|--------------------|------------------------|
| 0 | Nothing | No |
| 1 | Runs joint back and forth between its limits a couple times | Yes |
| 2 | Runs joint back and forth between its limits a couple times | Yes |
| 3 | Runs joint back and forth between its limits a couple times | Yes |
| 4 | Moves joint in the positive direction at a constant velocity | Yes |
| 5 | Nothing | No |
| 6 | Moved Shouler joint up then down a couple times | No |
| 7 | Moves joint back and forth slightly from a standard neutral position | Yes |

Some small example psudeo code is shown below:

```cpp
// Change to service mode
setParam(OperationMode, 5);
// Should move base joint towards the positive direction at a constant velocity
setParam(ServiceOption, 4);
setparam(TestJoint, 1);

```

A working C++ example can be found in armeo_examples:
[Working C++ Example](https://github.com/nathant127/armeo_examples/blob/main/src/vel_control.cpp)



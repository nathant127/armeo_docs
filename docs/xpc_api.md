# xPC API Introduction

xPC Target is a legacy system developed by MathWorks for MATLAB Simulink. It allows simulink models to be loaded onto a special computer referred to as the Target PC. This PC runs a special real time kernel and can be communicated with using xPC API over a local network interface (typically ethernet) using a tcp socket.

It has its own packet structure and protocol, if you are looking for information on that see [xPC Protocol](/docs/xpc_protocol.md).

The focus of this doc is to give a brief explanation of the API such that you can use it to control the Armeo Power. For more information on the xPC API, you can read MathWorks offical documentation.

## Initialization and Shutdown

You must first initialize a connection with the Target PC, and load the model (.dlm file) you want it to run. Some example code is below:

```cpp
// Open a tcp connection
int port = xPCOpenTcpIpPort("10.10.10.11", "22222");

char name[100];
// If an app is already running or loaded, stop it and unload it
xPCGetAppName(port, name);
if (strcmp("loader", name) != 0) {
    if (xPCIsAppRunning(port)) {
        xPCStopApp(port);
    }
    xPCUnloadApp(port);
}

// Load the app we want to run
xPCLoadApp(port, path, target_model);
// Start the app
xPCStartApp(port);

{
    // Do some work
}

// Stop and unload app when done
xPCStopApp(port);
xPCUnloadApp(port);
// Close the connection (Optional if program will terminate)
xPCCloseConnection(port);
```

Some important aspects of this code to point out

- The "port" that xPCOpenTcpIpPort returns is just used to allow you to connect to multiple Target PC's
- When no app is loaded the current app is "loader"
- If an app is already loaded, you must make sure to unload it first before loading a new one.
- The "path" must be the path to the folder that contains the model you want to load, and target_model is the filename of the model to load.
- xPCLoadApp reads a file on your machine, so ensure that the path corresponds to an actual .dlm file

## Communication

From this point, the app is loaded and running and you can communicate with the app via the model's exposed signals and parameters.

- Signals can only be read from and are typically used to store things like state
- Parameters can be read from and written to and are typically used to control the model, they may provide a way to fine tune the model, provide ways to switch operation modes and more.
- Unlike signals, Parameters also have dimensions and so can store multiple values

To interact with signals and parameters, see the below example code:

### Signals
```c
// Requests the id that corresponds with the given signal name
int joint_angle_id = xPCGetSignalIdx(port, "Output/SoftwareSignals/JointAngle/s1");
// Requests the current value of the signal with the given id
double joint_angle = xPCGetSignal(port, joint_angle_id);

// Get a different signal id
int joint_angle_id_2 = xPCGetSignalIdx(port, "Output/SoftwareSignals/JointAngle/s2");
// Make an arary of signal ids
int sig_ids[] = {joint_angle_id, joint_angle_id_2};
// Make an array of signal values
double joint_angles[2];
// Request multiple signals with one packet (less network traffic)
xPCGetSignals(port, 2, sig_ids, joint_angles);

// Signal Id's do not change and so can be hardcoded:
double sig_val = xPCGetSignal(port, 1349);
```

### Parameters
```c
// Requests the id that corresponds with the given signal name
int om_id = xPCGetParamIdx(port, "Input/OperationMode/OperationMode", "Value");


// Retreive the dimensions of the parameter
int dims_size = xPCGetParamDimsSize(port, om_id);
int* dims = (int*) malloc(dims_size * sizeof(int));
xPCGetParamDims(port, om_id, dims);

// From the dimensions, figure out how large of an array needs to be provided
int param_size = 1;
for (int i = 0; i < dims_size; i++) {
    param_size = dims[i] * param_size;
}

free(dims);

// Creates an array with the appropriate size for the parameter
double* om_value = (double*)malloc(param_size * sizeof(double));

// Requests the current value of the parameter with the given id
xPCGetParam(port, om_id, om_value);


{
    // Do some work that sets om_value
}


// Sets the given parameter to the given value
xPCSetParam(port, om_id, om_value);

free(om_value);
```

Note: 

- Parameter Ids and Dimensions do not change, so you may assume these to simplify your code.
- If the array you provide is too small, you will trigger a out of bounds read/write and cause an error

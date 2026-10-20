# Armeo Docs

## Intro

## Further Info

| Document | Description |
|----------|-------------|
|[Armeo Power Info](/docs/armeo_power_info.md) | General information about the armeo power including dh parameters, joints, joint limits (Start here if new) |
|[xPC API Intro](/docs/xpc_api.md) | Introduction to how to use xpcapi to communicate with an xPC Target PC |
|[xPC Target Protocol](/docs/xpc_protocol.md) | Information about the xpcapi network protocol used to communicate with the xPC Target PC that controls the Armeo |
|[Armeo Control](/docs/armeo_control.md) | Information on how to control the Armeo Power using xPC API |
|[Armeo Ros Driver](/docs/armeo_ros_driver.md) | Information on how to use the Armeo Ros driver |
|[Armeo Signals](/data/armeo_signals.csv) | Full list of all signals in the Armeo Power Model |
|[Armeo Parameters](/data/armeo_parameters.csv) | Full list of all parameters in the Armeo Power Model |

## Design Decisions and Process

|Document | Description |
|---------|-------------|
|



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

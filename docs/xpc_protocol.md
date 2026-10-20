# xPC Target Protocol

xPC Target uses a simple system to establish communication between the client and the Target PC. It uses two way tcp communication where the client sends a request and then the target pc reads the request and sends the appropriate response. Note that only one message can be sent at a time, the Target PC will never send a request to the client.

It uses a normal socket tcp connection, the protocol is not very complex.

## Requests
A request is always sent by the client, to the Target PC. It is a singular tcp packet following the packet format layed out in the next section.

## Responses
A response is always sent by the target pc to the client, in response to a request. It is also a singular tcp packet using the same format as the requests.

## Packet Format
A packet is made up of a header and the payload, the header is 8 bytes, the payload contents and length depends on the contents of the header.
The only difference between a request packet and a response packet is who sends them, the contents of the payload and the size of the payload.

The packet structure is as follows:

| Byte No | Entry Name | Purpose |
|---------|------------|---------|
| 0-1     | Magic Number [0x4E, 0xCB] | This entry is always the same value for every xpc packet, it is used to differentiate between xpc packets and other packets |
| 2-3     | Command    | The purpose of the packet, determines what information is in the payload and what the Target PC should do in response |
| 4-7     | Payload Size | The size of the payload in bytes |
| 8+      | Payload | Contents determined by the command, can be empty |

To make it clearer, an example command is "SIG_GET" [0x28, 0x0A], this command should be sent with a payload that contains an array of unsigned 32 bit integers, each one representing a signal ID that target PC should send the value of in response. The Target PC then sends a response back that uses the same command, but the payload is then an array of 64 bit floats each the signal value corresponding to the sent signal ID.

There are a large amount of commands all with a different purpose, typically each xPC API function will correspond to a unique command packet, and so you can easily reverse engineer the payload format by sending a packet using the API and decoding it with wireshark or other similar programs.

For this exact purpose, I have made a wireshark plugin as part of the xpctarget_api_cpp project, which includes all the command formats that I have figured out, there are still a number of missing packets, but the ones in there cover well beyond what is needed for the Armeo so I stopped. [Wireshark Plugin](https://github.com/nathant127/xpctarget_api_cpp/blob/master/wireshark/xpc.lua)

In addition to this, when a payload includes an array, there will always be a 32 bit signed integer before the array that corresponds to the number of elements in the array

## Example
If you want to see an implementation of this protocol to wrap your head around how it works, have a look at the reimplementation of xPC API. It provides a full backend for sending/recieving xPC Target Messages, as well as implementations of a subset of the original functions.

[xpctarget_api_cpp](https://github.com/nathant127/xpctarget_api_cpp)

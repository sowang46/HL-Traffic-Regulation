#!/bin/bash

sudo modprobe dummy
sudo ip link add tr0 type dummy
sudo ifconfig tr0 hw ether C8:D7:4A:4E:47:50
# sudo ip addr add 192.168.10.100/24 brd + dev tr0 label tr0:0
sudo ip link set dev tr0 up
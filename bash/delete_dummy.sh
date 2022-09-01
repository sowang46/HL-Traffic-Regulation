#!/bin/bash

# sudo ip addr del 192.168.10.100/24 brd + dev tr0 label tr0:0
sudo ip link delete tr0 type dummy
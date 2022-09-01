#!/bin/bash

if [ -z $1 ]; then
    export UL_IF="tr0"
else
    export UL_IF=$1
fi

sudo sysctl net.ipv4.ip_forward=1
# sudo iptables -t nat -A POSTROUTING -o $UL_IF -j MASQUERADE
sudo iptables -A FORWARD -i enp0s1 -o $UL_IF -j ACCEPT
sudo iptables -A FORWARD -i $UL_IF -o enp0s1 -m state --state RELATED,ESTABLISHED -j ACCEPT
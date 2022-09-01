#!/bin/bash

if [ -z $1 ]; then
	export CLIENT_IP=192.168.60.163
else
	export CLIENT_IP=$1
fi

sudo route add -host $CLIENT_IP dev tr0

#!/bin/bash

echo "======sysytem info======"
echo "hostname: $(hostname)"
echo "username: $(whoami)"
echo "runtime: $(uptime -p)"
echo

echo "=====menemory====="
free -h
echo

echo "======DISK======="
df -h

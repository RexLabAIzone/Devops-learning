#!/bin/bash
FILE="/etc/passwd"
if [ -f $FILE ];then
	echo "file exist"
else
	echo "file null"
fi

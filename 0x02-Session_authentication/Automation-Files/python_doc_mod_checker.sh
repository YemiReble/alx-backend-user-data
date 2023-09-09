#!/usr/bin/env bash
# This Bash script checks the Following
# Documentation
# Module
# Classes
# Function of any python file if available

file="$1"
funct="$2"

python3 -c 'print(__import__("'$file'").__doc__)'
echo "----------------------------------------------------------------"
python3 -c 'print(__import__("'$file'").'$funct'.__doc__)' 
echo "----------------------------------------------------------------"
#python3 -c 'print(__import__("'$file'").MyClass.my_function.__doc__)'
#echo "----------------------------------------------------------------"
#python -c 'print(__import__("'$file'").MyClass.__doc__)'

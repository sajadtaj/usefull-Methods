#!/bin/bash

# CPU Usage
echo "CPU Usage"
echo "---------"
top -bn1 | grep "Cpu(s)" | \
sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | \
awk '{print "CPU Usage: " 100 - $1"%"}'

# Memory Usage
echo ""
echo "Memory Usage"
echo "------------"
free -h

# Disk Usage
echo ""
echo "Disk Usage"
echo "----------"
df -h

# Network Usage
echo ""
echo "Network Usage"
echo "-------------"
ip -s link

# Processes Usage
echo ""
echo "Top Processes by CPU and Memory Usage"
echo "-------------------------------------"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 10

# End of script
echo ""
echo "Resource usage information retrieval complete!"


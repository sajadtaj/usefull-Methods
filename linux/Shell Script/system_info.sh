#!/bin/bash

# System Information
echo "System Information"
echo "------------------"
uname -a

# CPU Information
echo ""
echo "CPU Information"
echo "---------------"
lscpu

# Memory Information
echo ""
echo "Memory Information"
echo "------------------"
free -h

# Disk Information
echo ""
echo "Disk Information"
echo "----------------"
lsblk
df -h


# End of script
echo ""
echo "Information retrieval complete!"


#!/bin/bash
echo "Enabling bluetooth..."
rfkill unblock bluetooth
echo "Discoverable on..."
hciconfig hci0 piscan
echo "Enabling secure pairing mode..."
hciconfig hci0 sspmode 1
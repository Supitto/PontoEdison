#!/bin/bash

function enable {
	echo "Enabling bluetooth..."
	rfkill unblock bluetooth
	usleep 500000
	echo "Discoverable on..."
	hciconfig hci0 piscan
	echo "Enabling secure pairing mode..."
	hciconfig hci0 sspmode 1
}

function disable {
	echo "Disabling bluetooth..."
	rfkill block bluetooth
}

key="$1"
case $key in
	-e|--enable)
	enable
	shift # past argument
	;;
	-d|--disable)
	disable
	shift # past argument
	;;
	*)
	echo "parameter not specified"
	;;
esac
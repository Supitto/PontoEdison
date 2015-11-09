#!/usr/bin/env python 
# source: https://github.com/karulis/pybluez/blob/master/examples/simple/inquiry.py

import bluetooth
import logging

def nearby_devices(duration=5):
	logging.debug("performing inquiry...")

	nearby_devs = bluetooth.discover_devices(
		duration=duration, lookup_names=True, flush_cache=True, lookup_class=False)

	logging.debug("found %d devices" % len(nearby_devs))

	return nearby_devs

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)

	for addr, name in nearby_devices(6):
		try:
			print("  %s - %s" % (addr, name))
		except UnicodeEncodeError:
			print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))


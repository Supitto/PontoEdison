#!/bin/bash
sdptool add --channel=22 SP
rfcomm listen /dev/rfcomm0 22 &
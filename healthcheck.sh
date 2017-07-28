#!/bin/bash

if [ -z "$RCON_HEALTH_COMMAND" ]; then
	echo "Cannot check health: Please set RCON_HEALTH_COMMAND to a RCON command."
	exit 1
fi

python /home/steam/rcon/healthcheck.py
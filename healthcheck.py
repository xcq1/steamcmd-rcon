import sys
import os
import re
sys.path.append(os.path.abspath("/home/steam/rcon"))
import SourceRcon

challenge = os.environ.get('RCON_HEALTH_COMMAND')
check = os.environ.get('RCON_HEALTH_REGEXP')

rcon = SourceRcon.SourceRcon(os.environ.get('RCON_HOST'), int(os.environ.get('RCON_PORT')), os.environ.get('RCON_PASSWORD'))
response = rcon.rcon(challenge)
rcon.disconnect()

if len(check) > 0:
	p = re.compile(check)
	healthy = p.search(response) is not None
else:
	healthy = response is not None and len(response) > 0

if not healthy:
	print "Unhealthy response was '" + response + "'"

sys.exit(0 if healthy else 1)
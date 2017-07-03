import sys
import os
import re
import SourceRcon as rcon

challenge = os.environ.get('RCON_HEALTH_COMMAND')
check = os.environ.get('RCON_HEALTH_REGEXP')

rcon = SourceRcon.SourceRcon(os.environ.get('RCON_HOST'), os.environ.get('RCON_PORT'), os.environ.get('RCON_PASS'))
response = rcon.rcon(challenge)
rcon.disconnect()

if len(check) > 0:
	p = re.compile(check)
	healthy = p.search(response) is not None
else:
	healthy = response is not None and len(response) > 0

sys.exit(0 if healthy else 1)
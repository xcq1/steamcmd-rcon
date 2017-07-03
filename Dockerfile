FROM xcq1/steamcmd
LABEL maintainer="mail@tobiaskuhn.de"

ENV RCON_HOST "localhost"
ENV RCON_PORT "27015"
ENV RCON_PASSWORD ""
ENV RCON_HEALTH_COMMAND ""
ENV RCON_HEALTH_REGEXP ""

ADD SourceRcon.py /rcon/SourceRcon.py
ADD healthcheck.py /rcon/healthcheck.py
ADD healthcheck.sh /rcon/healthcheck.sh

HEALTHCHECK --interval=1m --retries=5 CMD /rcon/healthcheck.sh

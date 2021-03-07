import os

name = 'flask-dogstatsd'
statsd_host = f"{os.getenv('DD_AGENT_HOST', 'localhost')}:8125"
bind = '0.0.0.0:5000'

import os
from datadog import initialize, statsd

options = {
    'statsd_host':os.environ.get('DD_AGENT_HOST')
}

initialize(**options)

from flask import Flask

def create_app():
  app = Flask(__name__)

  @app.route('/')
  def hello_world():
    statsd.increment('hello.world', tags=["app:flask-hello-world"])
    return 'Hello, World!\n'
  
  return app

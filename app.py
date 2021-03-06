import os
import random

from datadog import initialize, statsd

options = {
    'statsd_host':os.environ.get('DD_AGENT_HOST')
}

initialize(**options)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    statsd.increment('hello.world', tags=["app:flask-hello-world"])
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

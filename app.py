import random

from datadog import initialize, statsd
options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    statsd.gauge('hello.world', random.randint(0, 9), tags=["app:flask-hello-world"])
    return 'Hello, World!'

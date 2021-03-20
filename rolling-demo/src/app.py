#!/usr/bin/env python

from flask import Flask
from flask_healthz import healthz


app = Flask(__name__)
app.config.from_pyfile('defaults.py', silent=True)
app.register_blueprint(healthz, url_prefix="/healthz")

@app.route('/')
def hello():
    app.logger.info("main route")
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
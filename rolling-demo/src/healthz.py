from flask_healthz import HealthError

import os
from time import sleep

def liveness():
    pass

def readiness():
    if not os.path.exists(os.getenv('READY_FILE', '/tmp/ready')):
        raise HealthError("Still waiting to be ready")
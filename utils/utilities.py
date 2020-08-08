import json
import os
from pathlib import Path

SECRETS = json.loads(Path("secrets.json").read_text())

def get_secret(key):
    return os.environ.get(key, SECRETS[key])

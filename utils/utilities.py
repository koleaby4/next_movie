import json
import os
from pathlib import Path
import re


FILE_SECRETS = json.loads(Path("secrets.json").read_text())


def get_secret(key):
    return os.environ.get(key, FILE_SECRETS[key])


def get_prostgres_auth_dict():

    database_url = get_secret("DATABASE_URL")

    postgres_pattern = re.compile(
        r"""
        postgres:\/\/       # postgres://   literal
        (?P<username>[^:]+) # username
        :                   # colon literal
        (?P<password>[^@]+) # pwd
        @                   # @ literal
        (?P<host>[^:]+)     # host
        :                   # colon literal
        (?P<port>\d+)     # port
        \/                  # / literal
        (?P<db_name>\w+)$   # db_name
        """,
        re.VERBOSE,
    )

    matches = re.match(postgres_pattern, database_url)
    return matches.groupdict()

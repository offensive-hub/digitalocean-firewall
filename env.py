"""
*********************************************************************************
*                                                                               *
* env.py -- Environment variables.                                              *
*                                                                               *
*********************************************************************************
"""

from os.path import dirname, join, isfile

# ------- Black-widow files ------- #
ROOT_PATH = dirname(__file__)
PRIVATE_ENV_FILE = join(ROOT_PATH, '.env')

# ----- Editable environments ----- #
DIGITALOCEAN_ACCESS_TOKEN = ''
DIGITALOCEAN_BASE_URL = ''

EDITABLE_ENV = (
    'DIGITALOCEAN_BASE_URL',
    'DIGITALOCEAN_ACCESS_TOKEN',
)

# ----------- Read .env ----------- #
if isfile(PRIVATE_ENV_FILE):
    with open(PRIVATE_ENV_FILE) as f:
        for e in f.readlines():
            env = e.strip()
            if len(env) < 3:
                continue
            if env[0] == '#':
                continue
            key, val = env.split('=', 1)[0:2]
            key = key.strip()
            val = val.strip()
            if len(key) == 0 or len(val) == 0:
                raise EnvironmentError("Wrong environment in .env file: " + env)
            if key not in EDITABLE_ENV:
                raise EnvironmentError("Non editable environment in .env file: " + env)
            if val[0] == "'" or val[0] == '"':
                i = 0
                val_ok = ''
                for char in val:
                    val_ok += val[i]
                    if i >= 1 and char == val[0]:
                        if val[i-1] != '\\':
                            break
                    i += 1
                val = val_ok
                if len(val) == 0:
                    raise EnvironmentError("Wrong environment in .env file: " + env)
            else:
                val = val.split('#')[0].strip()
            exec(key + ' = ' + str(val))

import subprocess
import sys

def dump(address):
    try:
        return subprocess.Popen(['pg_dump', address], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)

def dump_file_name(address, timestamp=None):
    db_name = address.split("/")[-1]
    db_name = db_name.split("?")[0]
    if timestamp:
        return f"{db_name}-{timestamp}.sql"
    else:
        return f"{db_name}.sql"

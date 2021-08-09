import pytest
import subprocess

from pgbackup import pgdump

address = "192.169.0.167/db_one"

def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with the database URL
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(address)
    subprocess.Popen.assert_called_with(['pg_dump', address], stdout=subprocess.PIPE)


def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump isn't installed.
    """
    mocker.patch('subprocess.Popen', side_effect=OSError('no such file'))
    with pytest.raises(SystemExit):
        pgdump.dump(address)


def test_dump_file_name_without_timestamp():
    """
    pgdump.dump_file_name retuns the name of the database
    """
 
    assert pgdump.dump_file_name(address) == "db_one.sql"   


def test_dump_file_name_with_timestamp():
    """
    pgdump.dump_file_name retuns the name of the database with timestamp
    """
    timestamp = "2017-12-03T13:14:10"
    assert pgdump.dump_file_name(address, timestamp) == f"db_one-{timestamp}.sql"   

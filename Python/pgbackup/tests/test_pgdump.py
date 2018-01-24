import pytest
import subprocess

from pgbackup import pgdump

url = "postgres://bob:password@example.com:5432/db_one"

# This ensures popen runs with specified params and returns something
def test_dump_call_pg_dump(mocker):
    """
    Utilize pg_dump to interact with Database
    """
    proc = mocker.Mock()
    mocker.patch('subprocess.Popen', return_value=proc) # mocker is a fixture like parser
    assert pgdump.dump(url) == proc
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE) # Popen is a similar command to pg_dump

# If postgreSQL pgdump isnt installed throwing an OSerror deal with it
def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump isn't installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)

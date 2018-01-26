import tempfile

from pgbackup import storage

def test_storing_file_locally():
    """
    Write content from one file-like to another
    """
    infile = tempfile.TemporaryFile('r+')
    infile.write("Testing")
    infile.seek(0)

    # Expects a file to read from and one to write to
    outfile = tempfile.NamedTemporaryFile(delete=False)
    storage.local(infile, outfile)
    with open(outfile.name) as f:
        assert f.read() == "Testing"

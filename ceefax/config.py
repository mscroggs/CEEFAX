import os as _os
from datetime import datetime as _dt


def test_dir(directory):
    if not _os.path.isdir(directory):
        try:
            _os.mkdir(directory)
        except:
            pass


def now():
    return _dt.now()


WIDTH = 80
HEIGHT = 30
NAME = "CEEFAX"
default_path = _os.path.join(_os.path.expanduser("~"), ".fax/")
pages_dir = None
ceefax_lib_path = _os.path.dirname(_os.path.realpath(_os.path.join(__file__, "..")))
ceefax_path = None

with open(_os.path.join(ceefax_lib_path, "VERSION")) as f:
    LIB_VERSION = f.read()
VERSION = None

sleeping_time_ms = 100
default_page_duration_sec = int(_os.getenv('default_page_duration_sec', 30))

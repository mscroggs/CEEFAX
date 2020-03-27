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
ceefax_lib_path = _os.path.dirname(_os.path.realpath(__file__))
ceefax_lib_pages = _os.path.join(ceefax_lib_path, "pages")
ceefax_path = None
pages_dir = None

try:
    with open(_os.path.join(ceefax_lib_path, "VERSION")) as f:
        LIB_VERSION = f.read()
except FileNotFoundError:
    with open(_os.path.join(ceefax_lib_path, "../VERSION")) as f:
        LIB_VERSION = f.read()
VERSION = None

sleeping_time_ms = 100
default_page_duration_sec = int(_os.getenv('default_page_duration_sec',
                                           30))

title = ""

def test_time():
    from ceefax.helpers import time
    assert time.datetime(year=2018, month=10, day=1).strftime("%Y") == "2018"

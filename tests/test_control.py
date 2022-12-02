import time
import pytest

from pyrupt.control import timeout

def test_timeout_intrerrupt():
    time_now = time.monotonic()
    
    with pytest.raises(RuntimeError):
        with timeout(0.5):
            time.sleep(1)
        
    time_end = time.monotonic() - time_now
    assert 0.5 <= time_end < 1 

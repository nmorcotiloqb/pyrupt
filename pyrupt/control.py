import contextlib


@contextlib.contextmanager
def timeout(time_limit: float):
    yield
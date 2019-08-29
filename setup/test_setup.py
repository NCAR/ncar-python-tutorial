import os


def test_conda_presence():
    from distutils.spawn import find_executable

    assert find_executable("conda") is not None or "conda" in os.environ["PATH"]

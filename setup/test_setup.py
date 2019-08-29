def test_conda_presence():
    from distutils.spawn import find_executable

    assert find_executable("conda") is not None

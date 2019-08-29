import os
import pytest

CIRCLE_CI_CHECK = os.environ.get("CIRCLECI", False)


@pytest.mark.skipif(CIRCLE_CI_CHECK, reason="$PATH doesn't get updated properly on CIRCLI")
def test_conda_presence():
    from distutils.spawn import find_executable

    assert find_executable("conda") is not None

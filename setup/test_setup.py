import os
import pytest

CIRCLE_CI_CHECK = os.environ.get("CIRCLECI")
if CIRCLE_CI_CHECK:
    CHECK = True
else:
    CHECK = False


@pytest.mark.skipif(CHECK, reason="$PATH doesn't get updated properly on CIRCLECI")
def test_conda_presence():
    from distutils.spawn import find_executable

    assert find_executable("conda") is not None

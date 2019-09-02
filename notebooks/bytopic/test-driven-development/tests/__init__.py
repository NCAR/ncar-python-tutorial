from my_cesm_package.statistics import mean


def test_ints():
    num_list = [1, 2, 3, 4, 5]
    obs = mean(num_list)
    exp = 3
    assert obs == exp


def test_zero():
    num_list = [0, 2, 4, 6]
    obs = mean(num_list)
    exp = 3
    assert obs == exp


def test_double():
    # This one will fail in Python 2
    num_list = [1, 2, 3, 4]
    obs = mean(num_list)
    exp = 2.5
    assert obs == exp


def test_long():
    big = 100000000
    obs = mean(range(1, big))
    exp = big / 2.0
    assert obs == exp


def test_complex():
    # given that complex numbers are an unordered field
    # the arithmetic mean of complex numbers is meaningless
    num_list = [2 + 3j, 3 + 4j, -32 - 2j]
    obs = mean(num_list)
    exp = NotImplemented
    assert obs == exp

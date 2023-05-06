import pytest
import Series.series


def test_fibo_0():
    actual = Series.series.fibo(0)
    expected = 0
    assert actual == expected
def test_fibo_1():
    actual = Series.series.fibo(1)
    expected = 1
    assert actual == expected
def test_fibo_2():
    actual = Series.series.fibo(2)
    expected = 1
    assert actual == expected
def test_fibo_3():
    actual = Series.series.fibo(3)
    expected = 2
    assert actual == expected
def test_fibo_5():
    actual = Series.series.fibo(5)
    expected = 5
    assert actual == expected
def test_fibo_10():
    actual = Series.series.fibo(10)
    expected = 55
    assert actual == expected


def test_lucas_0():
    actual = Series.series.lucas(0)
    expected = 2
    assert actual == expected
def test_lucas_1():
    actual = Series.series.lucas(1)
    expected = 1
    assert actual == expected
def test_lucas_2():
    actual = Series.series.lucas(2)
    expected = 3
    assert actual == expected
def test_lucas_5():
    actual = Series.series.lucas(5)
    expected = 11
    assert actual == expected


def test_sum_series_0_default():
    actual = Series.series.sum_series(0)
    expected = 0
    assert actual == expected
def test_sum_series_1_default():
    actual = Series.series.sum_series(1)
    expected = 1
    assert actual == expected
def test_sum_series_2_default():
    actual = Series.series.sum_series(2)
    expected = 1
    assert actual == expected
def test_sum_series_2_lucas():
    actual = Series.series.sum_series(2, 2, 1)
    expected = 3
    assert actual == expected
def test_sum_series_8_lucas():
    actual = Series.series.sum_series(6, 2, 1)
    expected = 18
    assert actual == expected
def test_sum_series_7():
    actual = Series.series.sum_series(7, 5, 10)
    expected = 170
    assert actual == expected
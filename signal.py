from math import pi, sin

from helper import *

PHI = pi / 32.0


def get_K(N):
    return 3 * N // 4


def get_M(N):
    minimum = get_K(N)
    maximum = 2 * N


def assert_n(N):
    assert is_power2(N) and N >= 64


def harmonic_value(n, N):
    return sin((2.0 * pi * n) / N)

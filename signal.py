from math import pi, sin, sqrt, cos

from helper import *


def assert_n(N):
    assert is_power2(N) and N >= 64


def harmonic_value(n, N, phase=0):
    return sin((2.0 * pi * n) / N + phase)


def harmonic_signal(N, M, phase=0):
    for n in range(M):
        yield harmonic_value(n, N, phase)


def mean_from_power(values):
    values = list(values)
    N = len(values)
    return sqrt(1 / (N + 1) * sum(x ** 2 for x in values))


def mean_from_variance(values):
    values = list(values)
    N = len(values)
    return sqrt(1 / (N + 1) * sum(x ** 2 for x in values) - (1 / (N + 1) * sum(values)) ** 2)


def fourier_amplitude(values):
    values = list(values)
    N = len(values)
    sin_sum, cos_sum = 0, 0
    for i, y in enumerate(values):
        angle = 2 * pi * i / N
        sin_sum += y * sin(angle)
        cos_sum += y * cos(angle)
    sin_sum *= 2 / N
    cos_sum *= 2 / N
    return sqrt(sin_sum ** 2 + cos_sum ** 2)

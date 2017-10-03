from math import pi

from draw import draw_plots
from signal import error_points_by_M, \
    harmonic_signal, \
    mean_from_power, \
    mean_from_variance, \
    fourier_amplitude, \
    EXPECTED_MEAN, \
    EXPECTED_AMPLITUDE

# Variant 1
PHASES = [0.0, pi / 32.0]
K_FROM_N = lambda N: 3 * N // 4
N = 64

LABELS = [
    'Amplitude error',
    'Mean from power error',
    'Mean from variance error'
]
PLOT_FUNCTIONS = [
    lambda phase: error_points_by_M(N, K_FROM_N(N), harmonic_signal, phase, EXPECTED_AMPLITUDE, fourier_amplitude),
    lambda phase: error_points_by_M(N, K_FROM_N(N), harmonic_signal, phase, EXPECTED_MEAN, mean_from_power),
    lambda phase: error_points_by_M(N, K_FROM_N(N), harmonic_signal, phase, EXPECTED_MEAN, mean_from_variance)
]


if __name__ == '__main__':
    draw_plots(PHASES, PLOT_FUNCTIONS, LABELS)

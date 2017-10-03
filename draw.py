from matplotlib import pyplot as plt


def draw_plots(phases, plot_functions, labels):
    plt.subplots_adjust(bottom=0.25)
    lines = []
    for i, phase in enumerate(phases):
        plt.subplot(2, 1, i + 1)
        for plot_function in plot_functions:
            x_points, y_points = plot_function(phase)
            line, = plt.plot(x_points, y_points)
            lines.append(line)

    plt.figlegend(lines, labels, loc='lower center')
    plt.show()

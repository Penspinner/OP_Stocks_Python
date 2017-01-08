from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

# Options for each letter figure
plot_options = {
    "title": "",
    "width": 150,
    "height": 150,
    "tools": ""
}

# S
S = figure(**plot_options)
S_x = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5]
S_y = [5, 4, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 2, 1]
S.circle(S_x, S_y, size=10, color="navy", alpha=0.5)

# T
T = figure(**plot_options)
T_x = [1, 2, 3, 4, 5, 3, 3, 3, 3]
T_y = [5, 5, 5, 5, 5, 4, 3, 2, 1]
T.triangle(T_x, T_y, size=10, color="green")

# E
E = figure(**plot_options)
E_x = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
E_y = [1, 2, 3, 4, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5]
E.diamond(E_x, E_y, size=10, color="purple")

# V
V = figure(**plot_options)
V_x = list(range(11))
V_y = [abs(i - 5) for i in V_x]
V.line(V_x, V_y, line_width=10, color="red")

# E2
E2 = figure(**plot_options)
E2_x = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
E2_y = [1, 2, 3, 4, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5]
E2.diamond(E2_x, E2_y, size=10, color="purple")

# N
N = figure(**plot_options)
N_x = [1, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5, 5]
N_y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]
N.line(N_x, N_y, line_width=10, color="orange")

# To hide toolbar: toolbar_location=None
p = gridplot([[S, T, E, V, E2, N]])
output_file("letters.html")
show(p)

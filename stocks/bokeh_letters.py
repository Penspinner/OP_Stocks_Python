from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

# Options for each letter figure
plot_options = {"width": 200, "height": 150}

# Axis
x = list(range(11))
y = [10, 10, 10, 10, 10, 10, 10, 10]

S = figure(**plot_options)
S.circle(x, y, color="navy", alpha=0.5)
T = figure()
E = figure()
V = figure()
N = figure()


p = gridplot([[S]])
output_file("letters.html")
show(p)

from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

plot_options = {}

S = figure()
T = figure()
E = figure()
V = figure()
N = figure()


p = gridplot([[]])
output_file("letters.html")
show(p)

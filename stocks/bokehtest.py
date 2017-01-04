import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot

########Figure 1########
# prepare some data
f1_x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
f1_y0 = [i**2 for i in f1_x]
f1_y1 = [10**i for i in f1_x]
f1_y2 = [10**(i**2) for i in f1_x]

# create a new plot
f1 = figure(
   tools="pan,box_zoom,reset,save",
   y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
   x_axis_label='sections', y_axis_label='particles'
)

# add some renderers
f1.line(f1_x, f1_x, legend="y=x")
f1.circle(f1_x, f1_x, legend="y=x", fill_color="white", size=8)
f1.line(f1_x, f1_y0, legend="y=x^2", line_width=3)
f1.line(f1_x, f1_y1, legend="y=10^x", line_color="red")
f1.circle(f1_x, f1_y1, legend="y=10^x", fill_color="red", line_color="red", size=6)
f1.line(f1_x, f1_y2, legend="y=10^x^2", line_color="orange", line_dash="4 4")

########Figure 2########
# prepare some data
f2_N = 4000
f2_x = np.random.random(size=f2_N) * 100
f2_y = np.random.random(size=f2_N) * 100
radii = np.random.random(size=f2_N) * 1.5
colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*f2_x, 30+2*f2_y)
]

TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

# create a new plot with the tools above, and explicit ranges
f2 = figure(tools=TOOLS, x_range=(0,100), y_range=(0,100))

# add a circle renderer with vectorized colors and sizes
f2.circle(f2_x, f2_y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

########Figure 3########
# prepare some data
f3_N = 100
f3_x = np.linspace(0, 4*np.pi, f3_N)
f3_y0 = np.sin(f3_x)
f3_y1 = np.cos(f3_x)
f3_y2 = np.sin(f3_x) + np.cos(f3_x)

# create a new plot
s1 = figure(width=250, plot_height=250, title=None)
s1.circle(f3_x, f3_y0, size=10, color="navy", alpha=0.5)

# NEW: create a new plot and share both ranges
s2 = figure(width=250, height=250, x_range=s1.x_range, y_range=s1.y_range, title=None)
s2.triangle(f3_x, f3_y1, size=10, color="firebrick", alpha=0.5)

# NEW: create a new plot and share only one range
s3 = figure(width=250, height=250, x_range=s1.x_range, title=None)
s3.square(f3_x, f3_y2, size=10, color="olive", alpha=0.5)

# output to static HTML file (with CDN resources)
output_file("templates/stocks/index.html", title="Examples", mode="cdn")

# put the subplots in a gridplot
p = gridplot([[f1], [f2], [s1, s2, s3]])

# show the results
show(p)

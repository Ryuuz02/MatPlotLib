import matplotlib as mlb
import matplotlib.pyplot as plt
import numpy as np

# !!!----------------------------------------------------------------------------------------------------------------!!!
# !!!----------------Using the matplotlib basic tutorial on their website, this is not my own work-------------------!!!
# !!!----------------------------------------------------------------------------------------------------------------!!!

# Takes only the axis part of a subplot
# ax = plt.subplots()[1]

# Takes figures and axis
# fig, ax = plt.subplots()

# Some different plots using lists and ranges
# ax.plot([1, 2, 3, 4], [1, 2, 3, 4])
# ax.plot([2, 1, 4, 3], [4, 3, 2, 1])
# ax.plot(range(1, 101), [x/10 for x in range(0, 100)])

# empty figure
# fig = plt.figure()

# Figure with one axis
# fig, ax = plt.subplots()

# Figure with 2x2 axes
# fig, axs = plt.subplots(2, 2)

# Figures take in np.arrays, other things might not work as intended. To convert, do as follows
# non_array = np.matrix([[1, 2], [3, 4]])
# into_array = np.asarray(non_array)

"""
# np.random.seed(""""""You can insert a seed here"""""")
# Creates some data for our figure
# a will be the x of our figure
# c is the color of our scatter dots
# d is the shape of our figure
data = {
    "a": np.arange(50),
    "c": np.random.randint(0, 50, 50),
    "d": np.random.randn(50)
}

# Creates b based on a, b will be our y value
data["b"] = data["a"] + 10 * np.random.randn(50)
# Since d uses randn, it can return negative numbers, so we make it an absolute value and make it bigger to see easier
data["d"] = np.abs(data["d"]) * 100

# Creates our figure and axis, the figsize determines the height and width of our graph (in inches), and the layout
# determines how the info is displayed
fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
# Makes the axis a scatter plot with the data
ax.scatter("a", "b", c="c", s="d", data=data)
# Labels the x and y axes
ax.set_xlabel("entry a")
ax.set_ylabel("entry b")

"""

"""
# Creates evenly space values over a range, of a specified amount of values. In this case from 0-2 makes 100 values
x = np.linspace(0, 2, 100)

# Creates figure and axis
fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")

# Some different plots, one is just a straight line, the next is the parabola of the quadratic, next is the cubic line
ax.plot(x, x, label="linear")
ax.plot(x, x**2, label="quadratic")
ax.plot(x, x**3, label="cubic")

# Some labels and a title, also adds a legend to see which line is which
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_title("Different Graphs")
ax.legend()
"""

plt.show()

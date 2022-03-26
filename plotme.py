#!/usr/bin/env python

"""plotme.py: Plot an x,y sequence of numbers in CSV. """

__author__      = "Henrik I Christensen"
__copyright__   = "NA 2022, Planet Earth"


import pandas as pd
import csv
import argparse
from distutils import util
import matplotlib.pyplot as plt

# construct the argument parser and parse arguments

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="path of input image")
ap.add_argument("-t", "--title", type=str, help="Title of the plot")
ap.add_argument("-x", "--x_label", type=str, help="label on x-axis")
ap.add_argument("-y", "--y_label", type=str, help="label on y-axis")
ap.add_argument("-g", "--grid", type=util.strtobool, help="turn grid on or off")
ap.add_argument("-h", "--header", type=util.strtobool, help="is first line a header?")
args = vars(ap.parse_args())

headers = ['x', 'y']
df = pd.read_csv(args["file"],names=headers)
print (df)
x = df['x']
y = df['y']

# plot
plt.plot(x,y)
plt.title(args["title"])
plt.xlabel(args["x_label"])
plt.ylabel(args["y_label"])
if args["grid"]:
    plt.grid()
# beautify the x-labels
plt.show()

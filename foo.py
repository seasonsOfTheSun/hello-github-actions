
import networkx as nx
import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

n_bins = 10
def assign_to_bin(weight, n_bins = 10):
    return int(weight // (1/n_bins))


def name_bin(x, n_bins=10):
    return f"{x/n_bins}-{(x+1)/n_bins}"

def points3d(x,y,z,colors):

    fig = go.Figure()
    fig = fig.add_scatter3d(
                    x=x,
                    y=y,
                    z=z,
                    marker = {"color":colors,
                              "size" :2,
                              "line" :dict(color='black', width=0.3)},
                    line={"width":0.0001}

             )

    return fig





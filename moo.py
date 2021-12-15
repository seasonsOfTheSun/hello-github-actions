
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







                    #line = dict(color='black', width=0.3)

fig.add_scatter3d(x=a[:,0],y=a[:,1],z=a[:,2],line={"width":0.0001}, marker = {"size":10,"line":dict(color='black', width=0.3)})

def draw_network(G,pos,n_bins=10):
    
    x_nodes = []
    y_nodes = []
    z_nodes = []
    
    for j in G.nodes():
    
        x_nodes.append(pos[j][0])
        y_nodes.append(pos[j][1])
        z_nodes.append(pos[j][2])
    
    
    
    bins = [name_bin(i) for i in range(n_bins)]
    
    x = []
    y = []
    z = []
    c = []
    
    for i,j in enumerate(G.edges()):

        x.extend([pos[j[0]][0], pos[j[1]][0], None])
        y.extend([pos[j[0]][1], pos[j[1]][1], None])
        z.extend([pos[j[0]][2], pos[j[1]][2], None])
        a = name_bin(assign_to_bin(float(G.edges()[j]['weight'])))
        c.extend([a,a,a])

    mu = pd.DataFrame({"x":x,"y":y,"z":z,"weight":c})
    
    # make some dummy length-zero edges with the right colors in the correct order 
    # so plotly makes the right colorbar
    bu = pd.DataFrame({"x":[0]*n_bins,"y":[0]*n_bins,"z":[0]*n_bins,"weight":bins[::-1]})
    df = pd.concat([bu,mu])
    
    fig = px.line_3d(df, x="x",
                         y="y",
                         z="z",
                         color="weight",
                         color_discrete_sequence=px.colors.sequential.Viridis_r
                     )

    #fig.add_scatter3d(x=x_nodes,
                       y=y_nodes,
                       z=z_nodes,
                       marker = {"color":labels.map(cmap).values,
                                 "size":10,
                                 "line":dict(color='black', width=0.3)
                                }
                       )
    return fig

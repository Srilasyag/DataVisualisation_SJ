# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:00:17 2020

@author: nnair
"""

import pandas as pd
import plotly
import plotly.graph_objs as go


# Load data that we will use.
timesData = pd.read_csv("timesData.csv")

""" Bar Plot """


# prepare data frame
df2015 = timesData[timesData.year == 2015].iloc[:5,:]


# create trace1 
trace1 = go.Bar(
                x = df2015.institution,
                y = df2015.citations,
                name = "citations",
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                              line=dict(color='rgb(0,0,0)',width=1.5))
                )

# create trace2 
trace2 = go.Bar(
                x = df2015.institution,
                y = df2015.publications,
                name = "publications",
                marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                              line=dict(color='rgb(0,0,0)',width=1.5))
                )

data = [trace1, trace2]

# Plotting the graph
fig = go.Figure(data=data)
plotly.offline.plot(fig,filename="barplot.html")




""" Scatter Plot """
import plotly.graph_objs as go


# Citation vs world rank of top 100 universities with 2014, 2015 and 2016 years

# prepare data frames
df2013 = timesData[timesData.year == 2013].iloc[:100,:]
df2014 = timesData[timesData.year == 2014].iloc[:100,:]
df2015 = timesData[timesData.year == 2015].iloc[:100,:]



# creating trace1
trace1 =go.Scatter(
                    x = df2013.world_rank,
                    y = df2013.citations,
                    mode = "markers",
                    name = "2013",
                    marker = dict(color = 'rgba(0, 255, 200, 0.8)'),
                    text= df2013.institution)

# creating trace2
trace2 =go.Scatter( 
                    x = df2014.world_rank,
                    y = df2014.citations,
                    mode = "markers",
                    name = "2014",
                    marker = dict(color = 'rgba(255, 128, 255, 0.8)'),
                    text= df2014.institution)

# creating trace3
trace3 =go.Scatter(
                    x = df2015.world_rank,
                    y = df2015.citations,
                    mode = "markers",
                    name = "2015",
                    marker = dict(color = 'rgba(255, 128, 2, 0.8)'),
                    text= df2015.institution)

data = [trace1, trace2, trace3]


layout = dict(title = 'Citation vs world rank of top 100 universities with 2013, 2014 and 2015 years',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Citation',ticklen= 5,zeroline= False)
             )

fig = dict(data = data, layout = layout)


plotly.offline.plot(fig, filename="scatterplot.html")



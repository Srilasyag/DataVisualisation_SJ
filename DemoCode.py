# -*- coding: utf-8 -*-
"""
Created on Sun May 31 09:57:36 2020

@author: nnair
"""

import pandas as pd
import plotly
import plotly.graph_objs as go



timesData=pd.read_csv("timesData.csv")

df2012= timesData[timesData.year == 2012].iloc[:5,:]
df2013= timesData[timesData.year == 2013].iloc[:5,:]



# Create Trace1
trace1 =go.Bar( 
               x= df2012.institution,
               y= df2012.citations,
               name='2012'
              )


trace2 =go.Bar( 
               x= df2013.institution,
               y= df2013.citations,
               name='2013'
              )

data=[trace1, trace2]

fig= go.Figure(data=data)
plotly.offline.plot(fig, filename="barplot.html")



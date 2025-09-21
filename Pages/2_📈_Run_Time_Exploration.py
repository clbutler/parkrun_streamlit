#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 22:00:15 2025

@author: chrisbutler
"""

#load our packages
import streamlit as st
import pandas as pd
import altair as alt

        
parkrun_df = st.session_state['parkrun_df']        


#add a line plot 
lineplot = parkrun_df.copy()
lineplot['Run date'] = pd.to_datetime(lineplot['Run date'], format = '%d/%m/%Y')
lineplot['time_in_minutes'] = lineplot['time_delta'].dt.total_seconds() / 60

# Create the Altair chart
lplot = alt.Chart(lineplot).mark_line().encode(
    x = alt.X('Run date', axis = alt.Axis(title = 'Run Date')),
    y = alt.Y('time_in_minutes', title = 'Run Time (Minutes)', scale = alt.Scale(zero = False))).properties(title = 'Your Parkruns Over Time')

st.altair_chart(lplot)
    


   
#add the boxplot
boxplot = parkrun_df.copy()
boxplot['time_in_minutes'] = boxplot['time_delta'].dt.total_seconds() / 60
bplot = alt.Chart(boxplot).mark_boxplot(extent = "min-max").encode(
    x = alt.X('time_in_minutes', axis = alt.Axis(title = 'Time (minutes)'), scale = alt.Scale(zero = False)),
y = alt.Y('category:N', axis = None)).properties(title = 'Your Parkrun Performance')


st.altair_chart(bplot)
    


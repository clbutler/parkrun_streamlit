#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 22:07:33 2025

@author: chrisbutler
"""

#load our packages
import streamlit as st
import pandas as pd

if 'parkrun_df' in st.session_state:

    
    
    unfiltered_parkruns = st.session_state['unfiltered_parkruns']
    parkrun_df = st.session_state['parkrun_df']    
    
    #add the number of unique events card
    unique_location = len(unfiltered_parkruns['Event'].unique())
    
    
    #add your favourite event card
    fav_runs = unfiltered_parkruns.groupby('Event').count().reset_index()
    fav_runs = fav_runs[['Event', 'Run date']].sort_values('Run date', ascending = False)
    fav_runs = fav_runs.iloc[0,0]
    
    col1, col2, = st.columns(2)
    col1.metric("Number of Parkrun Locations", unique_location, border = True)
    col2.metric("Most Visited Parkrun Location", fav_runs, border = True)
    
    
    #add the map
    from parkrun_functions import json_mapping
    locations = json_mapping('parkrun_locations.json')
    locations = pd.merge(left = unfiltered_parkruns, right = locations, how = 'left', left_on= 'Event', right_on = 'EventShortName')
    st.map(locations, size = 20)

else:
        st.title("Welcome to Your Parkrun Dashboard!")
        col1, col2, col3 = st.columns([1, 6, 1])

        with col2:
            st.image('parkrun_logo.png', caption = 'Your Parkrun journey starts here!')
        st.write("It looks like you haven't uploaded your parkrun data yet. To get started, please navigate to the **📊 Import ParkRun Data** page. Once you've uploaded your results, you'll be able to see a custom dashboard with your performance over time, including your fastest times, progress, and more.")
        st.info('Click the link in the sidebar to begin.')  
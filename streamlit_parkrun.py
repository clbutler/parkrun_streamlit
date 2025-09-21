#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 11:23:17 2025

@author: chrisbutler
"""

#load our packages
import streamlit as st
import pandas as pd
import altair as alt
import json

#create our header 
st.write("ParkRun Data Exploration App")

#create our upload box 
uploaded_file = st.file_uploader(label = 'Upload your ParkRun data as a csv file here', type = 'csv')

#Visualise the dataframe
if uploaded_file:
    parkrun_df = pd.read_csv(uploaded_file)
    parkrun_df.columns = parkrun_df.columns.str.strip().str.capitalize()

    
    #set up multiselect for run location 
    with st.sidebar:
        locations = parkrun_df['Event'].unique()
        locations_selected = st.multiselect('Select the parkrun locations you are interested in (optional)', locations)
        if locations_selected:
            parkrun_df = parkrun_df[parkrun_df['Event'].isin(locations_selected)]
        
            
        
    parkrun_df['time_delta'] = pd.to_timedelta('00:' + parkrun_df['Time'])
    
    
    #card creation 
    num_races = len(parkrun_df)
    fastest_time = parkrun_df['time_delta'].min().total_seconds()
    minutes_fastest = int(fastest_time/60)
    seconds_fastest = int(fastest_time % 60)
    fastest_time_str = "{:02}:{:02}".format(minutes_fastest, seconds_fastest)
    
    average_time = parkrun_df['time_delta'].mean().total_seconds()
    minutes_average = int(average_time/60)
    seconds_average = int(average_time % 60)
    average_time_str = "{:02}:{:02}".format(minutes_average, seconds_average)
    

    #card change creation
    historic = parkrun_df.iloc[1:,]
    average_time_historic = historic['time_delta'].mean().total_seconds()
    change_since_last_run = (((average_time - average_time_historic)/average_time_historic)*100)
    change_since_last_run = round(change_since_last_run, 2)

    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total ParkRuns", num_races, border = True)
    col2.metric("Quickest ParkRun Time", fastest_time_str, border = True)
    col3.metric("Average ParkRun Time", average_time_str, '{} %'.format(change_since_last_run) , border = True, delta_color = 'inverse')

    
    parkrun_df_view = parkrun_df.drop('time_delta',axis = 1)
    st.write(parkrun_df_view)
    
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
    
    #add the number of unique events card
    unique_location = len(parkrun_df['Event'].unique())
    
    
    #add your favourite event card
    fav_runs = parkrun_df.groupby('Event').count().reset_index()
    fav_runs = fav_runs[['Event', 'Run date']].sort_values('Run date', ascending = False)
    fav_runs = fav_runs.iloc[0,0]
    
    col1, col2, = st.columns(2)
    col1.metric("Number of Parkrun Locations", unique_location, border = True)
    col2.metric("Most Visited Parkrun Location", fav_runs, border = True)
    
    
    #add the map
    from parkrun_functions import json_mapping
    locations = json_mapping('parkrun_locations.json')
    locations = pd.merge(left = parkrun_df, right = locations, how = 'left', left_on= 'Event', right_on = 'EventShortName')
    st.map(locations, size = 20)
# =============================================================================

# =============================================================================
# 
#  parkrun_df = pd.read_csv('all_results.csv')
#  parkrun_df.columns = parkrun_df.columns.str.strip().str.capitalize()
#  parkrun_df['time_delta'] = pd.to_timedelta('00:' + parkrun_df['Time'])
#  st.write(parkrun_df)
#  
#  #card creation 
#  num_races = len(parkrun_df)
#  fastest_time = parkrun_df['Time'].min().round(2)
#  average_time = parkrun_df['Time'].mean().round(2)
#  
#  #card change creation
#  historic = parkrun_df.iloc[1:,]
#  average_time_historic = historic['Time'].mean().round(2)
#  change_since_last_run = average_time - average_time_historic
#  change_since_last_run = int(change_since_last_run)
#  
#  col1, col2,col3 = st.columns(3)
#  col1.metric("Total ParkRuns", num_races)
#  col2.metric("Quickest ParkRun", str(fastest_time))
#  col3.metric("Average ParkRun", str(average_time), change_since_last_run)
# =============================================================================
# =============================================================================

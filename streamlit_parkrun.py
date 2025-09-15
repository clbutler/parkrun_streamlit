#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 11:23:17 2025

@author: chrisbutler
"""

#load our packages
import streamlit as st
import pandas as pd
import seaborn as sns

#create our header 
st.write("ParkRun Data Exploration App")

#create our upload box 
uploaded_file = st.file_uploader(label = 'Upload your ParkRun data as a csv file here', type = 'csv')

#Visualise the dataframe
if uploaded_file:
    parkrun_df = pd.read_csv(uploaded_file)
    parkrun_df.columns = parkrun_df.columns.str.strip().str.capitalize()

    
    #set up slider for run location 
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
    st.write(parkrun_df)
   
    #add the boxplot
    boxplot = parkrun_df.copy()
    boxplot['time_in_minutes'] = boxplot['time_delta'].dt.total_seconds() / 60
    boxplot = sns.boxplot(data = boxplot['time_in_minutes'], orient = 'h', width = .2)
    boxplot.set_xlabel('Time in Minutes')
    boxplot.set_title('Run Time Distribution')
    st.pyplot(boxplot.get_figure())
    



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

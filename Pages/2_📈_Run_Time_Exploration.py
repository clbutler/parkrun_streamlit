#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 22:00:15 2025

@author: chrisbutler
"""


        
            
        
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
    


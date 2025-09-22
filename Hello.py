#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 11:23:17 2025

@author: chrisbutler
"""

#load our packages
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Wecome to your ParkRun App")

st.sidebar.success("Start With Importing Your ParkRun Data")

st.write('This application was  created with **Streamlit** by Dr. Chris Butler')

col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    st.image('parkrun_logo.png', caption = 'Your Parkrun journey starts here!')




st.markdown(
    """


    
    This app provides a comprehensive analysis of your personal Parkrun journey. It offers insights into your performance over time and across different locations.

    The app is organised into two main pages: **📈 Run Time Exploration** and **🌍 Location Exploration**. Each page is designed to give you a detailed view of your Parkrun statistics.

    ### Instructions for Use

    Getting started is straightforward. Just follow these steps to set up and visualise your data:

    1.  **Download the File**: First, download the `parkrun.csv` file from the provided GitHub page.

    2.  **Update Your Data**: Your personal results are stored in the `parkrun.csv` file. Since Parkrun doesn't allow API access, you'll need to update this file manually:
        * Log in to your Parkrun account.
        * Go to the **'Results'** tab.
        * Click on **'View stats for all parkruns by this parkrunner'**.
        * **Copy and paste** the entire **'All Results'** table directly into your `parkrun.csv` file.
        
    
    
        
    3.  **Import**: Finally, import your updated `parkrun.csv` file into the app using the **📊 Import ParkRun Data** tab.
    """
)


#
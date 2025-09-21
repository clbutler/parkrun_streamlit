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

st.write("# Wecome to your ParkRun App 👋")

st.sidebar.success("Start With Importing Your ParkRun Data")

st.markdown(
    """
This ParkRun application provides a comprehensive analysis of your personal ParkRun journey, offering insights into your performance over time and across different locations.

The application is organized into two main pages, each designed to give you a detailed view of your ParkRun statistics:

Instructions for Use


Getting started with your ParkRun App is straightforward! Just follow these steps to set up and visualize your data:

1. Download the Files


First, download the following file from this GitHub page:
    

parkrun.csv


2. The parkrun.csv file is where your personal ParkRun results live. Since ParkRun doesn't offer API connectivity or allow web scraping, you'll need to manually update this file with your own data:

Log in to your ParkRun account.


Navigate to the "Results" tab.


Click on "View stats for all parkruns by this parkrunner".


Copy and paste the entire table (currently titled "All Results") directly into your parkrun.csv file.


The app was created using Streamlit and all code was written by Christopher L Butler
"""
)


#
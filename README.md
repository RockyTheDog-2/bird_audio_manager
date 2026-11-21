
# St. Louis Project Wildlife Database

A Streamlit application for recording and reviewing wildlife observations in the St. Louis area.

## Features

- Submit bird observations manually
- Identify bird species from audio using BirdNET
- Save observation details and identification scores
- Browse wildlife records

## Setup

1. Install Python 3.13.
2. Install the dependencies:

   `python -m pip install -r requirements.txt`

3. Configure the sumbission_pin, admin_pin, github_token (only do this if you are going to use github to back up your data, otherwise plug in your own database or storage method), and github_repo (ditto) in `.streamlit/secrets.toml`.
4. We prefer to use Streamlit~=1.66.0 because it looks better to us, but the newer versions start faster, so keep that in mind when you are installing our requirments.txt
5. In Input_Species_Data.py, it is configured to only look for birds in the St. Louis area, so change that if you are going to use it somewhere else.
6. Start the application:

   `python -m streamlit run "Home Page.py"`

## Data and privacy

Any observations made, audio uploaded, and changes to the main submissions csv files will be uploaded to your own Github repo if you configure it to do so. Otherwise remove those lines of code in Input_Species_Data.py and Wildlife_Database_Administration.py
It will not be uploaded to our repo unless you somehow got a token to do so and configured it that way.

## AI use disclosure

We did indeed use some AI to troubleshoot bugs and make the csv converter, along with some other things

## Crediting us

If you are going to use this project to use it or change it in any way, feel free!
However, please credit Dhruv Bherthepudi and Matthew Elliott for working on it

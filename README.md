# Python Flask Component of Titanium Crab's Treehacks 2021 Project

## To run and build the web app:

1) Commit the files you want to edit and the build/deploy pipline will automatically run
2) Navigate to the flask app's service page (flask-dki7nqauggpky)
3) Click "Start" and make sure that the app deployment is finished (about 30 seconds)
4) Reload url (https://flask-dki7nqauggpky.azurewebsites.net/) and see the product :)

## Pipelines
* Scheduled data collection pipeline: runs every hour and runs the python script to grab data from our backend and publish
the data into a JSON object for ease of access and visualization
* Main build/deploy pipeline: Runs manually but eventually at each production level commit to master branch. Builds and 
packages script and web dev files to send to the Azure Linux app

## Folders and files
* EMBEDDING: Contains scripts and utility functions for grabbing article data and applying OpenAI's APIs
* app.py: main Flask application
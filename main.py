import requests
from dotenv import load_dotenv
import os
import json
from flask import Flask, render_template
#import packages above
#loads the .env file into the program
load_dotenv()

api_key = os.getenv('nasa_api_key')

#pulls data from the api
r = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + api_key)
api_output = r.json()

#defining each part to a variable for later
apod_date = api_output['date']
apod_explain = api_output['explanation']
apod_pic = api_output['hdurl']
apod_title = api_output['title']

app =  Flask(__name__)

@app.route('/')
def home():
    message = 'NASA Astronomy Picture of the Day'
    pic_title = apod_title
    pic = apod_pic
    explain = apod_explain
    return render_template('index.html', message=message, pic_title=pic_title, pic=pic, explain=explain)
#This is creating a webpage at / and referencing the html file in this document and pulling the variables from the api pull
#to fill in the parts of the site that change daily.
if __name__ == '__main__':
    app.run()
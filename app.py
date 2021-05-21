from typing import Text
from flask import Flask
from flask.templating import render_template
from flask import request
import boto3
from werkzeug.utils import secure_filename
import os


app=Flask("myapp")
if __name__ == '__main__':
    app.run(debug=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def result():
    os.system("sleep 5")
    if request.method == "GET":
        polly=boto3.client('polly')
        text=request.args.get("text")
        voice=request.args.get("voice")
        name=request.args.get("name")
        response=polly.synthesize_speech(Text=text,OutputFormat="mp3",VoiceId=voice)
        output="static/audio/"+name+"output.mp3"
        file=open(output,'wb')
        file.write(response['AudioStream'].read())
        return render_template("output.html" , output=output)



    else:
        return"Error"


import time, os
from flask import Flask, render_template, url_for, redirect

app=Flask(__name__)

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

@app.route('/', methods=['GET', 'POST'])
def index():
    logFile = open("/home/minecraft/gamingnation/logs/latest.log")
    loglines = follow(logfile)
    for line in loglines:
        mc_chat = lines

    return render_template('index.html', mc_chat=mc_chat)

if __name__ == "__main__":
    app.run(debug=True)
    

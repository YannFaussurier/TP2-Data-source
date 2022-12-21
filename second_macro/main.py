
from flask import Flask, render_template

import requests

app = Flask(__name__)

# def hello_world():
#  prefix_google = """
#  <!-- Google tag (gtag.js) -->
# <script async
# src="https://www.googletagmanager.com/gtag/js?id=UA-250346713-1"></script>
# <script>
#  window.dataLayer = window.dataLayer || [];
#  function gtag(){dataLayer.push(arguments);}
#  gtag('js', new Date());
#  gtag('config', ' UA-250346713-1');
# </script>
#  """
#  return prefix_google + "Hello World"


@app.route('/', methods=["GET"])
def hello_world():
    return "Hello World"

@app.route('/cookies/', methods = ["GET"])
def req():
    req = requests.get("https://analytics.google.com/analytics/web/#/report-home/a250346713w344997828p281181552")
    
    #return req.cookies.get_dict()
    return req.text



#@app.route('/log', methods=["GET"])
#def index():
#    return render_template('index.html')

@app.route('/log', methods = ["GET"])
def logger():
    return render_template('log.html')
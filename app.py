from http.client import responses
from flask import Flask, request
import requests
import json


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    out = ""
    export = ""
    response = ""
    data = ""
    try:
        #response = requests.get("https://az999-vmappl02.itris-cloud.ch/api/table.json?content=sensortree&username=svc_prtg-api_pause&passhash=3970061384")
        response = requests.get("https://az999-vmappl02.itris-cloud.ch/api/table.xml?content=sensors&output=html&columns=objid,probe,group,device,sensor,status,message,lastvalue&count=400&username=svc_prtg-api_pause&passhash=3970061384")
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
    #data = json.loads(response.text)
    #data = json.dumps(data)
    return("""<html><head><h1>Test titel</h1></head></html>""" + response.text)
"""
@app.route("/", methods=['GET'])
def button_pause():
    row = ""
    objid = ""
    uri = ""
    prtgcore = "https://az999-vmappl02.itris-cloud.ch"
    for row in data:
        objid = row.Cells[0].Value
        uri = prtgcore+"'/api/pause.htm?id='objid'&pausemsg='message - Paused by USERNAME'&action=0&'auth"
        export = export.get(uri)
"""


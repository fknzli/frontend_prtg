from flask import Flask, request
import requests
import json
import os
#import pandas as pd

app = Flask(__name__)



@app.route("/", methods=['GET'])
def home():
    auth = "username=rhaerri&passhash=3835350314"
    auth_demo = "username=prtgadmin&password=password"
    url_demo = "https://demo-mon-01.demoren.ch/table.htm?content=sensors&output=json&columns=objid&count=1&"+auth_demo+"&noraw=1"
    url = "https://monitoring.itris-cloud.ch/api/table.htm?content=sensors&output=json&columns=objid,probe,group,device,sensor,status,message,lastvalue&count=200&"+auth+"&noraw=1"
    url_test = "https://monitoring.itris-cloud.ch/api/table.xml?content=sensortree&"+auth
    url_test_demo = "https://demo-mon-01.demoren.ch/api/table.xml?content=sensortree&"+auth_demo
    out = ""
    export = ""
    response = ""
    data = ""

    try:
        response = requests.get("https://az999-vmappl02.itris-cloud.ch/api/table.json?content=sensors&output=json&columns=objid,probe,group,device,sensor,status,message,lastvalue&count=400&username=svc_prtg-api_pause&passhash=3970061384")
        #refexport = export.sensors
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        #out += (e, file=sys.stderr)
        #raise SystemExit(e)
    data = json.loads(response.text)
    data = json.dumps(data)
    #response_df = pd.DataFrame(data=data, columns=['device', 'sensor', 'status'])
    #response_df.head(10)
    deganzihtmlcode = """<html><head><h1>titel</h1></head></html>""" + data
    return(deganzihtmlcode)
    
    #out += "\n" + x
    return "Hello \n " + out

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



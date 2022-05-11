from flask import Flask, request
import requests
import json

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
    x = ""
    try:
        x = requests.get("https://monitoring.itris-cloud.ch/api/table.xml?content=sensors&output=html&columns=objid,probe,group,device,sensor,status,message,lastvalue&count=400&username=rhaerri&passhash=3835350314")
        #x = requests.get("https://demo-mon-01.demoren.ch/api/table.xml?content=sensortree&output=html&columns=objid,probe,group,device,sensor,status,message,lastvalue&count=200&username=prtgadmin&password=password")
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        #out += (e, file=sys.stderr)
        #raise SystemExit(e)
        
    #data = json.loads(x.text)
    #data = json.dumps(data)
    return(x.text)
    #out += "\n" + x
    return "Hello \n " + out
    #https://monitoring.itris-cloud.ch/api/table.htm?content=sensors&output=json&columns=objid,probe,group,device,sensor,status,message,lastvalue&count=200&username=rhaerri&passhash=3835350314&noraw=1
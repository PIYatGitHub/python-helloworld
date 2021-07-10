from logging import Logger
from flask import Flask, json, logging
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('/ was successful');
    return "Hello World!"

@app.route("/status")
def status():
    
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('/status was successful');
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('/metrics was successful');
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

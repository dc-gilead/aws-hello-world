from flask import Flask, render_template, redirect, make_response, Response, jsonify
import requests
import os
app = Flask(__name__)

@app.route("/")
def hello():
    who =  os.environ.get('WHO')
    what = os.environ.get('WHAT')
    when = os.environ.get('WHEN')
    hello = {'Who' : who, 'What': what, 'When': when}
    dict = {'text': hello}
    return jsonify(dict)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5001)

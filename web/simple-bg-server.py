import json, os   
from flask import Flask
from queue import Queue


app = Flask(__name__)
hits = []
hits_q = Queue(maxsize = 6 )
version = os.environ.get('VERSION')

def append_version(curr_version): 
    if hits_q.full(): 
        hits_q.get()

    hits_q.put(curr_version)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/demo")
def hello_demo():
    return "<h1>Hello, Kube-Con</h1>"


@app.route("/version")
def return_version():
    append_version(version)
    return f"<p>{version}<p>"

@app.route("/hits")
def print_hits():
    hits = list(hits_q.queue)
    jsonStr= json.dumps(hits)
    return jsonStr

if __name__ == '__main__':
    app.run(debug=True, port='8000')


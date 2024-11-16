import json
import random
import time

from flask import Flask, Response, render_template

app = Flask(__name__)

CHECKBOXES = [False] * 10


def get_message():
    """this could be any function that blocks until data is ready"""
    time.sleep(0.1)
    return json.dumps(CHECKBOXES)


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/set/<int:idx>/<int:val>")
def update(idx, val):
    CHECKBOXES[idx] = bool(val)
    return "OK"


@app.route("/stream")
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            yield "data: {}\n\n".format(get_message())

    return Response(eventStream(), mimetype="text/event-stream")


app.run(host="0.0.0.0", port=8080)

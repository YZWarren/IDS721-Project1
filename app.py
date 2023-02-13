from flask import request, Flask, render_template, jsonify
import requests

import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
import torch
import torchvision

import numpy as np
from src.generator import generate
from src.calculator import calculator

app = Flask(__name__)

@app.route('/generate')
def refresh_generate():
    gen_imgs = generate()
    gen_imgs = gen_imgs / 2 + 0.5

    plt.imshow(np.transpose(gen_imgs, (1, 2, 0)))
    plt.axis('off')

    data = io.BytesIO()
    plt.savefig(data, format='png')
    img_stream = base64.b64encode(data.getvalue()).decode()
    return render_template('generate.html',
                           img_stream=img_stream)

@app.route("/")
def hello():
    """return an HTTP greeting and show code rain."""
    return render_template("hello.html")

@app.route("/calculate")
def calculate_home():

    return "Calculator that supports +, -, *, %, (, and ).Usage: /calculate/(1+2)*3\n\r"

@app.route("/calculate/<expression>")
def calculate_expr(expression):
    
    try:
        result = calculator(str(expression))
    except:
        result = "Inputting expression illegal, try again"

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)

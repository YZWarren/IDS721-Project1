from flask import request, Flask, render_template, jsonify
import requests

# import io
# from acgan.ACGAN import *
# import torch
# import torchvision
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import numpy as np
# import base64

app = Flask(__name__)


# def generate():
#     latent_dim = 100
#     num_classes = 10
#     batch_size = 16

#     generator = Generator(latent_dim + num_classes)
#     generator.load_state_dict(torch.load('./acgan/generator.pth', map_location=torch.device('cpu')))
#     generator.eval()

#     label = np.random.randint(0, 9)
#     z = torch.randn(batch_size, latent_dim)
#     gen_class = np.random.randint(label, label+1, batch_size)
#     z_labels = torch.zeros(batch_size, num_classes)
#     z_labels[np.arange(batch_size), gen_class] = 1.0
#     z = torch.concat((z, z_labels), 1)
#     gen_class = torch.from_numpy(gen_class).type(torch.LongTensor)

#     gen_imgs = generator(z).detach()
#     return torchvision.utils.make_grid(gen_imgs, nrow=4).numpy()

# @app.route('/generate')
# def refresh_generate():
#     gen_imgs = generate()
#     gen_imgs = gen_imgs / 2 + 0.5

#     plt.imshow(np.trrespose(gen_imgs, (1, 2, 0)))
#     plt.axis('off')

#     data = io.BytesIO()
#     plt.savefig(data, format='png')
#     img_stream = base64.b64encode(data.getvalue()).decode()
#     return render_template('generate.html',
#                            img_stream=img_stream)


def evaluate_expr(stack):
    if not stack or type(stack[-1]) == str:
        stack.append(0)

    last_operation = " "
    lastNum = stack.pop()
    res = lastNum
    while stack and stack[-1] != ")":
        operation = stack.pop()
        if operation == "+":
            last_operation = "+"
            lastNum = stack.pop()
            res += lastNum
        elif operation == "-":
            last_operation = "+"
            lastNum = -stack.pop()
            res += lastNum
        elif operation == "*":
            curr = int(stack.pop())
            if last_operation == "+":
                res = res - lastNum + lastNum * curr
            else:
                res = res * curr
            last_operation = " "
            lastNum = curr
        elif operation == "/":
            curr = int(stack.pop())
            if last_operation == "+":
                res = res - lastNum + lastNum / curr
            else:
                res /= curr
            last_operation = " "
            lastNum = curr

    return res


def calculator(s):
    stack = []
    n, operand = 0, 0

    for i in range(len(s) - 1, -1, -1):
        ch = s[i]
        if ch.isdigit():
            operand = (10**n * int(ch)) + operand
            n += 1

        elif ch != " ":
            if n:
                stack.append(operand)
                n, operand = 0, 0

            if ch == "(":
                res = evaluate_expr(stack)
                stack.pop()
                stack.append(res)
            else:
                stack.append(ch)

    if n:
        stack.append(operand)

    return evaluate_expr(stack)


@app.route("/")
def hello():
    """return an HTTP greeting and show code rain."""
    return render_template("hello.html")

@app.route("/calculate")
def calculate_home():

    return "Calculator that supports +, -, *, /, (, and ).Usage: /calculate/(1+2)*3\n\r"

@app.route("/calculate/<expression>")
def calculate_expr(expression):
    
    try:
        result = calculator(str(expression))
    except:
        result = "Inputting expression illegal, try again"

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)

from flask import request, Flask, render_template, jsonify
import requests
# from acgan.ACGAN import *
# import numpy as np


app = Flask(__name__)

@app.route('/chatgpt', methods=['GET', 'POST'])
def chatgpt():
    api_key=request.form.get('key')
    prompt = ""
    headers = {"Authorization":f"Bearer {api_key}"}
    api_url = "https://api.openai.com/v1/completions"

    resp = dict()
    resp["choices"] = [{"text": " "}]
    resp = jsonify(resp)

    prompt = request.form.get('prompt')
    data = {'prompt':prompt,
            "model":"text-davinci-003",
            'max_tokens':256,
            'temperature':1,
            }
    response = requests.post(api_url,json = data,headers = headers)
    resp = response.json()
    if "error" in resp.keys():
        print("Error: ", resp["error"])
        result = resp["error"]["message"].strip()
        return render_template("chatgpt.html", result=result if prompt else None)

    result = resp["choices"][0]["text"].strip()
    return render_template("chatgpt.html", result=result if prompt else None)

# @app.route('/generate', methods=['GET', 'POST'])
# def generate():
#     latent_dim = 100
#     num_classes = 10
#     batch_size = 16

#     generator = Generator(latent_dim + num_classes)
#     generator.load_state_dict(torch.load('./acgan/generator.pth')) 

#     z = torch.randn(batch_size, latent_dim)
#     gen_class = np.random.randint(label, label+1, batch_size)
#     z_labels = torch.zeros(batch_size, num_classes)
#     z_labels[np.arange(batch_size), gen_class] = 1.0
#     z = torch.concat((z, z_labels), 1)
#     gen_class = torch.from_numpy(gen_class).type(torch.LongTensor)

#     gen_imgs = generator(z)
#     return render_template("generate.html", result=gen_imgs)

@app.route('/')
def hello():
    """return an HTTP greeting and show code rain."""
    # return render_template("hello.html")
    return "This is the home page. Please go to /chatgpt to chat with GPT-3."
    # return render_template("chatgpt.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

from flask import request, Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/chatgpt', methods=['GET', 'POST'])
def chatgpt():
    api_key="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"
    prompt = ""
    headers = {"Authorization":f"Bearer {api_key}"}
    api_url = "https://api.openai.com/v1/completions"

    resp = dict()
    resp["choices"] = [{"text": " "}]
    resp = jsonify(resp)

    prompt = request.form.get('prompt')
    print("Prompt inputted: ", prompt)
    data = {'prompt':prompt,
            "model":"text-davinci-003",
            'max_tokens':256,
            'temperature':1,
            }
    response = requests.post(api_url,json = data,headers = headers)
    print("Response: ", response, type(response))
    resp = response.json()
    if "error" in resp.keys():
        print("Error: ", resp["error"])
        result = resp["error"]["message"].strip()
        return render_template("chatgpt.html", result=result if prompt else None)

    result = resp["choices"][0]["text"].strip()
    return render_template("chatgpt.html", result=result if prompt else None)

@app.route('/')
def hello():
    """return an HTTP greeting and show code rain."""
    # return render_template("hello.html")
    return "This is the home page. Please go to /chatgpt to chat with GPT-3."
    # return render_template("chatgpt.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

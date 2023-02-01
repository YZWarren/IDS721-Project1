from flask import request, Flask, render_template
import requests,json

app = Flask(__name__)

@app.route('/chatgpt', methods=['GET', 'POST'])
def chatgpt():
    api_key="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"
    prompt = ""
    headers = {"Authorization":f"Bearer {api_key}"}
    api_url = "https://api.openai.com/v1/completions"

    prompt = request.form.get('prompt')
    print(prompt)
    data = {'prompt':prompt,
            "model":"text-davinci-003",
            'max_tokens':256,
            'temperature':1,
            }
    response = requests.post(api_url,json = data,headers = headers)
    resp = response.json()
    print("A:",resp["choices"][0]["text"].strip(),end="\n")
    result = resp["choices"][0]["text"].strip()
    return render_template("chatgpt.html", result=result)

@app.route('/')
def hello():
    """return an HTTP greeting and show code rain."""
    # return render_template("hello.html")
    return render_template("chatgpt.html")

if __name__ == '__main__':
    app.run(debug=True)

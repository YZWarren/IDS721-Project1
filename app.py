from flask import request, Flask, render_template
import requests

app = Flask(__name__)

@app.route('/chatgpt', methods=['GET', 'POST'])
def chatgpt():
    api_key="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"
    prompt = ""
    headers = {"Authorization":f"Bearer {api_key}"}
    api_url = "https://api.openai.com/v1/completions"

    prompt = request.form.get('prompt')
    print("Prompt inputted: ", prompt)
    data = {'prompt':prompt,
            "model":"text-davinci-003",
            'max_tokens':256,
            'temperature':1,
            }
    response = requests.post(api_url,json = data,headers = headers)
    resp = response.json()
    print("Response: ", resp)
    print("Answer: ", resp["choices"][0]["text"].strip(),end="\n")
    result = resp["choices"][0]["text"].strip()
    return render_template("chatgpt.html", result=result if prompt else None)

@app.route('/')
def hello():
    """return an HTTP greeting and show code rain."""
    # return render_template("hello.html")
    return render_template("chatgpt.html")

if __name__ == '__main__':
    app.run(debug=True)

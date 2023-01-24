from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    """return an HTTP greeting and show code rain."""
    return render_template("hello.html")

if __name__ == '__main__':
    app.run(debug=True)
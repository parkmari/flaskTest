from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    host_addr = "0.0.0.0"

    app.run(host=host_addr)


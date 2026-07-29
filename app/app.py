from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello DevOPs Production!!"


@app.route("/health")
def health():
    return {
        "status":"ok"
    }


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        ports=80000,
        debug=True
    )

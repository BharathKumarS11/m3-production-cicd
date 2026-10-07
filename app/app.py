import importlib

Flask = importlib.import_module("flask").Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "M3 Production CI/CD - Version 1"


@app.route("/health")
def health():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
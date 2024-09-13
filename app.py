import subprocess
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run_script", methods=["POST"])
def run_script():
    data = request.get_json()
    script_path = data["path"]

    try:
        subprocess.run(
            ["cmd", "/c", script_path], capture_output=True, text=True, check=True
        )
        return jsonify({"message": "Script executed sucessfully!"})
    except subprocess.CalledProcessError as e:
        return jsonify({"message": f"Error detected: {e.stderr}"}), 500


if __name__ == "__main__":
    app.run(debug=True)

# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# https://docs.lextudio.com/blog/running-flask-web-apps-on-iis-with-httpplatformhandler/

# https://flask.palletsprojects.com/en/3.0.x/deploying/
# https://learn.microsoft.com/pt-br/visualstudio/python/configure-web-apps-for-iis-windows?view=vs-2022
# https://www.bing.com/search?q=WSGI+server+flask+IIS&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=wsgi+server+flask+iis&sc=10-21&sk=&cvid=52E20A37788040CBADE9F706305BC946&ghsh=0&ghacc=0&ghpl=
# https://www.bing.com/search?q=Flask+Python+Https+Instance&qs=n&form=QBRE&sp=-1&lq=0&pq=flask+python+https+instance&sc=6-27&sk=&cvid=4CAEEB5224944417BBE61061DCB38584&ghsh=0&ghacc=0&ghpl=

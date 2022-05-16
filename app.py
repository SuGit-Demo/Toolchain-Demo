#templates are used to separate bussiness logic from presentation logic
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

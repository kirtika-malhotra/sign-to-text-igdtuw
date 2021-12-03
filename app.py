from flask import Flask
import Application.py

app = Flask(__name__)

@app.route("/")
def index():
    # return render_template('index.html')
    #your database process here
    send_email_lemay.main()
    return "OK"
    return "Hello World!"
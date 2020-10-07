import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, redirect

import views

app = Flask(__name__)
load_dotenv()

# URL ROUTING
app.add_url_rule('/', view_func=views.home)
app.add_url_rule('/<light>/<value>', view_func=views.light)
app.add_url_rule('/uit/<light>', view_func=views.uit)
app.add_url_rule('/aan/<light>', view_func=views.aan)

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))

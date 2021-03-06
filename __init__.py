from flask import Flask
import os
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy
import ssl

#ctx = ssl.SSLContext()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))


app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


@app.route("/")
def home():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(debug=True)
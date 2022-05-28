

# Sending data from a Flask app to PostgreSQL database

from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

# first create your database on postgres named 'flaskProject'

# set up app.py to connect Postgres database to Flask application.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yourpassword@localhost/flaskProject'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



# After configuring connection to Postgres database through SQLAlchemy, we need to create our 'Cats' table. 
#  consist of a primary key of integer type, a name column that must be unique, and a color column.
#  Both the color and name columns must be entered by the user.

class Cats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(40), unique=True, nullable=False)
    color = db.Column(db.String(80), nullable=False)
    

    def __init__(self, cat_name, color):
        self.cat_name = cat_name
        self.color = color



# To get the information from the user and into the database, we use 
# an HTML form called index.html
@app.route('/')
def home():
    return '<a href="/addperson"><button> Click here </button></a>'


@app.route("/addperson")
def addperson():
    return render_template("index.html")


# When you use parameters with Request.Form, the Web server parses
#  the HTTP request body and returns the specified data. 

@app.route("/personadd", methods=['POST'])
def personadd():
    cat_name = request.form["cat_name"]
    color = request.form["color"]
    entry = Cats(cat_name, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")


if __name__ == '__main__':
    db.create_all()
    app.run()
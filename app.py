import os
import mysql.connector
from flask import Flask, render_template, request


app = Flask(__name__)


if os.environ.get("RAILWAY_ENVIRONMENT"):
    # Railway DB
    db = mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        port=os.environ["DB_PORT"]
    )
else:
    # Local DB
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Manir@2005",
        database="userdb"
    )


cursor = db.cursor()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    mobile = request.form["mobile"]


    query = "INSERT INTO users (name, age, gender, mobile) VALUES (%s, %s, %s, %s)"
    values = (name, age, gender, mobile)
    cursor.execute(query, values)
    db.commit()


    return "Data Saved Successfully!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
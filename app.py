from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="employee_db"
)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])

def save():

    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    salary = request.form['salary']

    cursor = db.cursor()

    sql = """
    INSERT INTO employee
    (name,email,age,salary)
    VALUES(%s,%s,%s,%s)
    """

    val=(name,email,age,salary)

    cursor.execute(sql,val)

    db.commit()

    return "Employee Saved Successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

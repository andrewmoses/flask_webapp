from flask import Flask, render_template, request
import mariadb
app = Flask(__name__)

conn = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="intern_task"
    )

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return "hello world"

@app.route('/signin', methods=['POST'])
def signin():
    cur = conn.cursor()
    cur.execute(
    "SELECT * FROM student WHERE username=?", 
    (request.form['username'],))
    for each in cur:
        if each[1]==request.form['password']:
            # return "name: "+each[2]+" regno: "+each[3]+" dept: "+each[4]+" gender: "+each[6]
            return render_template('student_dash.html', content=each, lg_success=True)
    return render_template('student_dash.html', content='something', lg_success=False)

if __name__ == '__main__':  
   app.run(host='0.0.0.0', debug=True)
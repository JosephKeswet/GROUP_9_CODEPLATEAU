from flask import Flask,render_template, request,url_for
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Joseph'
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)

    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)
    app.run(host='localhost', port=5000)
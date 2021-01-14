from flask import Flask,render_template,request,flash
import pyodbc
app = Flask(__name__)

# @app.route("/")
# def index():
server = 'mbsalesdb.database.windows.net'
database = 'mbsalesdb'
username = 'salesdb'
password = 'Manasa15'
driver = '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 Total FROM supermarket_sales")
        row = cursor.fetchone()
        while row:
            print(str(row[0]))
            row = cursor.fetchone()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index', methods=['GET'])
def date_s():
    start_date = float(request.args['sdate'])
    end_date = float(request.args['edate'])
    result = []
    c = 0
    select="select * from supermarket_sales where " + Date + " between ? and ?"
    # row = cursor.fetchone()
    cur = conn.cursor()
    cur.execute(select, (start_date, end_date))
    rows = cur.fetchall()
    result.append(rows)
    print(result)


   


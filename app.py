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
conn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    # with conn.cursor() as cursor:
    #     cursor.execute("SELECT TOP 3 Total FROM supermarket_sales")
    #     row = cursor.fetchone()
    #     while row:
    #         print(str(row[0]))
    #         row = cursor.fetchone()


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index', methods=['GET'])
def date_s():
    start_date = request.args['sdate']
    print(start_date)
    result = []

    c = 0
    select1 = "select * from supermarket_sales where convert(varchar, Date) = ?"
    # and convert(varchar, Date)>= ?"

    # row = cursor.fetchone()
    cur = conn.cursor()
    cur.execute(select1, (start_date))
    # print(cur)
    rows = cur.fetchall()
    # print(type(rows))

    return render_template('date_range.html', rows=rows, date1=start_date)




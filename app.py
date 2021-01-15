from flask import Flask,render_template,request,flash
import pyodbc
from random import randint

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

@app.route('/insert1', methods=['GET'])
def insert1():
    branch = request.args['branch']
    city = request.args['city']
    ctype = request.args['ctype']
    gender = request.args['gender']
    prod = request.args['prod']
    unit = request.args['unit']
    quantity = request.args['quantity']
    date = request.args['date']
    time = request.args['time']
    pay = request.args['pay']
    rating = request.args['rating']

    tax = float(unit)*float(quantity)*0.05
    total = (float(unit)*float(quantity))+tax
    cogs = float(total) - float(tax)
    gmp = 4.761904762
    gi = tax
    n = 9
    id1 = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
    id = id1[0:3] + "-" + id1[3:5] + "-" +id1[5:9]
    insert1 = "insert into supermarket_sales ( [Invoice ID], Branch, City, [Customer type], Gender, [Product line], [Unit price], Quantity, [Tax 5%], Total, Date, Time, Payment, cogs, [gross margin percentage], [gross income], Rating ) values ( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? )"
    cur = conn.cursor()
    cur.execute(insert1, (id, branch, city, ctype, gender, prod, unit, quantity, tax, total, date, time, pay, cogs, gmp, gi, rating))
    return render_template('insert_data.html')

@app.route('/changemem', methods=['GET'])
def changemem():
    print("new function")
    ii = str(request.args['ii'])
    ctype1 = request.args['ctype1']
    print(ctype1, ii)
    select2 = "select * from supermarket_sales where convert(varchar,[Invoice ID]) = ?"
    cur = conn.cursor()
    cur.execute(select2, ii)
    rows = cur.fetchall()
    print(rows)
    if (len(rows) == 0):
        return render_template('update_data.html', data="Cannot Update query since invoice number was not found.")

    insert1 = "insert into supermarket_sales ( [Invoice ID], Branch, City, [Customer type], Gender, [Product line], [Unit price], Quantity, [Tax 5%], Total, Date, Time, Payment, cogs, [gross margin percentage], [gross income], Rating ) values ( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? )"
    cur3 = conn.cursor()
    cur3.execute(insert1, (rows[0][0], rows[0][1], rows[0][2], ctype1, rows[0][4], rows[0][5], rows[0][6], rows[0][7], rows[0][8], rows[0][9], rows[0][10], rows[0][11], rows[0][12], rows[0][13], rows[0][14], rows[0][15], rows[0][16]))
    # update1 = "update supermarket_sales set [Customer type] = ? where convert(varchar,[Invoice ID])= ?"
    # # and convert(varchar, Date)>= ?"
    #
    # # row = cursor.fetchone()
    # cur5 = conn.cursor()
    # cur5.execute(update1, (ctype1, ii))

    # delete1 = "delete from supermarket_sales where convert(nvarchar,[Customer type]) != ? and convert(varchar,[Invoice ID])= ?"
    # cur5 = conn.cursor()
    # cur5.execute(delete1, (ctype1, ii))

    print("update")
    return render_template('update_data.html', data="The member information was updated to the given invoice.")


# @app.route('/update1', methods=['GET'])
# def update1():
#     ii = request.args['ii']
#     type = request.args['type']
#     print(type,ii)
#     select2 = "select * from supermarket_sales where [Invoice ID]) = ?"
#     cur = conn.cursor()
#     cur.execute(select2, (ii))
#     rows = cur.fetchall()
#     print(rows)
#     if(len(rows)==0):
#         return render_template('update_data.html', data="Cannot Update query since invoice number was not found.")
#
#     update1 = "update supermarket_sales set [Customer type] = ? where [Invoice ID]= ?"
#     # and convert(varchar, Date)>= ?"
#
#     # row = cursor.fetchone()
#     cur5 = conn.cursor()
#     cur5.execute(update1, (type,ii))
#     # print(cur)
#     return render_template('update_data.html', data="The member information was updated to the given invoice.")
#


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    # app.run(debug=True)

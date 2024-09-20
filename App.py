from flask import Flask , render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "flash_message"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'e-waste'


mysql = MySQL(app)

@app.route('/')
def index():
    
    cur = mysql.connection.cursor()
    cur.execute("select * from products")
    data = cur.fetchall()
    cur.close()
    
    return render_template('index.html' , products = data)

@app.route('/insert',methods = ['POST'])
def insert():
    
    flash("Data Inserted Successfully")
    
    if request.method == "POST":
        name = request.form['name']
        quantity = request.form['quantity']
        status = request.form['status']
        hsn = request.form['hsn']
        war = request.form['war']
        dp = request.form['dp']
        inv = request.form['inv']
        di = request.form['di']
        
        cur  = mysql.connection.cursor()
        cur.execute("INSERT INTO products(Description , Quantity , Status , HSN_CODE  , Warranty , DOP , Invoice_Number,DOI) values (%s, %s , %s , %s , %s , %s , %s , %s)",(name , quantity , status , hsn , war , dp , inv , di))
        
        mysql.connection.commit()
        return redirect(url_for('index'))
        


@app.route('/update',methods = ['POST','GET'])


def update():
    
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        status = request.form.get('status')
        hsn = request.form.get('hsn')
        war = request.form.get('war')
        dp = request.form.get('dp')
        inv = request.form.get('inv')
        di = request.form.get('di')
        cur =   mysql.connection.cursor()
        cur.execute("UPDATE products set description = %s , quantity = %s , status = %s , hsn_code = %s , warranty = %s , dop = %s , invoice_number = %s , doi = %s where  id = %s",(name , quantity , status , hsn , war , dp , inv , di , id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])

def delete(id):
    
    flash("Data Deleted  Successfully")
    cur = mysql.connection.cursor()
    cur.execute("delete from products where id = %s" , (id,))
    mysql.connection.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True,port = 5001)
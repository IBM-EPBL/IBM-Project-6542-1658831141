from flask import Flask, render_template,request,redirect,url_for,session
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32536;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ydk44341;PWD=eENReIXIS7xOOBBa",'','')

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register',methods=['GET', 'POST'])
def register():
    session['msg']=""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phno = request.form['phno']
        dob = request.form['dob']
        gender = request.form['gender']
        bloodgroup = request.form['bloodgroup']
        weight = request.form['weight']
        password = request.form['newpassword']
        
        sql = "SELECT * FROM Members WHERE email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        
        if account:
            session['msg']= 'Account already exists'
            return redirect(url_for("login"))  
        else:
            insert_sql = "INSERT INTO Members VALUES (?,?,?,?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, phno)
            ibm_db.bind_param(prep_stmt, 4, dob)
            ibm_db.bind_param(prep_stmt, 5, gender)
            ibm_db.bind_param(prep_stmt, 6, bloodgroup)
            ibm_db.bind_param(prep_stmt, 7, weight)
            ibm_db.bind_param(prep_stmt, 8, password)
            ibm_db.execute(prep_stmt)
            session['msg']= 'Account created Successfully '
            return redirect(url_for("login"))
     
    
    return render_template('register.html') 


@app.route('/login',methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['newpassword']
        
        
        sql = "SELECT * FROM Members WHERE Email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_both(stmt)
        
        accounts=account
        
        
        if (account):
            if  (password == accounts['PASSWORD'] ):
                return render_template('accounts.html',name=account['NAME'])
            else :
                return render_template('login.html',msg='wrong Password')
        else :
            return render_template('login.html',msg='wrong credentials')

            
    else:
        return  render_template('login.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')   

@app.route('/request1',methods=['GET', 'POST'])
def request1():
    session['msg']=""
    if request.method == 'POST':
        patientname = request.form['patientname']
        bloodgroupneeded = request.form['bloodgroupneeded']
        reasonforneed = request.form['reasonforneed']
        hospitalname = request.form['hospitalname']
        hospitaladdress = request.form['hospitaladdress']
        hospitalno = request.form['hospitalno']
        patientgender = request.form['patientgender']
        contactno = request.form['contactno']
        insert_sql = "INSERT INTO Requesters VALUES (?,?,?,?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, patientname)
        ibm_db.bind_param(prep_stmt, 2, bloodgroupneeded)
        ibm_db.bind_param(prep_stmt, 3, reasonforneed)
        ibm_db.bind_param(prep_stmt, 4, hospitalname)
        ibm_db.bind_param(prep_stmt, 5, hospitaladdress)
        ibm_db.bind_param(prep_stmt, 6, hospitalno)
        ibm_db.bind_param(prep_stmt, 7, patientgender)
        ibm_db.bind_param(prep_stmt, 8, contactno)
        ibm_db.execute(prep_stmt)
    return render_template('request.html',msg='Request Placed Successfully')

@app.route('/stats')
def stats():
    return render_template('stats.html')
           
@app.route('/view2')
def view2():
    return render_template('view2.html')   

@app.route('/view')
def view():
    return render_template('view.html')
                 



    
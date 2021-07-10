from flask import Flask,redirect,url_for,render_template,request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "users_data"

mysql = MySQL(app)

@app.route('/')
def home():
    # pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'images.png')
    return render_template("signup.html")

@app.route('/send_message', methods=['GET','POST'])
def send_message(): 

    if request.method == "POST":
        Fname = request.form['Fname']
        Lname = request.form['Lname']
        email = request.form['Email']
        username = request.form['Username']
        gender = request.form['Gender']
        age = request.form['Age']
        bloodgroup = request.form['Bloodgroup']
        number = request.form['Number']
        password = request.form['password']
        confirmpassword = request.form['ConfirmPassword']

        # below cur are used for connection in xampp server running on MySQL
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO register (Fname,Lame,Email,Username,Gender,Age,Bloodgroup,Number,Password,ConfirmPassword) VALUES (%s,%s,%s,%s,%s,%d,%s,%d,%s,%s)",(Fname,Lname,email,username,gender,age,bloodgroup,number,password,confirmpassword))
        mysql.connection.commit()
        cur.close()

        return render_template("",success=success)

if __name__ == '__main__':
    app.run(debug=True)
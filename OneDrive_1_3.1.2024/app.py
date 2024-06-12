from flask import Flask, render_template, request, url_for, redirect, session
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'development_key'  # Set a secret key for development purposes



# hovedsiden
@app.route('/')
def index():
    return render_template('index.html')

# navigerer til login-siden
@app.route('/login', methods=['GET'])
def login2():
    return render_template('login.html')

# poster resultatet fra login (over)
@app.route('/login', methods=['POST'])
def login():
    con = None  # Initialize con to None before the try block
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']

            if username == "admin" and password == "admin":
                return render_template("admin.html")

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("SELECT * from students where username =? and password =?", (username, password))
                result = cur.fetchall()
                if len(result) > 0:
                    msg = "Du er innlogget som " + username
                    session['username'] = username
                    return render_template("success.html", msg=msg)
                else:
                    msg = "Brukernavn eller passord er feil"
                    return render_template("error.html", msg=msg)

        except Exception as e:
            con.rollback()
            msg = f"Feil ved innloggingsoperasjon: {str(e)}"
            return render_template("error.html", msg=msg)
        finally:
            con.close()

# registreringssiden
@app.route('/register', methods=['GET'])
def addrec2():
    return render_template('register.html')

@app.route('/adminList')
def admin_list():
    # Your logic here
    return render_template('adminList.html')

# behandler registreringsskjemaet
@app.route('/register', methods=['POST'])
def addrec():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                # legger til ny data i SQL databasen
                cur.execute("INSERT INTO students (username, password, email) values (?,?,?)", (username, password, email))
                con.commit()
                msg = "Bruker registrert"

        except Exception as e:
            con.rollback()
            msg = f"Feil ved innloggingsoperasjon: {str(e)}"
            return render_template("error.html", msg=msg)
        finally:
            con.close()

@app.route('/success')
def success():
    if 'username' in session:  # Check if user is logged in
        username = session['username']
        print(f"Username from session: {username}")  # Debug print
        con = sql.connect("database.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT email FROM students WHERE username = ?", (username,))
        user = cur.fetchone()
        if user:
            print(f"User email from database: {user['email']}")  # Debug print
            return render_template('success.html', msg='Success!', contact_info=user["email"])
    print("User not logged in")  # Debug print
    return redirect(url_for('login'))  # Redirect to login if not logged in

# lister alle registrerte brukere
@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    # henter alle brukere fra SQL databasen
    cur.execute("select * from students")
    rows = cur.fetchall()
    return render_template('list.html', rows=rows)

if __name__ == "__main__":
    app.run(debug=True)

# lister alle registrerte brukere
@app.route('/adminList')
def adminList():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    return render_template('adminList.html', rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
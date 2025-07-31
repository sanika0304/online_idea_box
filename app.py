from flask import Flask, render_template, request, redirect, session, url_for, flash
import pyodbc
import hashlib
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# SQL Server connection string
conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-56E9GOD\\SQLEXPRESS;'
    'DATABASE=IdeaBoxDB;'
    'UID=sa;PWD=rns11;'
    'TrustServerCertificate=yes;'
)

def get_db_connection():
    return pyodbc.connect(conn_str)

# ---------- Home Page: Login & Register ----------
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'login_email' in request.form:
            email = request.form['login_email']
            password = hashlib.sha256(request.form['login_password'].encode()).hexdigest()

            con = get_db_connection()
            cur = con.cursor()
            cur.execute("SELECT * FROM Users WHERE email=? AND password=?", (email, password))
            user = cur.fetchone()
            con.close()

            if user:
                session['user_id'] = user[0]
                session['name'] = user[1]
                session['role'] = user[4]
                flash("Login successful!", "success")
                return redirect('/admin' if user[4] == 'Admin' else '/submit')
            else:
                flash("Invalid email or password.", "danger")

        elif 'reg_email' in request.form:
            name = request.form['reg_name']
            email = request.form['reg_email']
            role = request.form['reg_role']
            password = hashlib.sha256(request.form['reg_password'].encode()).hexdigest()

            con = get_db_connection()
            cur = con.cursor()
            cur.execute("SELECT * FROM Users WHERE email=?", (email,))
            if cur.fetchone():
                flash("Email already registered.", "warning")
            else:
                cur.execute("INSERT INTO Users (name, email, password, role) VALUES (?, ?, ?, ?)",
                            (name, email, password, role))
                con.commit()
                flash("Registered successfully! You can now log in.", "success")
            con.close()

    return render_template('index.html')

# ---------- Submit Idea ----------
@app.route('/submit', methods=['GET', 'POST'])
def submit_idea():
    if 'user_id' not in session:
        return redirect('/')

    if request.method == 'POST':
        idea_text = request.form['idea_text']
        con = get_db_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO Ideas (user_id, idea_text, submitted_at, status) VALUES (?, ?, ?, ?)",
                    (session['user_id'], idea_text, datetime.now(), 'Viewed'))
        con.commit()
        con.close()
        flash("Idea submitted successfully.", "success")
        return redirect('/my_ideas')

    return render_template('idea.html')

# ---------- View My Ideas ----------
@app.route('/my_ideas')
def my_ideas():
    if 'user_id' not in session:
        return redirect('/')

    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT idea_text, submitted_at, reply_text, status FROM Ideas WHERE user_id=?", (session['user_id'],))
    ideas = cur.fetchall()
    con.close()
    return render_template('my_ideas.html', ideas=ideas)

# ---------- Admin Dashboard ----------
@app.route('/admin')
def admin_dashboard():
    if 'user_id' not in session or session.get('role') != 'Admin':
        return redirect('/')

    con = get_db_connection()
    cur = con.cursor()
    cur.execute("""
        SELECT i.id, i.idea_text, i.submitted_at, i.reply_text, i.status, u.name, u.role
        FROM Ideas i
        JOIN Users u ON i.user_id = u.id
        ORDER BY i.submitted_at DESC
    """)
    ideas = cur.fetchall()
    con.close()
    return render_template('admin_dashboard.html', ideas=ideas)

# ---------- Admin Reply Submission ----------
@app.route('/admin/reply', methods=['POST'])
def admin_reply():
    if 'user_id' not in session or session.get('role') != 'Admin':
        return redirect('/')

    idea_id = request.form['idea_id']
    reply_text = request.form['reply_text']

    con = get_db_connection()
    cur = con.cursor()
    cur.execute("UPDATE Ideas SET reply_text = ? WHERE id = ?", (reply_text, idea_id))
    con.commit()
    con.close()
    flash("Reply submitted successfully.", "success")
    return redirect('/admin')

# ---------- Admin Status Update ----------
@app.route('/admin/status', methods=['POST'])
def admin_status_update():
    if 'user_id' not in session or session.get('role') != 'Admin':
        return redirect('/')

    idea_id = request.form['idea_id']
    status = request.form['status']

    con = get_db_connection()
    cur = con.cursor()
    cur.execute("UPDATE Ideas SET status = ? WHERE id = ?", (status, idea_id))
    con.commit()
    con.close()
    flash("Status updated successfully.", "success")
    return redirect('/admin')

# ---------- About Us ----------
@app.route('/aboutus')
def about():
    return render_template('aboutus.html')

# ---------- Logout ----------
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

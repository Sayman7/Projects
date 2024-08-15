from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///idbase.db"
app.config["SQLALCHEMY_BINDS"] = {"chatbase": "sqlite:///chatbase.db"}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.secret_key = "Conn0/1chat"

class Idtable(db.Model):
    __bind_key__ = None
    __tablename__ = "ids"
    sno = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    password = db.Column(db.String)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form.get("action") == "signup":
            # Handle sign-up
            userid = request.form["number"]
            password = request.form["pass"]
            password_confirm = request.form["pass2"]

            if password != password_confirm:
                flash("Passwords do not match!", "danger")
                return redirect(url_for('index'))

            existing_user = Idtable.query.filter_by(userid=userid).first()
            if existing_user:
                flash("User already exists!", "danger")
                return redirect(url_for('index'))

            # Create new user
            new_user = Idtable(userid=userid, password=password)
            db.session.add(new_user)
            db.session.commit()
            session["id"] = userid  # Store user ID in session
            flash("Sign up successful!", "success")
            return redirect(url_for('send'))

        elif request.form.get("action") == "signin":
            # Handle sign-in
            userid = request.form["userid"]
            password = request.form["password"]

            user = Idtable.query.filter_by(userid=userid, password=password).first()
            if user:
                session["id"] = userid  # Store user ID in session
                flash("Login successful!", "success")
                return redirect(url_for('send'))
            else:
                flash("Invalid credentials, please try again.", "danger")
                return redirect(url_for('index'))

    # Show any flash messages
    return render_template('index.html')

with app.app_context():
    db.create_all(bind_key=None)

class Chattable(db.Model):
    __bind_key__ = "chatbase"
    __tablename__ = "chats"
    sno = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer)
    receiver = db.Column(db.Integer)
    message = db.Column(db.String)

with app.app_context():
    db.create_all(bind_key="chatbase")

@app.route("/post_data", methods=["POST", "GET"])
def send():
    if "id" in session:
        if request.method == "POST":
            chat = Chattable(sender=session["id"], receiver=request.form["rNum"], message=request.form["mess"])
            db.session.add(chat)
            db.session.commit()
            return redirect(url_for('send'))
        return render_template('send.html')
    else:
        return url_security()

@app.route("/posts")
def posts():
    if "id" in session:
        allChats = Chattable.query.all()
        return render_template('display.html', allChats=allChats, id=int(session["id"]))
    else:
        return url_security()

@app.route("/notify")
def notify():
    if "id" in session:
        allChats = Chattable.query.all()
        return render_template('rdisplay.html', allChats=allChats, id=int(session["id"]))
    else:
        return url_security()

def url_security():
    return "Cannot access this page without signup/signin"

@app.route("/logout")
def logout():
    # Clear the session and any flashed messages
    session.pop("id", None)
    flash("You have been logged out.", "info")  # Optionally flash a logout message
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

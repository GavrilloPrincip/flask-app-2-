from flask import Flask, render_template, request, abort, session, redirect, flash
from wtforms import StringField, TextAreaField, PasswordField, Form, validators
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:''@localhost/eablog"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) 




#sigin up formu
class upForm(Form):
    email = StringField(validators=[validators.Email(message="Geçerli bir email adresi giriniz!"), validators.DataRequired(message="boş bırakamazsınız!")])
    username = StringField(validators=[validators.DataRequired(message="Boş bırakamazsınız!"), validators.Length(min=4,max=10, message="4-10 karakter arası giriniz!")])
    password = PasswordField(validators=[validators.Length(min=8,max=16, message="8-16 karakter arası giriniz"), validators.DataRequired("Boş bırakamazsınız!")])
    confirm = PasswordField(validators=[validators.EqualTo(password, message="Parolanız uyuşmuyor")])

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/siginup",methods=["GET", "POST"])
def siginup():
    form = upForm(request.form)
    if request.method == "POST" and form.validate():
        pass
    else:
        return render_template("siginup.html", form = form)
    
        

if __name__ == "__main__":
    app.run(debug=True)

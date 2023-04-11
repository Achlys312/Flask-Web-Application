from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)
 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    data = request.form
    return render_template("sign_up.html")
from flask import Flask, request, redirect, render_template
import jinja2
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


#if my form makes a post request at the route / (as defined in the form in the index page), then go to index again, or welcome page
@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        username = str(request.form['username-actual'])
        password = str(request.form['password-actual'])
        verifiedpassword = str(request.form['verifiedpassword-actual'])
        email = str(request.form['email-actual'])

        #if (not username) or len(username) < 3 or len(username) > 20 or ' ' in username: IGNORE THIS

        #If any of the fields have any of these conditions, fill the error message with the message. otherwise, empty
        
        if username == '' or len(username) < 3 or len(username) > 20 or ' ' in username:
            usererror = "Invalid username lol"
        else:
            usererror = ""

        if password == '' or len(password) < 3 or len(password) > 20 or ' ' in password:
            passworderror = "Invalid password lol"
        else:
            passworderror = ""

        if verifiedpassword != password:
            verifiedpassworderror = "Passwords dont match lol"
        else:
            verifiedpassworderror = ""

        if email == '' or len(email) < 3 or len(email) > 20 or ' ' in email or '@' not in email:
            emailerror = "Invalid email lol"
        else:
            emailerror = ""

    #if all the error messages are empty, render the home page again, with the necessary strings provided for jinja
        if len(usererror) > 0 or len(passworderror) > 0 or len(verifiedpassworderror) > 0 or len(emailerror) > 0:
            return render_template("index.html",usererror=usererror,
                                passworderror=passworderror,
                                verifiedpassworderror=verifiedpassworderror,
                                emailerror=emailerror,
                                username=username,
                                email=email)
        #otherwise, go to the welcome page, with the necessary username
        else:  
            return render_template("welcome.html",username=username) #redirect("/welcome")

@app.route("/welcome", methods=['GET'])
def welcome_page():
    return render_template("welcome.html")

app.run()
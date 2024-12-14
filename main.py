from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "gtg"

@app.route("/")
def Home():
    guessData = db.GetAllGuesses()
    return render_template("index.html", guesses=guessData)

@app.route("/login", methods=["GET", "POST"])
def Login():

    # They sent us data, get the username and password
    # then check if their details are correct.
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Did they provide good details
        user = db.CheckLogin(username, password)
        if user:
            # Yes! Save their username then
            session['username'] = user['username']
            session['id'] = user['id']

            # Send them back to the homepage
            return redirect("/")

    return render_template("login.html")

@app.route("/logout")
def Logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def Register():

    # If they click the submit button, let's register
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Try and add them to the DB
        if db.RegisterUser(username, password):
            # Success! Let's go to the homepage
            return redirect("/")
       
    return render_template("register.html")

##################################
### New code starts here
##################################
@app.route("/add", methods=["GET","POST"])
def Add():
##################################
### New code starts here
##################################
    # Check if they are logged in first
    if session.get('username') == None:
        return redirect("/")
##################################
### New code ends here
##################################

    # Did they click submit?
    if request.method == "POST":
        user_id = session['id']
        date = request.form['date']
        game = request.form['game']
        score = request.form['score']
        comments = request.form['comments']
        # Send the data to add our new guess to the db
        db.AddGuess(user_id, date, game, score, comments)

    return render_template("add.html")


##################################
### New code ends here
##################################
@app.route("/Instructions", methods=["GET"])
def Instructions():
    return render_template ("Instructions.html")

app.run(debug=True, port=5000)
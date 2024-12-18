from flask import Flask, render_template, request, session, redirect
import db
from datetime import date

app = Flask(__name__)
app.secret_key = "mvr"

@app.route("/")
def Home():
    reviewData = db.GetAllReviews()
    return render_template("index.html", reviews=reviewData)

@app.route("/login", methods=["GET", "POST"])
def Login():
    
    """
    The `Login` function in Python handles user login by checking provided credentials and redirecting
    to the homepage if successful.
    :return: The `Login()` function is returning either a redirection to the homepage ("/") if the
    user's login details are correct, or it is rendering the "login.html" template if the request method
    is not POST or if the login details are incorrect.
    """


    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']


        user = db.CheckLogin(username, password)
        if user:

            session['username'] = user['username']
            session['id'] = user['id']


            return redirect("/")

    return render_template("login.html")

@app.route("/logout")
def Logout():
    """
    The `Logout` function clears the session and redirects the user to the homepage.
    :return: The `Logout()` function is returning a redirect response to the root URL ("/").
    """
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def Register():
    """
    The function `Register` handles user registration by capturing username and password from a form
    submission, attempting to add the user to a database, and redirecting to the homepage upon
    successful registration.
    :return: The `Register()` function is returning either a redirect to the homepage ("/") if the user
    registration is successful, or it is rendering the "register.html" template if the request method is
    not POST.
    """

    # If they click the submit button, let's register
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Try and add them to the DB
        if db.RegisterUser(username, password):
            # Success! Let's go to the homepage
            return redirect("/")
       
    return render_template("register.html")

@app.route("/add", methods=["GET","POST"])
def Add():
    """
    The `Add` function checks if the user is logged in, processes form data if the request method is
    POST, and adds a new review to the database.
    :return: The `Add()` function is returning a redirect to the root path ("/") if the session username
    is None. If the request method is POST, it processes the form data and adds a new review to the
    database using the `db.Addreview()` function. Finally, it renders the "add.html" template.
    """

   
    if session.get('username') == None:
        return redirect("/")

    # Did they click submit?
    if request.method == "POST":
        user_id = session['id']
        datet = request.form['date']
        game = request.form['game']
        score = request.form['score']
        comments = request.form['comments']
        # Send the data to add our new review to the db
        #if date is null then current date is used.
        if datet == '':
            datet=date.today()
        db.Addreview(user_id, datet, game, score, comments)

    return render_template("add.html")



@app.route("/Instructions", methods=["GET"])
def Instructions():
    """
    The function `Instructions()` returns a rendered template for an HTML file named
    "Instructions.html".
    :return: The function `Instructions()` is returning a call to
    `render_template("Instructions.html")`, which typically renders an HTML template named
    "Instructions.html".
    """
    return render_template ("Instructions.html")


app.run(debug=True, port=5000)
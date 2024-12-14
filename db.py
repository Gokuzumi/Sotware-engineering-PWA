import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def GetDB():
    """
    The function `GetDB` connects to a SQLite database file named `mvr.db` located in the `.database`
    directory and returns the connection object.
    :return: The function `GetDB()` is returning a connection to a SQLite database located at
    ".database/mvr.db" with row factory set to `sqlite3.Row`.
    """






    db = sqlite3.connect(".database/mvr.db")
    db.row_factory = sqlite3.Row

    return db

def GetAllReviews():
    """
    The function `GetAllReviews` retrieves all reviews from a database, including the date, game, score,
    username of the reviewer, and comments, and returns the data sorted by date in descending order.
    :return: The GetAllReviews function returns a list of tuples, where each tuple contains the
    following information for a review: date, game, score, username of the user who posted the review,
    and comments. The reviews are ordered by date in descending order.
    """
    #
    db = GetDB()
    reviews = db.execute("""SELECT Reviews.date, Reviews.game, Reviews.score, Users.username, Reviews.comments
                            FROM Reviews JOIN Users ON Reviews.user_id = Users.id
                            ORDER BY date DESC""").fetchall()
    db.close()
    return reviews

def CheckLogin(username, password):
    """
    The function `CheckLogin` checks if a user exists in the database and if the provided password
    matches the stored password for that user.
    
    :param username: The `CheckLogin` function you provided is a Python function that checks if a user
    with the given `username` exists in the database and if the provided `password` matches the stored
    password for that user. If both conditions are met, it returns the user details; otherwise, it
    returns `None
    :param password: The function `CheckLogin` takes two parameters, `username` and `password`. It
    retrieves user information from a database based on the provided `username`. If the user exists and
    the password matches the hashed password stored in the database, it returns the user details.
    Otherwise, it returns `None`
    :return: If the username and password are correct, the function will return the user details. If the
    username or password is incorrect, it will return None.
    """

    db = GetDB()


    user = db.execute("SELECT * FROM Users WHERE username=?", (username,)).fetchone()


    if user is not None:
        
        if check_password_hash(user['password'], password):
            
            return user
       
    
    return None

def RegisterUser(username, password):

    
    if username is None or password is None:
        return False

   
    db = GetDB()
    hash = generate_password_hash(password)
    db.execute("INSERT INTO Users(username, password) VALUES(?, ?)", (username, hash,))
    # `db.commit()` is a method in SQLite that is used to commit the current transaction in the
    # database. When you make changes to the database (such as inserting, updating, or deleting
    # records), those changes are not immediately saved to the database file. Instead, they are kept
    # in a transaction buffer.
    db.commit()

    return True


def Addreview(user_id, date, game, score, comments):
    """
    The function `AddGuess` inserts a user's review for a game into a database table.
    
    :param user_id: The `user_id` parameter is used to identify the user who is submitting the guess. It
    is typically a unique identifier for each user in the system
    :param date: The `date` parameter is typically a timestamp or date value representing when the guess
    or review was made. It could be in a specific format like "YYYY-MM-DD" or a timestamp format
    depending on the database schema and requirements
    :param game: The `game` parameter in the `AddGuess` function represents the name or title of the
    game for which the user is submitting a review or guess. It is a required parameter for adding a
    guess to the database
    :param score: The `score` parameter in the `AddGuess` function represents the rating or score given
    by the user for a particular game. It is a numerical value that typically indicates the user's
    evaluation or opinion of the game's quality, performance, or overall experience. The score can be
    based on a predefined
    :param comments: Comments is a parameter that allows the user to provide additional feedback or
    information about their guess for a game. It can include any thoughts, opinions, or details that the
    user wants to share related to their experience with the game
    :return: The function `AddGuess` will return `True` if the `date` and `game` parameters are not
    `None` and the guess is successfully added to the database. Otherwise, it will return `False`.
    """
   
   
    if date is None or game is None:
        return False
   
    # Get the DB and add the guess
    db = GetDB()
    db.execute("INSERT INTO Reviews(user_id, date, game, score, comments) VALUES (?, ?, ?, ?, ?)",
               (user_id, date, game, score, comments))
    db.commit()

    return True


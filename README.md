# Movie Review PWA
This is a PWA where the user can Register an account, login and write reviews as well as see other user's reviews.

### Prerequisites
 Lists : 
 - **List 1** :
 Backend: Python Flask

Database: SQLite

Frontend: HTML, CSS, JavaScript

PWA Integration: Service workers for offline support

### Installing
Clone the repository:

git clone https://github.com/Gokuzumi/Sotware-engineering-PWA.git

cd movie-review-pwa

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Initialize the database:

python models.py

Run the application:

python app.py

Open your web browser and navigate to http://127.0.0.1:5000/.

Key Files

## Backend

app.py: Contains the Flask routes and application logic.

models.py: Defines the SQLite database schema and initialization script.

## Frontend

templates/: HTML templates for the app.

static/css/styles.css: Contains styles for the app.

static/js/app.js: Handles client-side interactions.

PWA Integration



## Usage
Register and Make an acount if you don't have one already.
To add a review Log in then click on the "Add Review" button and enter out the details.
Log out when session is finished.

## Acknowledgments
Inspired by Guess the game.db by Daniel Yew Boon Phua. 

    Big thanks to Mr. Daniel Yew Boon Phua.🙏
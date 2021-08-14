from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

import random 	# import the random module
random_int = random.randint(1, 100) # random number between 1-100

app.secret_key = 'super secret key'

@app.route('/')
def index():
    #set the random integer if it is not in session. set current guesses if they have not already been defined. set leaderboard if it has not been defined.
    if not 'random_int' in session:
        session['random_int'] = random.randint(1,100)

    #set this so that current_guesses is being stored in session
    if not 'current_guesses' in session:
        session['current_guesses'] = 0

    #set the leaderboard to an array if it is not already defined
    if not 'leaderboard' in session:
        session['leaderboard'] = []

    
    print(session)

    return render_template("index.html")


@app.route('/guess_number', methods=['POST'])
def guess_number():

    #turn the integer from the request.form into a session variable 
    session['guess'] = int(request.form['guess'])

    #Current guesses will increase by one anytime the submit button is pressed. Will not increase if the page is refreshed.
    if request.form['guess']: 
        session['current_guesses'] += 1


    return redirect("/")




@app.route('/add_to_leaderboard', methods=['POST'])
def add_to_leaderboard():
    # append winner info to the 'leaderboard' session. sorted the leaderboard by the second value in each list in the list so that the leaderboard can be sorted by place on the html side
    session['leaderboard'].append([request.form['leaderboard'], session['current_guesses']])
    session['leaderboard'].sort(key = lambda x: x[1])

    #calls on the reset session function
    reset_session()
    return redirect("/")


@app.route('/destroy_session', methods=['POST'])
def reset_session():

    #reset the current session information 
    session.pop('guess')
    session.pop('current_guesses')
    session.pop('random_int')
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


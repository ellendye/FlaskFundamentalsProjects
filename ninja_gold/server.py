from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'super secret key'

import random
import datetime

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session: 
        session['activities'] = []
    if not 'moves' in session: 
        session['moves'] = 0

    return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def process_money():
    timestamp = datetime.datetime.now()
    if request.form['building'] == 'farm':
        gold = random.randint(10,20)
        session['gold'] += gold
        session['activities'].append(f'Earned {gold} golds from the farm! {timestamp}')
        session['moves'] += 1
    elif request.form['building'] == 'cave':
        gold = random.randint(5,10)
        session['gold'] += gold
        session['activities'].append(f'Earned {gold} golds from the cave! {timestamp}')
        session['moves'] += 1
    elif request.form['building'] == 'house':
        gold = random.randint(2,5)
        session['gold'] += gold
        session['activities'].append(f'Earned {gold} golds from the house! {timestamp}')
        session['moves'] += 1
    elif request.form['building'] == 'casino':
        session['moves'] += 1
        gold = random.randint(10,20)
        operator = random.randint(1,2)
        if operator == 1:
            session['gold'] += gold
            session['activities'].append(f'Earned {gold} golds from the Casino! {timestamp}')
        else:
            session['gold'] -= gold
            session['activities'].append(f'Entered a casino and lost {gold} golds.. Ouch.. {timestamp}')

    


    return redirect("/")


@app.route('/destroy_session', methods=['POST'])
def reset_session():

    #reset the current session information 
    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'super secret key'


@app.route('/')
def index():
    #setting the number of visits to 0 if the session has been cleared
    if not 'visits' in session: 
        session['visits'] = 1
    else:
        session['visits'] += 1

    return render_template("index.html")

    
@app.route('/number_of_visits', methods=['POST'])
def add_two():
    #adding in the increment for the +2 button. the page automatically adds 1 when refreshed, only adding one here and that will add two altogether. 
    #Added an if/else statement to determine if it would add 2 for the add 2 button or add a custom number depending on what was entered for the custom button
    if request.form['visits'] == 'add_two':
        session['visits'] += 1
    else:
        session['visits'] += (int(request.form['visits'])-1)
    return redirect("/")

@app.route('/destroy_session', methods=['POST'])
def reset_session():
    #reset the current session
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hello_name(name):
    return 'Hello ' + str(name)

@app.route('/repeat/<num>/<word>')
def pattern_and_function(num,word):
    return f'{str(word)} \n'*int(num)

@app.route('/<path:path>')
def undefined(path):
    path = "Sorry! No response. Try again"
    return path

if __name__=="__main__":  
    app.run(debug=True)
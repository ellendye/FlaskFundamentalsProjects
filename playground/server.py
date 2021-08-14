from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def playground():
    return render_template('index.html', times=3, backgroundcolor='cornflowerblue')

@app.route('/play/<int:num>')
def playground_add_boxes(num):
    return render_template('index.html', times=num, backgroundcolor='cornflowerblue')

@app.route('/play/<int:num>/<string:color>')
def playground_add_boxes_and_color(num, color):
    return render_template('index.html',times=num, backgroundcolor=color)


if __name__=="__main__":
    app.run(debug=True)
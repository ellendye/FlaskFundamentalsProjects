from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def generate_checkerboard():
    return render_template('index.html', boardlength=8, boardwidth=8, color1='black', color2='red')


@app.route('/<int:width>')
def generate_checkerboard_custom_width(width):
    return render_template('index.html', boardlength=8, boardwidth=width, color1='black', color2='red')

@app.route('/<int:width>/<int:length>')
def generate_checkerboard_custom_width_and_length(length,width):
    return render_template('index2.html', boardlength=length, boardwidth=width, color1='black', color2='red')

@app.route('/<int:width>/<int:length>/<string:color_one>/<string:color_two>')
def generate_checkerboard_custom_width_length_color(length,width,color_one,color_two):
    return render_template('index2.html', boardlength=length, boardwidth=width, color1=color_one, color2=color_two)


if __name__=="__main__":
    app.run(debug=True)
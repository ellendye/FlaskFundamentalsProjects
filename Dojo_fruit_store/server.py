from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form


@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    number_of_items=0
    for k,v in request.form.items():
        if k == 'strawberry' or k == 'apple' or k == 'blackberry' or k == 'raspberry':
            number_of_items += int(v)
    print(f'Charging {request.form["first_name"]} {request.form["last_name"]} for {number_of_items} fruit(s)')
    return render_template("checkout.html", student_data=request.form,number_of_items=number_of_items)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")



if __name__ == "__main__":
    app.run(debug=True)
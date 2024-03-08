from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=['POST'])
def calculate():
    number_1 = request.form.get('number_1', type=int)
    number_2 = request.form.get('number_2', type=int)
    operation = request.form.get('operation')

    if(not number_1 or not number_2):
        return jsonify({'error': 'Please enter values for both numbers.'}), 400

    result = 0

    if operation == "Addition":
        result = number_1 + number_2
    elif operation == "Subtraction":
        result = number_1 - number_2
    elif operation == "Multiplication":
        result = number_1 * number_2
    elif operation == "Division":
        result = number_1 / number_2
    else:
        pass
    
    return render_template("result.html", result=result)

if __name__ == '__main__':  
   app.run(debug=True)
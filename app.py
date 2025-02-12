from flask import Flask, render_template, request, redirect, url_for, jsonify.

## Creating a simple Flask application.
#Variable 'app' to denote the class flask, __ denotes the entry point in the program.

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route("/htmlH1", methods=["GET"])
def header():
    return "<h1> This is the Header tag page </h1>"

#Variable rule.
@app.route('/success/<float:score>', methods=["GET"])
def success(score):
    return """
        <html>
            <head>
                <style>
                    body {
                        background-color: black;
                        color: white;
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1 style='color: green;'> Status: PASSED </h1>
                <h3> Score: """ + str(score) + """  </h3>
            </body>
        </html>
    """

@app.route('/fail/<float:score>', methods=["GET"])
def fail(score):
    return """
        <html>
            <head>
                <style>
                    body {
                        background-color: black;
                        color: white;
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1 style='color: red;'> Status: FAILED </h1>
                <h3> Score: """ + str(score)+ """ </h3>
            </body>
        </html>
    """


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        
        average_score = ((science + maths + history)/3)
        
        res = ""
        
        if average_score >= 45:
            res = "success"
        else:
            res = "fail"
        return redirect(url_for(res, score=average_score))


#Creating a test API with 3 values as A, B and C.
#Values are defined in JSON file names test.json.
#API testing done via Postman.

@app.route('/api', methods=["POST"])
def calculateSum():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    c_val = float(dict(data)['c'])
    return jsonify(a_val + b_val + c_val)


if __name__ == "__main__":
    app.run(debug=True) #Do debug=True to keep running the flask server.
    

from flask import Flask, redirect, url_for, render_template, request
###Creates a WSGI application -> Comm between the web server and the web application.
app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/pass/<int:score>')
def passed(score):
    return render_template('passed.html', score = score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('failed.html', score = score)

@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if(marks >= 40):
        result = 'passed'
    if(marks < 40):
        result = 'fail'
    
    return redirect(url_for(result, score=marks))

### Submitting the form using HTTP methods.
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        math = float(request.form['math'])
        SST = float(request.form['social'])
        
        total_score = (science + math + SST)/4
        return redirect(url_for('result', marks = int(total_score)))

@app.route('/toHtmlGoogle', methods=['GET'])
def displayHTML():
    return render_template('tempJmpGoogle.html')

@app.route('/redirectTGoogle')
def toGoogle():
    return redirect('https://www.google.com')

@app.route('/redirectToGithub')
def toGithub():
    return redirect('https://www.github.com')


if __name__ == '__main__':
    app.run(debug = True)

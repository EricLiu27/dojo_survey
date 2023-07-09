from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = "display info"


@app.route('/')
def hello_world():

    return render_template("index.html")



@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    data = {**request.form}
    print(data)
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['comment'] = request.form['comment']
    session['receive_emails'] = request.form['receive_emails']
    session['reach'] = request.form['reach']
    
    return redirect("/result")

@app.route('/result')
def display():
    return render_template('display.html')

if __name__ == "__main__":
    app.run(debug=True)
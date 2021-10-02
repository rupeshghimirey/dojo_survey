from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

app.secret_key = "asdsadsd"


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add_form", methods = ['POST'])
def submitForm():
    print(request.form)

    survey = {
        "full_name" : request.form['full_name'],
        "dojo_location" : request.form['dojo_location'],
        "dojo_language" : request.form['dojo_language'],
        "comments" : request.form['comments']
    }
    session['survey'] = survey;
    session['full_name'] = survey['full_name']
    print(session)
    return redirect('/result')

@app.route('/result')
def result():
    fullName = session['survey']['full_name']
    dojoLocation = session['survey']['dojo_location']
    dojoLanguage = session['survey']['dojo_language']
    comments = session['survey']['comments']
    return render_template('result.html', fullName = fullName, dojoLocation = dojoLocation, 
    dojoLanguage = dojoLanguage, comments = comments)


if __name__=="__main__":
    app.run(debug=True)

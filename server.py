from flask import Flask, render_template, redirect, request, flash
from dojo import Dojo
app = Flask(__name__)
app.secret_key = "asdsadssad"


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add_form", methods = ['POST'])
def create_dojo():

    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    
    
    data = {
        "name": request.form["name"],
        "location" : request.form["dojo_location"],
        "language" : request.form["dojo_language"],
        "comments" : request.form["comments"],
        
    }
    Dojo.save(data)

    flash("Form data submitted to database")
    return redirect('/result')



@app.route('/result')
def submitted_info():

    list_of_all_dojos = Dojo.get_all_dojos()

    return render_template("result.html", list_of_all_dojos = list_of_all_dojos)




if __name__=="__main__":
    app.run(debug=True)

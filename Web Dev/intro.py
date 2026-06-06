from flask import Flask, render_template,request,flash,jsonify

app = Flask(__name__,static_folder="assets",static_url_path="/files")
app.secret_key="shreyas"
@app.route('/index')
def index():
    # name="Shreyas"
    # surname="Pawar"
    Qualifications="Pursuing B.Tech"
    marks=[78,78,79,79,80,90,86,88,70]
    footer="<p>All Rights Reserved! 2026<p>"

    name=request.args.get('name', default="User")
    surname=request.args.get('surname', default=" ")
    lang=request.args.get('lang', default=" ")
    print(f"Name: {name} {surname} Qualifications are {Qualifications} Marks {marks} and learns {lang}" )
    return render_template("index.html", name=name, surname=surname, qualifications=Qualifications ,marks=marks,lang=lang,footer=footer)

@app.route('/contact')
def contact():
    flash("List of COntact")
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/form', methods=["GET","POST"])
def form():
    if request.method=="POST":
        email=request.form["Email"]
        password=request.form["Password"]
        print(f"Thanks for Logged In your email is {email} and password is {password}")
        return "<b> Thanks For Logged In!<b>"
    return render_template("form.html")

@app.route('/api')
def api():
    #Some Machine Learning Model
    data={"Input":31,"Output":28,"Accuray":92.53}
    return jsonify(data),400

if __name__ == '__main__':
    app.run(debug=True)
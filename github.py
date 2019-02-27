from flask import Flask,render_template,request
import requests

app = Flask(__name__)
baseUrl = "https://api.github.com/users/"

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        githubname = request.form.get("githubname")
        responseUser = requests.get(baseUrl + githubname)
        responseRepos =requests.get(baseUrl + githubname + "/repos")

        userInfo = responseUser.json()
        userRepos = responseRepos.json()

        if "message" in userInfo:
            return render_template("index.html", error = "Kullanici Bulunamadi")
        else:    
            return render_template("index.html", profile = userInfo , repos = userRepos) 
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


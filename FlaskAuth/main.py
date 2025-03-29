from flask import Flask, render_template,request, jsonify, redirect, url_for
import json

app = Flask(__name__)


#Loading the data into flask.
def load_users():
    with open("data.json", "r") as file:
        return json.load(file)["users"]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.json  #Requesting json format.
    username = data.get("username")
    password = data.get("password")
    
    users = load_users()
    
    for user in users:
        if user["username"] == username and user["password"] == password:
            return jsonify({"redirect": url_for("afterlogin")})
        
        ## url_for sends the function name.
        ## then the js code checks for the redirect word.
        ## If yes then it redirects to the key (afterlogin).
        
        
    return jsonify({"message": "Invalid credentials"})

            
            
@app.route("/nextPage")
def afterlogin():
    return render_template("afterlogin.html")



if __name__ == "__main__":
    app.run(debug = True)
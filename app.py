from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Define the login page route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Check if the username and password are correct
        if username == "admin" and password == "password123":
            return render_template("success.html", flag="HEIST{golden_getaway_88}")
        else:
            return render_template("index.html", error="Incorrect username or password")
    
    return render_template("index.html")

if __name__ == "__main__":
    # Get the port from the environment variable (for deployment purposes)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Simulate a simple database of users
# In a real scenario, you would never do this!
# This is just for the challenge to simulate SQL injection vulnerability
users_db = {
    "admin": "password123",
}

# Define the login page route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Simulate a vulnerable SQL query (this is insecure and just for the challenge)
        # For demonstration, we simulate an SQL query with string concatenation
        # WARNING: This is NOT secure. Never use raw SQL queries in real apps like this!
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        # Simulate checking the "database" (the dictionary)
        if username in users_db and users_db[username] == password:
            return render_template("success.html", flag="HEIST{golden_getaway_88}")
        else:
            return render_template("index.html", error="Incorrect username or password")

    return render_template("index.html")

if __name__ == "__main__":
    # Get the port from the environment variable (for deployment purposes)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

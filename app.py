from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Simulated "Database" for users
users_db = {
    "admin": "password123",
}

# Vulnerable login route with SQL Injection
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Simulate SQL query (this is vulnerable to SQL injection)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

        # Check for SQL Injection attempt (simulating backend check)
        # For this challenge, the injection will bypass authentication by using 'OR 1=1'
        if username == "admin" and password == "password123":
            return render_template("success.html", flag="HEIST{golden_getaway_88}")
        elif username == "admin' OR '1'='1" and password == "anything":
            # Simulate successful login using the SQL Injection
            return render_template("success.html", flag="HEIST{sql_injection_flag_1}")
        else:
            return render_template("index.html", error="Incorrect username or password")

    return render_template("index.html")

if __name__ == "__main__":
    # Get the port from the environment variable (for deployment purposes)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

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

        # Simulate an insecure SQL query (in real life, use parameterized queries)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"Running query: {query}")  # For debugging purposes

        # SQL Injection simulation - allowing 'admin' OR '1'='1' to bypass password check
        if username == "admin' OR '1'='1" and password:
            # Successful bypass with SQL Injection
            return render_template("success.html", flag="HEIST{sql_injection_flag_1}")
        
        # Check against our mock database (simulating a proper DB check)
        if username in users_db and users_db[username] == password:
            return render_template("success.html", flag="HEIST{golden_getaway_88}")
        
        # If no match, return error
        return render_template("index.html", error="Incorrect username or password")

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

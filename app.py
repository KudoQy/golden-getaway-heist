from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Simulated "Database" for users
users_db = {
    "admin": "password123",
    "user": "securepass"
}

# Vulnerable login route with SQL Injection
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # --- SIMULATED SQL INJECTION VULNERABILITY ---
        # This section simulates how a real SQL database would interpret
        # common SQL Injection bypasses, specifically those that make the
        # WHERE clause always TRUE and comment out the rest of the query.

        # In a real vulnerable app:
        # query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        # The database would then parse and execute 'query'.

        # Here, we simulate the effect of the database parsing this vulnerable query.
        
        sql_bypass_detected = False
        
        # Define common truthy SQL conditions that attackers might use
        truthy_conditions = [
            "1=1",
            "'1'='1'",
            "TRUE",
            "2>1", # Example: another truthy condition
            "1=2 OR 1=1" # Example: a more complex truthy condition
        ]

        # Define common SQL comment delimiters
        comment_delimiters = ["--", "#"] # -- for SQL standard, # for MySQL

        # Check for injection pattern: <any_string>' OR <truthy_condition><comment_delimiter>
        # This simulates the attacker closing the string, adding an OR TRUE, and commenting out the rest.
        for condition in truthy_conditions:
            for comment_char in comment_delimiters:
                # We expect the payload to close the initial quote, then introduce OR condition, then comment
                # Example: ' OR 1=1--
                # The ' OR ' must be present to make it an OR injection.
                
                # Check for pattern: single_quote + ' OR ' + condition + comment_char
                # The condition might have leading/trailing spaces before the comment.
                potential_payload = f"' OR {condition}{comment_char}"
                
                if potential_payload in username:
                    # Further check if the comment char is indeed at the end of the effective payload
                    # This prevents partial matches like "something' OR 1=1--notcommented"
                    # We check if the comment character is at the end of the matched sequence in the username
                    
                    # Find the index of the comment char in the matched part
                    comment_idx_in_username = username.find(comment_char, username.find(potential_payload))
                    
                    if comment_idx_in_username != -1:
                        # Ensure no more relevant SQL syntax after the comment (e.g., another ' AND ')
                        # This is a simplification; real SQL parsers are more complex.
                        # We'll just assume if the comment char is found, the rest is ignored.
                        sql_bypass_detected = True
                        break # Found a bypass, no need to check other conditions/comments
            if sql_bypass_detected:
                break # Found a bypass, no need to check other conditions/comments

        # If an SQL Injection bypass pattern is detected, grant the SQLi flag
        # For a real SQLi, the password input wouldn't matter if the username injection is successful.
        # So, we only need to check if the username payload triggered the bypass.
        if sql_bypass_detected:
            return render_template("success.html", flag="HEIST{SQLi_Auth_Bypass_Real_Sim}")

        # --- Original database check (for 'admin':'password123' without injection) ---
        # This is where legitimate logins (and potential brute-force if not rate-limited) would occur.
        if username in users_db and users_db[username] == password:
            return render_template("success.html", flag="HEIST{golden_getaway_88}")
        
        # If no match for either legitimate login or SQLi bypass, return error
        return render_template("index.html", error="Incorrect username or password")

    return render_template("index.html") # Render the login form for GET requests

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

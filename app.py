from flask import Flask, request

app = Flask(__name__)

FLAG = "flag{you_found_the_flag}"

@app.route("/")
def index():
    return '''
        <h2>Welcome to the CTF Challenge</h2>
        <form method="GET" action="/check">
            <input name="input" placeholder="Enter a secret..." />
            <button type="submit">Submit</button>
        </form>
    '''

@app.route("/check")
def check():
    user_input = request.args.get("input", "")
    if user_input == "admin":
        return f"Correct! Here is your flag: {FLAG}"
    return "Try again."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

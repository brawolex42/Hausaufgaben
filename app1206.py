from flask import Flask

app = Flask(__name__)

users = {1: "Alice", 2: "Bob", 3: "Charlie"}

@app.route('/')
def index():
    return "Welcome to the user API! Try /user/1 or /user/Charlie"

@app.route('/user/<int:user_id>')
def get_user_by_id(user_id):
    name = users.get(user_id)
    return name if name else "User not found"

@app.route('/user/<name>')
def get_user_by_name(name):
    for user_id, username in users.items():
        if username.lower() == name.lower():
            return f"{username} (ID: {user_id})"
    return "User not found"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Log credentials to console for educational demo (never do this in real life!)
    print(f"Captured credentials: {username} / {password}")
    return "This was a demo. Credentials captured for lab purpose only."

if __name__ == '__main__':
    app.run(debug=True)
  

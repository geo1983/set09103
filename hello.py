from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/private")
def private():
  #  Test for user logged failed
  #  so redirect to login URL
  return redirect(url_for('login'))

@app.route('/login')
def login():
  return "Now we would get username $ pass"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


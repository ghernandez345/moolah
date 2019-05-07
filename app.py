from flask import Flask, render_template
app = Flask(__name__)

client_id = 'oauth2client_00009gPEfPRsJ7pcPHo16f'
redirect_uri = 'http://localhost:5000/oauth/callback'

@app.route('/')
def login():
  return render_template('login.html')

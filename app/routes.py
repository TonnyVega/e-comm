from flask import flash, render_template, request, url_for
from app import app

from app.models import User

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    
    users = User.query.all()  
    return render_template('home.html', users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login.html', title='login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  return render_template('signup.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
  return render_template('profile.html')

@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
  return render_template('purchase.html')


@app.route('/item', methods=['GET', 'POST'])
def product():
  return render_template('item.html')

@app.route('/payment', methods=['GET', 'POST'])
def make_payment():
  return render_template('payment.html')
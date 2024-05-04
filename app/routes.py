from flask import flash, render_template, request, url_for, redirect
from flask_login import current_user, login_user
from app import app, db, bcrypt

from app.models import User
from app.forms import LoginForm, Signup_form

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    
    users = User.query.all()  
    return render_template('home.html', users=users)


# Sign up and login
@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form =LoginForm()
  if form.validate_on_submit():
    user= User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember= form.remember.data)
      next_page = request.args.get('next')
      flash(f'Welcome back.', 'success')
      return redirect(next_page) if next_page else redirect(url_for('home'))
    else:
      flash('Login unsuccessful, please enter the correct email or password', 'danger')
  return render_template('login.html', title='login', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = Signup_form()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email= form.email.data, password= hashed_password)
    db.session.add(user)
    db.session.commit()
    
    flash(f'Your account has been created. You can now login as{form.username.data}', 'success')
    return redirect(url_for('home'))
  else:
    return render_template('signup.html', title='Sign Up', form=form)



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
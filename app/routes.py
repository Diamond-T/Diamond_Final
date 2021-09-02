from app import app,db
from flask import render_template,redirect,url_for,flash,request,session, url_for
from app.forms import LoginForm, register
from app.models import User
from flask_login import current_user, login_user,login_required, logout_user,current_user
from app.models import User



@app.route('/')
def main_page ():
    return render_template('index.html')

@app.route('/signup')
def signup():
    form = register()
    if form.validate_on_submit():
        # Grab data from our submitted form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)
        # Create new instance of User
        new_user = User(username, email, password)

        # Add new_user to our database
        db.session.add(new_user)
        db.session.commit()

        # Once new_user is added to db, flash success message
        flash(f'Thank you for signing up {new_user.username}!', 'danger')

        # Redirect user back to home page
        return redirect(url_for('index'))

        
    return render_template('signup.html', title='Register for CT Blog', form=form)

 
   
    









@app.route('/Login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            flash('Incorrect Username/Password. Please try again!', 'danger')
            return redirect(url_for('login'))
        
        login_user(user)
        flash('You have succesfully logged in!', 'success')
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary')
    return redirect(url_for('index'))
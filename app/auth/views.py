from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from ..models import Community
from .forms import RegistrationForm, LoginForm
from .. import db
from . import auth


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        community = Community(username=form.username.data,
                              email=form.email.data,
                              password=form.password.data
                              )
        db.session.add(community)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = 'Create Account'
    return render_template('auth/register.html',
                           registration_form=form,
                           title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Community.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Uzalendo"
    return render_template('auth/login.html', login_form=login_form,
                           title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))

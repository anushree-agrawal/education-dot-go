from flask import Flask, redirect, url_for, session, request, render_template
from flask_oauth import OAuth
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import json

class MyForm(FlaskForm):
    login = SubmitField('Login', validators=[DataRequired()])
    #button = SubmitField("button")

SECRET_KEY = 'development key'
DEBUG = True
FACEBOOK_APP_ID = '188477911223606'
FACEBOOK_APP_SECRET = '621413ddea2bcc5b2e83d42fc40495de'


app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)

@app.route('/', methods=('GET', 'POST'))
def index():
    form = MyForm()
    if form.validate_on_submit():
        #return redirect('/success')
        return redirect(url_for('login'))
    else:
        return render_template('index.html', form=form)



@app.route('/login')
def login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))


@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    messages = json.dumps({"name":me.data["name"]})
    session['me'] = messages
    return redirect(url_for('logged_in'))

@app.route('/logged_in', methods=('GET', 'POST'))
def logged_in():
    return render_template('logged_in.html', me=json.loads(session['me']))

@app.route('/thanks', methods=('GET', 'POST'))
def thanks():
    return render_template('thanks.html', me=json.loads(session['me']))


@app.route('/showprog', methods=('GET', 'POST'))
def showprog():
    return render_template('showprog.html', me=json.loads(session['me']))

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')


if __name__ == '__main__':
    app.run()


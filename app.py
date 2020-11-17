from flask import Flask, session, render_template, url_for, request, redirect
from form import registerForm

app = Flask(__name__)
app.config['SECRET_KEY']='fkbvjfbvjrekhvjhghyhvyhbejkr'


@app.route('/')
def hello():
    return '<p>hi</p>'

@app.route('/register', methods=["GET", "POST"])
def reg():
    registerp1 = registerForm()
    name = None
    if registerp1.validate_on_submit():
        session['name'] = registerp1.name.data
        session['surname'] = registerp1.surname.data
        name = registerp1.name.data
        return redirect(url_for('trial'))
    return render_template('register.html',registerp1=registerp1, name=name)

@app.route('/trial')
def trial():
    if session.get('name'):
        return render_template('trial.html')
    else:
        return redirect(url_for('hello'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect('reg')

if __name__ == '__main__':
    app.run(debug=True)

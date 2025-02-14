from flask import Flask, render_template , url_for
from form import CompanyAccount , CandidateAccount, CompanyAccount2 , CandidateAccount2
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'G528JYFYJKSDGFKWRL57'

@app.route('/')
def home():
    return render_template('home.html',title="home")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/partnership')
def partnership():
    return render_template('partnership.html')

@app.route('/pricing')
def pricing():
    return render_template('pricingplan.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signuporloginascandidate')
def signuporloginascandidate():
    return render_template('signuporloginascandidate.html')

@app.route('/candidateaccount',methods=['GET', 'POST'])
def candidateaccount():
    form = CandidateAccount()
    return render_template('candidateaccount.html', form = form)

@app.route('/signuporloginascompany')
def signuporloginascompany():
    return render_template('signuporloginascompany.html')

@app.route('/companyaccount', methods=['GET', 'POST'])
def companyaccount():
    form = CompanyAccount()
    return render_template('companyaccount.html', form = form)

@app.route('/companyaccount2' , methods=['GET', 'POST'])
def companyaccount2():
    form = CompanyAccount2()
    return render_template('companyaccount2.html',form = form)

@app.route('/candidateaccount2', methods=['GET', 'POST'])
def candidateaccount2():
    form = CandidateAccount2()
    return render_template('candidateaccount2.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)

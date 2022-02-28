from flask import Flask, render_template, session, redirect,request
import random

app = Flask(__name__)

app.secret_key="It was Me!"

@app.route('/')
def index():
    if 'gold_total' not in session:
        session['gold_total'] = 0
        session['gold_num'] = 0
        session['moves'] = 0
        session['activities'] = []
        list = session['activities']  
    return render_template("index.html")

@app.route('/process_money', methods = ['POST'])
def play():
    if session['moves'] < 15 and session['gold_total'] < 500:
        if request.form['ninja_form'] == 'farm':
            num = random.randint(10,20)
            session['gold_total']+=num
            session['gold_num']=num
            number = session['gold_num']
            session['moves'] += 1
            return redirect('/')
        elif request.form['ninja_form'] == 'cave':
            num = random.randint(5,10)
            session['gold_total']+=num
            session['gold_num']=num
            session['moves'] += 1
            return redirect('/')
        elif request.form['ninja_form'] == 'house':
            num = random.randint(2,5)
            session['gold_total']+=num
            session['gold_num']=num
            session['moves'] += 1
            return redirect('/')
        elif request.form['ninja_form'] == 'casino':
            num = random.randint(0,50)
            session['gold_total']+=num
            session['gold_num']=num
            value = session['gold_num']
            session['moves'] += 1
        return redirect('/')
    else:
        session.clear()
        return redirect('/')
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
    

if __name__=="__main__":
    app.run(debug=True)
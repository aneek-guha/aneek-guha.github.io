from flask import Flask, render_template, request
import joblib

load_mod = joblib.load('diabete_78.pkl')
app_flask = Flask(__name__)

@app_flask.route('/model')
def model():
    return render_template('model.html')

@app_flask.route('/predict', methods = ['POST'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    print(preg, plas, pres, skin,test, mass, pedi, age)

    predicted = load_mod.predict([[int(preg) , int(plas) , int(pres), int(skin) , int(test) , int(mass) , int(pedi) , int(age)]])
    
    if predicted[0]==1:
        result= 'diabetic'
    if predicted[0]==0:
        result = 'not diabetic'
    
    return render_template('results.html', value=result)

if __name__ == '__main__':
    app_flask.run(debug=True)


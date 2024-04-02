# Imports

from flask import Flask, render_template, request, redirect, url_for
import pickle
import sklearn

#############################################################

with open('models/model1.pkl', 'rb') as file:
    pickled_model1 = pickle.load(file)

with open('models/model2.pkl', 'rb') as file:
    pickled_model2 = pickle.load(file)

#############################################################

app = Flask(__name__)

#############################################################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index2():
    return render_template('index.html')

@app.route('/features.html')
def features():
    return render_template('features.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

#############################################################

@app.route('/results.html')
def results():
    prediction = request.args.get('prediction')
    return render_template('results.html', prediction=prediction)

#############################################################

@app.route('/model1.html', methods=['POST', 'GET'])
def model1():
    if request.method == 'POST':
        
        reaction_time_producer = float(request.form['reactionTimeProducer'])
        reaction_time_consumer1 = float(request.form['reactionTimeConsumer1'])
        reaction_time_consumer2 = float(request.form['reactionTimeConsumer2'])
        reaction_time_consumer3 = float(request.form['reactionTimeConsumer3'])
        elasticity_producer = float(request.form['elasticityProducer'])
        elasticity_consumer1 = float(request.form['elasticityConsumer1'])
        elasticity_consumer2 = float(request.form['elasticityConsumer2'])
        elasticity_consumer3 = float(request.form['elasticityConsumer3'])
        stab = float(request.form['stab'])

        prediction_num = pickled_model1.predict([[reaction_time_producer, reaction_time_consumer1, reaction_time_consumer2, reaction_time_consumer3, elasticity_producer, elasticity_consumer1, elasticity_consumer2, elasticity_consumer3, stab]])
        prediction = "Stable" if prediction_num == 1 else "Unstable"

        return redirect(url_for('results', prediction=prediction))
    
    return render_template("model1.html")

@app.route('/model2.html', methods=['POST', 'GET'])
def model2():
    
    if request.method == 'POST':
        wind_speed = float(request.form['windSpeed'])
        wind_direction = float(request.form['windDirection'])
        power_curve = float(request.form['powerCurve'])

    
        prediction = pickled_model2.predict([[wind_speed, wind_direction, power_curve]])

        return redirect(url_for('results', prediction=prediction))
    
    return render_template("model2.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/model1.html', methods=['POST', 'GET'])
def model1():
    if request.method == 'POST':
        # Get the form data
        reaction_time_producer = float(request.form['reactionTimeProducer'])
        reaction_time_consumer1 = float(request.form['reactionTimeConsumer1'])
        reaction_time_consumer2 = float(request.form['reactionTimeConsumer2'])
        reaction_time_consumer3 = float(request.form['reactionTimeConsumer3'])
        elasticity_producer = float(request.form['elasticityProducer'])
        elasticity_consumer1 = float(request.form['elasticityConsumer1'])
        elasticity_consumer2 = float(request.form['elasticityConsumer2'])
        elasticity_consumer3 = float(request.form['elasticityConsumer3'])
        stab = float(request.form['stab'])

        # Here you can perform your prediction or any other processing with the input data
        # For now, let's just return a basic response
        prediction_result = f"Reaction Time (Energy Producer): {reaction_time_producer}, Reaction Time (Consumer 1): {reaction_time_consumer1}, Reaction Time (Consumer 2): {reaction_time_consumer2}, Reaction Time (Consumer 3): {reaction_time_consumer3}, Elasticity (Energy Producer): {elasticity_producer}, Elasticity (Consumer 1): {elasticity_consumer1}, Elasticity (Consumer 2): {elasticity_consumer2}, Elasticity (Consumer 3): {elasticity_consumer3}, Stability: {stab}"

        return prediction_result
    
    return render_template("model1.html")

@app.route('/model2.html', methods=['POST', 'GET'])
def model2():
    # Get the form data
    if request.method == 'POST':
        wind_speed = float(request.form['windSpeed'])
        wind_direction = float(request.form['windDirection'])
        power_curve = float(request.form['powerCurve'])

        # Here you can perform your prediction or any other processing with the input data
        # For now, let's just return a basic response
        prediction_result = f"Wind Speed: {wind_speed}, Wind Direction: {wind_direction}, Power Curve: {power_curve}"

        return prediction_result
    
    return render_template("model2.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

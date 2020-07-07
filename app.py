from flask import Flask
#from joblib import joblib
import joblib as joblib

app = Flask(__name__)


	# Load ML model
model = joblib.load('./lab week 2/regr_lab2_prob1.pkl')

# Make prediction - features = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
prediction = model.predict([[4, 2.5, 3005, 15, 17903.0, 1]])[0][0].round(1)
prediction = str(prediction)

	# Load ML model
model2 = joblib.load('./lab week 2/regr_lab2_prob2.pkl')

# Make prediction - features = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
prediction2 = model2.predict([[4, 2.5, 3005, 15, 17903.0, 1]]).round(1)
prediction2 = str(prediction2)

@app.route('/')
def predict1():
	return 'Prediction for linear regression' + prediction
@app.route('/')
def predict2():
	return 'Prediction for decision tree regression' + prediction2

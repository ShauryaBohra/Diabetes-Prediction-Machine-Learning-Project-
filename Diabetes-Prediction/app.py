import numpy as np
import pickle
# Flask utils
from flask import Flask, redirect, url_for, request, render_template

# Define a flask app
app = Flask(__name__)

# Load the model
try:
    model = pickle.load(open('model.pkl', 'rb'))
    print('Model loaded. Start serving...')
    print('Check http://127.0.0.1:5000/')
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("Inside POST request")
        # Get form data
        try:
            age = request.form['age']
            gender = request.form['gender']
            Polyuria = request.form['Polyuria']
            Polydipsia = request.form['Polydipsia']
            Weight = request.form['Weight']
            Weakness = request.form['Weakness']
            Polyphagia = request.form['Polyphagia']
            Thrush = request.form['Thrush']
            Blurring = request.form['Blurring']
            Itching = request.form['Itching']
            Irritability = request.form['Irritability']
            Healing = request.form['Healing']
            Paresis = request.form['Paresis']
            Stiffness = request.form['Stiffness']
            Alopecia = request.form['Alopecia']
            Obesity = request.form['Obesity']

            # Create input array for prediction
            newpat = [[int(age), int(gender), int(Polyuria), int(Polydipsia), int(Weight),
                       int(Weakness), int(Polyphagia), int(Thrush), int(Blurring),
                       int(Itching), int(Irritability), int(Healing), int(Paresis),
                       int(Stiffness), int(Alopecia), int(Obesity)]]

            # Make prediction
            if model is not None:
                result = model.predict(newpat)
                print(f"Prediction result: {result}")
                val = "Diabetes" if result[0] == 1 else "No Diabetes"
            else:
                val = "Error: Model not loaded"
        except Exception as e:
            val = f"Error in prediction: {str(e)}"

        return render_template('index.html', value=val)
    
    # For GET request, render the form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
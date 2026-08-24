import os
from flask import Flask, render_template, request
import joblib
import pandas as pd

# Define base directory (root folder: campus_placement_predictor)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static'),
    static_url_path='/static'
)

# Load model
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'placement_model.joblib')
model = joblib.load(MODEL_PATH)

# Note methods=['GET', 'POST'] here!
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        try:
            # Gather all 12 input features matching model training order
            data = {
                'gender': int(request.form.get('gender', 0)),
                'ssc_p': float(request.form.get('ssc_p', 0.0)),
                'ssc_b': int(request.form.get('ssc_b', 0)),
                'hsc_p': float(request.form.get('hsc_p', 0.0)),
                'hsc_b': int(request.form.get('hsc_b', 0)),
                'hsc_s': int(request.form.get('hsc_s', 0)),
                'degree_p': float(request.form.get('degree_p', 0.0)),
                'degree_t': int(request.form.get('degree_t', 0)),
                'workex': int(request.form.get('workex', 0)),
                'etest_p': float(request.form.get('etest_p', 0.0)),
                'specialisation': int(request.form.get('specialisation', 0)),
                'mba_p': float(request.form.get('mba_p', 0.0))
            }
            
            input_df = pd.DataFrame([data])
            res = model.predict(input_df)[0]
            
            prediction = "Placed 🎉" if res == 1 else "Not Placed 😞"
        except Exception as e:
            prediction = f"Error processing input: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
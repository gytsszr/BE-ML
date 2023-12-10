from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = load_model('model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from request
        data = request.get_json()

        # Preprocess the input data (modify this according to your model's input requirements)
        input_data = np.array(data['features'])
        input_data = input_data.reshape((1,) + input_data.shape)

        # Make predictions
        predictions = model.predict(input_data)

        # Post-process the predictions (modify this according to your model's output)
        result = {'prediction': predictions.tolist()}

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

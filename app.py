from flask import Flask, request, jsonify
from tensorflow import keras

app = Flask(__name__)

# Load model saat aplikasi dimulai
model = keras.models.load_model("model.h5")

@app.route('/api/users/resume', methods=['POST'])
def predict_resume():
    # Ambil data input dari request JSON
    data = request.get_json()

    # Lakukan prediksi menggunakan model
    prediction = model.predict(data['input'])

    # Format output sebagai JSON
    output = {'prediction': prediction.tolist()}

    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

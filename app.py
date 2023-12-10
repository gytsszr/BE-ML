import os
from flask import Flask, jsonify, request
from pdf2image import convert_from_path
from deepface import DeepFace

app = Flask(__name__)

CONFIG = {
    "UPLOAD_FOLDER": "static/"
}

def extract_text_from_pdf(pdf_path):
    # Gunakan perpustakaan parsing PDF untuk mengekstrak teks dari file PDF
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += DeepFace.text(img)
    return text

@app.route("/")
def index():
    return jsonify({
        "status_code": 200,
        "message": "Berhasil mengambil API",
        "data": None
    }), 200

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Periksa apakah permintaan POST memiliki bagian file
        if 'resume_pdf' not in request.files:
            return jsonify({
                "status_code": 400,
                "message": "Tidak ada bagian file dalam permintaan",
                "data": None,
            }), 400

        resume_pdf = request.files['resume_pdf']

        if resume_pdf.filename == '':
            return jsonify({
                "status_code": 400,
                "message": "Tidak ada file yang dipilih",
                "data": None,
            }), 400

        pdf_path = os.path.join(CONFIG['UPLOAD_FOLDER'], resume_pdf.filename)
        resume_pdf.save(pdf_path)

        try:
            # Ekstrak teks dari PDF
            resume_text = extract_text_from_pdf(pdf_path)

            # Lakukan prediksi menggunakan model yang telah dilatih
            # Gantilah baris berikut dengan logika prediksi sebenarnya Anda
            hasil_prediksi = {"message": "Gantilah ini dengan logika prediksi Anda", "text": resume_text}

            return jsonify({
                "status_code": 200,
                "message": "Berhasil melakukan prediksi",
                "data": hasil_prediksi
            }), 200
        except Exception as e:
            return jsonify({
                "status_code": 400,
                "message": "Gagal melakukan prediksi karena {}".format(str(e)),
                "data": None,
            }), 400
        finally:
            os.remove(pdf_path)

    else:
        return jsonify({
            "status_code": 405,
            "message": "Metode tidak diizinkan",
            "data": None
        }), 405

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

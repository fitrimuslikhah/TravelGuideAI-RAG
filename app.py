import os
from flask import Flask, render_template, request
from google import genai

app = Flask (__name__)

# Menggunakan gemini API sebagai pengganti dari AWS Bedrock
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY") or "dummy_key_for_testing")

# Simulasi fungsi S3 Knowledge Base (Membaca file dari folder riviews)
def read_lokal_reviews(city_name):
    file_path = f"reviews/{city_name.lower()}.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return f.read()
    return "Belum ada reviews untuk kota ini"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    context = ""
    if request.method == "POST":
        city = request.form.get("city")
        context = read_lokal_reviews(city)

        prompt = f"Berdasarkan ulasan berikut: '{context}, berikut panduan wisata singkat untuk kota '{city}."

        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt
        )
        result = response.text

    # Memanggil file yang ada di folder templates
    return render_template("index.html", result=result, context=context)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
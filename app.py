import os
from flask import Flask, render_template, request
from google import genai
import markdown
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from dotenv import load_dotenv

app = Flask (__name__)
load_dotenv()

# Menggunakan gemini API sebagai pengganti dari AWS Bedrock
client = genai.Client (
    api_key=os.environ.get("GEMINI_API_KEY")
)

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
            model='models/gemini-3.1-flash-lite',
            contents=prompt
        )
        raw_text = response.text

        # Mengubah text markdown dari ai menjadi format html murni
        result = markdown.markdown(raw_text)

    # Memanggil file yang ada di folder templates
    return render_template("index.html", result=result, context=context)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
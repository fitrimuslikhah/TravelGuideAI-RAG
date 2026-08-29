import os
from flask import Flask, render_template, request
from google import genai
import markdown
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

# Route Destination
@app.route("/destination/<city>")
def destination(city):

    destinations = {
        "bandung": {
            "name": "Bandung",
            "description": "A cool city in West Java known for beautiful landscapes, local food, and creative culture.",
            "places": "Kawah Putih, Braga Street, Gedung Sate, and Lembang",
            "food": "Batagor, Seblak, Surabi, and Siomay"
        },

        "bali": {
            "name": "Bali",
            "description": "A tropical destination famous for beaches, temples, culture, and unforgettable experiences.",
            "places": "Ubud, Kuta, Uluwatu, and Nusa Penida",
            "food": "Babi Guling, Ayam Betutu, Lawar, and Sate Lilit"
        },

        "yogyakarta": {
            "name": "Yogyakarta",
            "description": "A cultural city known for heritage, traditional arts, and delicious local cuisine.",
            "places": "Malioboro, Borobudur, Prambanan, and Keraton",
            "food": "Gudeg, Bakpia, Sate Klathak, and Oseng Mercon"
        }
    }

    destination = destinations.get(city.lower())

    if not destination:
        return "Destination not found", 404

    return render_template(
        f"{city.lower()}.html",
        destination=destination
)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    context = ""

    if request.method == "POST":
        city = request.form.get("city")
        context = read_lokal_reviews(city)

        prompt = f"""
You are TravelGuideAI, an AI travel assistant.

Based on the following local reviews:
"{context}"

Create a short travel guide for {city}.

IMPORTANT:
- Respond entirely in English.
- Do not use Indonesian.
- Do not mix English and Indonesian.
- Use clear and natural English.
- Include recommendations for places, food, activities, and useful travel tips.
"""

        response = client.models.generate_content(
            model='models/gemini-3.1-flash-lite',
            contents=prompt
        )

        raw_text = response.text

        # Mengubah text markdown dari AI menjadi HTML
        result = markdown.markdown(raw_text)

    return render_template(
        "index.html",
        result=result,
        context=context
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
## TravelGuideAI (Local RAG Project)

## AWS Architecture Simulation
This project is a local simulation of an AWS RAG (Retrieval-Augmented Generation) architecture:

* **AWS Bedrock** Simulated using **Google Gemini API** (`google-genai`).
* **Amazon S3 (Knowledge Base)** Simulated using local text files (`/reviews`).
* **Amazon S3 / CloudFront (Static Assets):** Simulated using the `/static` directory for images, CSS, and media assets.
* **Amazon EC2 (Application Host)** Simulated running locally via **Flask App**
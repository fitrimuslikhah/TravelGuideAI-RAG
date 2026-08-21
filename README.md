## TravelGuideAI (Local RAG Project)

## AWS Architecture Simulation
This project is a local simulation of an AWS RAG (Retrieval-Augmented Generation) architecture:

* **AWS Bedrock** $\rightarrow$ Simulated using **Google Gemini API** (`google-genai`).
* **Amazon S3 (Knowledge Base)** $\rightarrow$ Simulated using local text files (`/reviews`).
* **Amazon EC2 (Application Host)** $\rightarrow$ Simulated running locally via **Flask App**.
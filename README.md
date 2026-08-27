# TravelGuideAI (Local RAG Project)

## AWS Architecture Simulation

This project is a local simulation of an AWS based RAG (Retrieval Augmented Generation) architecture.

The project demonstrates how several AWS services can be simulated locally using open source tools and Google Gemini API.

### Architecture Components

- **AWS Bedrock**  
  Simulated using **Google Gemini API (Google AI Studio)** with the `google-genai` SDK.

- **Amazon S3 (Knowledge Base)**  
  Simulated using local text files stored in the `/reviews` directory.

- **Amazon S3 / CloudFront (Static Assets)**  
  Simulated using the `/static` directory for images, CSS, and other static assets.

- **Amazon EC2 (Application Host)**  
  Simulated by running the Flask application inside a **Docker container**.

- **Docker / Docker Compose**  
  Used to containerize the Flask application and manage the application environment.

- **CI/CD Pipeline**  
  Planned using **GitHub Actions** for automated testing and deployment.

- **Observability**  
  Implemented using **OpenTelemetry** and integrated with **Grafana Cloud** for application monitoring and telemetry.

## Local Development

Run the application using Docker Compose:

```bash
docker compose up --build
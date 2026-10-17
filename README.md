<img width="2172" height="407" alt="AI Customer Feedback Analyzer Banner (1)" src="https://github.com/user-attachments/assets/0362d2a9-e20d-4090-a34c-a1f091925d1f" />

# 💬 AI Customer Feedback Analyzer

An NLP-powered web application that analyzes customer reviews using a pretrained Hugging Face Transformer model. The application supports individual sentiment predictions as well as bulk customer-feedback analysis through CSV uploads.

## 📑 Table of Contents
- [🚀 Live Demo](#-live-demo)
- [✨ Features](#-features)
- [🏗️ System Architecture](#️-system-architecture)
- [📸 Application Screenshots](#-application-screenshots)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [📊 CSV Format](#-csv-format)
- [🔄 How It Works](#-how-it-works)
- [⚠️ Limitations](#️-limitations)
- [🚀 Future Enhancements](#-future-enhancements)
- [📄 License](#-license)


## 🚀 Live Demo

**Try the application here:** [AI Customer Feedback Analyzer](https://ragasandhiya05-ai-customer-feedback-analyzer-app-dlfxw6.streamlit.app/)


## ✨ Features

- Single-review sentiment prediction
- Positive and negative sentiment classification
- Model confidence scores
- Bulk CSV review processing
- Sentiment distribution visualization
- Interactive results table
- Downloadable CSV results
- Cached model loading for improved performance

## 🏗️ System Architecture

<img width="1372" height="3342" alt="mermaid-diagram (5)" src="https://github.com/user-attachments/assets/c7771e60-feaf-4d3f-9266-283bf318379b" />

## 📸 Application Screenshots

### 1. 🏠 Application Home Page
<p align="center">
  <img width="1761" height="612" alt="Screenshot 2026-10-17 161912" src="https://github.com/user-attachments/assets/fc3a548a-a001-4f52-a7e4-dd29a48ed814" />
</p>

### 2. 😊 Positive Sentiment Analysis
<p align="center">
  <img width="1757" height="740" alt="Screenshot 2026-10-17 162036" src="https://github.com/user-attachments/assets/098f2229-6177-49d7-b53f-500cc8ac5026" />
</p>

### 3. 😞 Negative Sentiment Analysis
<p align="center">
  <img width="1767" height="742" alt="Screenshot 2026-10-17 162142" src="https://github.com/user-attachments/assets/793d8114-3e31-45f7-ac6e-d48b0bde9479" />
</p>

### 4. 📂 Bulk CSV Upload
<p align="center">
  <img width="1757" height="533" alt="Screenshot 2026-10-17 162300" src="https://github.com/user-attachments/assets/29f684bd-10a7-4ac7-a127-32f8ff13740c" />
</p>

### 5. 📊 Feedback Summary
<p align="center">
  <img width="1746" height="443" alt="Screenshot 2026-10-17 162346" src="https://github.com/user-attachments/assets/77365a25-0054-4702-9a5b-a3a65d282521" />
</p>

### 6. 📈 Sentiment Distribution
<p align="center">
  <img width="1757" height="532" alt="Screenshot 2026-10-17 162409" src="https://github.com/user-attachments/assets/e023e140-17da-4d64-94ac-564515352e91" />
</p>

### 7. 📋 Detailed Analysis Results
<p align="center">
  <img width="1756" height="411" alt="Screenshot 2026-10-17 162431" src="https://github.com/user-attachments/assets/492b3f47-9e7b-4c79-8440-e005a3287194" />
</p>

### 8. 💾 Downloaded CSV Results
<p align="center">
  <img width="640" height="171" alt="Screenshot 2026-10-17 162539" src="https://github.com/user-attachments/assets/096007ae-ff8f-4fdb-ad87-3359c0268946" />
</p>

## 🛠️ Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Pandas

## 📂 Project Structure

```text
AI-Customer-Feedback-Analyzer/
├── app.py
├── requirements.txt
├── sample_reviews.csv
├── README.md
└── .gitignore
```

## ⚙️ Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Create and activate a Python virtual environment.
4. Install the required packages.
5. Start the Streamlit application.

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

Open the local URL displayed in the terminal.

## 📊 CSV Format

The uploaded CSV must contain a column named `review`.

```csv
review
"The product is excellent."
"The quality is very poor."
```

## 🔄 How It Works

1. The user enters a review or uploads a CSV file.
2. The application cleans the input text.
3. A pretrained Transformer model predicts sentiment.
4. The application displays sentiment labels and confidence scores.
5. For bulk analysis, the results can be visualized and exported to CSV.

## ⚠️ Limitations

- Predictions depend on the pretrained model and its training data.
- Sarcasm, mixed opinions, and domain-specific language may be classified incorrectly.
- Confidence scores are not guarantees of prediction accuracy.
- The application requires internet access for the initial model download unless the model is already available locally.

## 🚀 Future Enhancements

- Three-class sentiment classification: positive, neutral, and negative
- Emotion detection
- Aspect-based sentiment analysis
- Customer feedback topic extraction
- Sentiment trends over time
- Advanced analytics dashboard

## 📄 License

This project is available for educational and portfolio use. Check the licenses of all third-party libraries and pretrained models before distributing or deploying the application.

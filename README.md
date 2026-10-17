<img width="2172" height="407" alt="AI Customer Feedback Analyzer Banner (1)" src="https://github.com/user-attachments/assets/5085bbd5-7bf1-4229-9823-eb89fbce27f1" />

# AI Customer Feedback Analyzer

An NLP-powered web application that analyzes customer reviews using a pretrained Hugging Face Transformer model. The application supports individual sentiment predictions as well as bulk customer-feedback analysis through CSV uploads.


## 🚀 Live Demo

**Try the application here:** [AI Customer Feedback Analyzer](https://ragasandhiya05-ai-customer-feedback-analyzer-app-dlfxw6.streamlit.app/)


## 📑 Table of Contents

- [Features](#features)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [CSV Format](#csv-format)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features

- Single-review sentiment prediction
- Positive and negative sentiment classification
- Model confidence scores
- Bulk CSV review processing
- Sentiment distribution visualization
- Interactive results table
- Downloadable CSV results
- Cached model loading for improved performance

## System Architecture

<img width="1372" height="3342" alt="mermaid-diagram (5)" src="https://github.com/user-attachments/assets/c7771e60-feaf-4d3f-9266-283bf318379b" />


## Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Pandas

## Project Structure

```text
AI-Customer-Feedback-Analyzer/
├── app.py
├── requirements.txt
├── sample_reviews.csv
├── README.md
└── .gitignore
```

## Installation

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

## CSV Format

The uploaded CSV must contain a column named `review`.

```csv
review
"The product is excellent."
"The quality is very poor."
```

## How It Works

1. The user enters a review or uploads a CSV file.
2. The application cleans the input text.
3. A pretrained Transformer model predicts sentiment.
4. The application displays sentiment labels and confidence scores.
5. For bulk analysis, the results can be visualized and exported to CSV.

## Limitations

- Predictions depend on the pretrained model and its training data.
- Sarcasm, mixed opinions, and domain-specific language may be classified incorrectly.
- Confidence scores are not guarantees of prediction accuracy.
- The application requires internet access for the initial model download unless the model is already available locally.

## Future Enhancements

- Three-class sentiment classification: positive, neutral, and negative
- Emotion detection
- Aspect-based sentiment analysis
- Customer feedback topic extraction
- Sentiment trends over time
- Advanced analytics dashboard

## License

This project is available for educational and portfolio use. Check the licenses of all third-party libraries and pretrained models before distributing or deploying the application.

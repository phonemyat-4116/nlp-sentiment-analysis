# NLP Sentiment Analysis

A Streamlit-based sentiment analysis project with two app entry points:

- `hello.py`: a basic Streamlit demo that reads `Reviews.csv`, shows sample rows, and renders random charts.
- `pages/dashboard.py`: an advanced sentiment dashboard that uses the Hugging Face model `cardiffnlp/twitter-roberta-base-sentiment` for CSV and free-text sentiment analysis.

## Project Structure

- `hello.py` – basic Streamlit page and CSV preview.
- `pages/dashboard.py` – main sentiment analysis dashboard (upload CSV + text analysis).
- `Sentiment Analysis.ipynb` – notebook workbench.
- `Streamlit Sentiment Analysis/main.py` – alternate script variant for the sentiment app.
- `Streamlit Sentiment Analysis/README.md` – minimal legacy note.

## Initialization (First-Time Setup)

### 1) Clone and enter the project

```bash
git clone <your-repo-url>
cd nlp-sentiment-analysis
```

### 2) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install --upgrade pip
pip install streamlit pandas numpy matplotlib seaborn transformers torch
```

> Note: The first run of the RoBERTa dashboard downloads model weights from Hugging Face.

### 4) (Optional) Prepare input CSV

For `hello.py`, place a `Reviews.csv` file in the project root.

For dashboard upload, your CSV should contain one of these columns:

- `Feedback`
- `Review`
- `Text`

### 5) Run the app

Basic page:

```bash
streamlit run hello.py
```

Dashboard page:

```bash
streamlit run pages/dashboard.py
```

## What the Dashboard Does

- Runs sentiment analysis using RoBERTa.
- Supports long texts by chunking and averaging class scores.
- Produces `positive`, `negative`, `neutral`, and `compound` scores.
- Labels each row as `Positive`, `Negative`, or `Neutral`.
- Visualizes sentiment distribution with pie and bar charts.
- Lets you download analyzed CSV output.

## Troubleshooting

- If Streamlit command is missing, verify virtual environment is activated.
- If model loading fails, check internet access for initial model download.
- If CSV upload fails, ensure your file has `Feedback`, `Review`, or `Text` column.

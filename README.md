# Advanced Sentiment Analysis with RoBERTa

A Streamlit-based sentiment analysis project powered by the `cardiffnlp/twitter-roberta-base-sentiment` model.

This repository now supports two practical workflows:

1. **Notebook-first workflow (primary entry point)** via `Sentiment_Analysis.ipynb`
2. **Direct Streamlit app workflow** via `Streamlit Sentiment Analysis/main.py`

The notebook flow uses **ngrok as a bridge** so you can open the Streamlit app from a public URL while it runs in a hosted notebook environment.

---

## Project Structure

```text
.
├── README.md
├── Sentiment_Analysis.ipynb                # Primary entry point
├── hello.py                                # Simple Streamlit demo script
└── Streamlit Sentiment Analysis/
    ├── main.py                             # Main Streamlit sentiment app
    └── README.md
```

---

## Features

- RoBERTa sentiment inference using Hugging Face transformers.
- Supports:
  - **CSV upload analysis** (`Feedback`, `Review`, or `Text` column)
  - **Single text input analysis**
- Outputs:
  - Positive / Negative / Neutral probabilities
  - Compound sentiment score (`positive - negative`)
  - Sentiment label (`Positive`, `Neutral`, `Negative`)
- Visual summaries with pie chart + bar chart.
- Downloadable CSV with sentiment results.

---

## Primary Usage: Run from Notebook (with ngrok)

Use this when your environment cannot expose port `8501` directly (for example, cloud notebooks).

### 1) Open `Sentiment_Analysis.ipynb`
Run cells in order.

### 2) Install required packages
The notebook installs dependencies such as Streamlit and pyngrok.

### 3) Configure ngrok
Set your ngrok authtoken before opening the tunnel.

> **Important:** Do not hardcode secrets in notebooks for shared/public repos. Use environment variables or secret managers instead.

### 4) Launch Streamlit and create the tunnel
The notebook runs the app and opens an ngrok tunnel to `localhost:8501`.

### 5) Open the printed public URL
Use the ngrok URL printed in notebook output to access the app.

---

## Alternative Usage: Run locally from `main.py`

If you are running on your own machine and can open local ports, run Streamlit directly:

```bash
cd "Streamlit Sentiment Analysis"
streamlit run main.py
```

Then open the local URL (usually `http://localhost:8501`).

---

## Dependencies

Typical packages used in this project:

- `streamlit`
- `pandas`
- `matplotlib`
- `seaborn`
- `transformers`
- `torch`
- `pyngrok` (notebook/ngrok workflow)

Install with pip as needed:

```bash
pip install streamlit pandas matplotlib seaborn transformers torch pyngrok
```

---

## Input Format

For CSV upload mode, include one of these columns:

- `Feedback`
- `Review`
- `Text`

If none of these columns exist, the app will show an error.

---

## Notes

- GPU is used automatically if available (`torch.cuda.is_available()`).
- Long text is chunked before inference to stay within model limits.
- Model loading is cached for better performance.

---

## Troubleshooting

- **App not reachable from notebook environment:**
  - Confirm ngrok auth is configured.
  - Confirm tunnel is pointing to port `8501`.
  - Restart the tunnel if the URL expired.

- **Slow analysis on large CSV files:**
  - This is expected with transformer inference.
  - Use smaller batches/files or a GPU-backed runtime.

- **Model download issues:**
  - Verify internet access in your runtime.
  - Retry after clearing environment cache if needed.

---


# Optimisation_in_PyTorch

# 🧠 Sentiment Classification on SST-2 using Linear Models (PyTorch)

## 📌 Overview

This project implements a binary sentiment classification system using the **SST-2 (Stanford Sentiment Treebank)** dataset. The goal is to classify sentences as **positive or negative** using classical machine learning techniques and PyTorch-based linear models.

The project focuses on understanding the full NLP pipeline — from raw text to numerical representation and model training — rather than using pre-trained large language models.

---

## 🎯 Objectives

- Understand text preprocessing and NLP pipelines
- Implement tokenization and Bag-of-Words feature extraction
- Build logistic regression model using PyTorch
- Train and evaluate sentiment classification models
- Explore optimization techniques and training dynamics

---

## 🧩 Dataset

- **Dataset:** SST-2 (Stanford Sentiment Treebank)
- **Task:** Binary sentiment classification
- **Labels:**
  - `0` → Negative sentiment
  - `1` → Positive sentiment

---

## ⚙️ Pipeline

### 1. Text Preprocessing
- Lowercasing
- Cleaning special characters
- Normalization of text input

### 2. Tokenization
- Splitting sentences into word-level tokens
- Building vocabulary from training data

### 3. Feature Extraction
- Bag-of-Words representation
- Fixed vocabulary size (top 10,000 most frequent words)
- Conversion of text → numerical vectors

### 4. Model
Implemented a **Logistic Regression model from scratch using PyTorch**:
- Linear transformation: `xW + b`
- Sigmoid activation for probability output
- Binary classification threshold at 0.5

---

## 🧠 Model Architecture

- Input: Bag-of-Words feature vector
- Layer: Linear (Fully Connected)
- Activation: Sigmoid
- Output: Probability of positive sentiment

---

## 🏗️ Implementation Highlights

- Custom weight initialization (zeros / random / tensor-based)
- Manual implementation of forward pass
- Training using gradient-based optimization
- Experimentation with optimization algorithms (SGD, Adam, etc.)
- PyTorch-based tensor operations

---

## 📊 Key Concepts Learned

- Tokenization & vocabulary design
- Feature engineering for NLP
- Logistic regression fundamentals
- Gradient-based optimization
- PyTorch model building
- Training workflow for ML systems

---

## 🧪 Technologies Used

- Python 🐍
- PyTorch 🔥
- NumPy
- Matplotlib
- Jupyter Notebook
- VS Code

---

## 🚀 How to Run

```bash
# Clone repository
git clone https://github.com/your-username/your-repo.git

# Install dependencies
pip install torch numpy matplotlib

# Open notebook
jupyter notebook LLM_Architectures.ipynb

## 📁 Project Structure

```text
Projects/
│
├── LLM_Architectures.ipynb # Main notebook (SST-2 sentiment classification)
├── README.md # Project documentation
│
└── scripts/
└── clean_notebook.py # Utility script to fix Jupyter notebook metadata for GitHub rendering
```

## ⚠️ Notes

- This project was developed as part of hands-on ML learning and experimentation.
- Notebook metadata was cleaned to ensure GitHub compatibility.
- Some interactive Colab-specific components were removed for reproducibility in local environments.
- The repository includes a utility script in `scripts/` used to clean Jupyter notebook metadata to ensure proper GitHub rendering.

## 📌 Future Improvements

- Replace Bag-of-Words with embeddings (Word2Vec / GloVe / BERT)
- Extend to deep learning models (RNN / Transformer)
- Add full training pipeline with evaluation metrics dashboard
- Convert into API using FastAPI or Streamlit UI
# RAG Retrieval & Generation Dashboard

> An end-to-end interactive platform for evaluating how neural reranking affects generation quality in biomedical Retrieval-Augmented Generation pipelines — built around the BioASQ benchmark.

---

## Why This Exists

Getting good answers from a RAG system isn't just about the generator — it's about **what you retrieve**. This dashboard was built to answer one concrete research question:

> **Does neural reranking meaningfully improve generation quality over BM25 alone, or is the difference just noise?**

The tool lets you run live queries through the full pipeline, compare every reranker configuration side by side, stress-test your results with statistical significance tests, and drill into exactly where and why a model fails. It's designed to give researchers and engineers the visibility needed to make informed decisions about reranker selection, fine-tuning, and retrieval depth — all of which directly impact the quality of generated answers.

---

## Pages

### 1 · Query Interface

Submit any biomedical question, choose a reranker model, and get a generated answer alongside live retrieval and generation metrics. The main entry point for exploratory analysis.

![Query Interface](https://github.com/user-attachments/assets/92827d54-323a-4214-95e4-09b9ed665ace)

---

### 2 · Retrieval Metrics

Deep-dive retrieval analysis across all pipeline configurations. Compares models on MRR, Recall@k, NDCG and more, with a per-query-type breakdown (factoid, yes/no, list, summary) to reveal where each reranker earns its place.

![Retrieval Metrics](https://github.com/user-attachments/assets/5e2f2613-8e9d-4acb-8e80-b7384222d744)

---

### 3 · Generation Metrics

Side-by-side generation quality comparison across all reranker models. Covers RAGAS Faithfulness, BERTScore, and BioASQ-native scores (accuracy, mean F1 by question type). Best-performing model per metric is automatically highlighted so the winner is always obvious at a glance.

![Generation Metrics](https://github.com/user-attachments/assets/536fd2f1-4bc3-4fc2-a53f-e46499b43dd9)

---

### 4 · Statistical Analysis

Runs Wilcoxon signed-rank tests across all model pairs to determine whether observed improvements are statistically significant or fall within noise. This is the page that answers the core thesis question with rigor, not just intuition.

![Statistical Analysis](https://github.com/user-attachments/assets/3e765b54-8792-44d8-b9a6-39da52faa266)

---

### 5 · Failure Analysis

Surfaces individual queries where a reranker underperformed BM25 or another baseline on generation metrics. Identifying *where* a model fails is the first step to understanding *why* — and this page makes that systematic rather than anecdotal.

![Failure Analysis](https://github.com/user-attachments/assets/89db9ce4-5732-458f-acae-42fc69f0fa9a)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vite · React · TypeScript · Tailwind CSS |
| Backend | Python · FastAPI · Uvicorn |
| Retrieval | Pyserini · BM25 · monoT5 · duoT5 · LiT5-Distill · Qwen3 |
| Generation | Llama-3.1-8B (HuggingFace Transformers) |
| Evaluation | RAGAS · BERTScore · BioASQ metrics · SciPy (Wilcoxon) |
| Environment | Conda · CUDA · Linux |

---

## Setup & Installation

### Requirements

- Linux (tested on Ubuntu) with a CUDA-capable GPU
- [Miniconda or Anaconda](https://docs.conda.io/en/latest/miniconda.html)
- Node.js ≥ 18 and npm
- Python 3.10+

---

### 1 · Clone the repository

```bash
git clone https://github.com/your-username/reranking_project.git
cd reranking_project
```

---

### 2 · Set up the Python environment

```bash
conda create -n pyml python=3.10 -y
conda activate pyml
```

Install core Python dependencies:

```bash
pip install fastapi uvicorn
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers accelerate peft
pip install pyserini
pip install ragas datasets
pip install bert-score
pip install scipy numpy pandas
```

> **Note on Pyserini:** it requires Java 11+. Install it with:
> ```bash
> sudo apt install default-jdk -y
> ```

---

### 3 · Install frontend dependencies

```bash
cd application/frontend
npm install
```

---

## Running the Application

The app runs as two separate processes: a Python backend (FastAPI) and a React frontend (Vite). Open two terminal windows or use the one-liner below.

### Backend

```bash
cd reranking_project
conda activate pyml
python3 -m uvicorn application.backend.main:app --port 8765
```

API available at → `http://localhost:8765`

### Frontend

```bash
cd reranking_project/application/frontend
npm run dev
```

Dashboard available at → `http://localhost:5173`

---

### Launch both at once (Kitty terminal)

If you use the [Kitty](https://sw.kovidgoyal.net/kitty/) terminal with Fish shell, this script opens both processes in separate windows simultaneously:

```bash
#!/bin/bash
PROJECT_DIR="$HOME/Desktop/reranking_project"

# Backend window
kitty fish -c "
  cd $PROJECT_DIR
  conda activate pyml
  python3 -m uvicorn application.backend.main:app --port 8765
  exec fish
" &

# Frontend window
kitty fish -c "
  cd $PROJECT_DIR/application/frontend
  npm run dev
  exec fish
" &
```

Each window stays open as a persistent Fish shell after the process exits, so you can inspect logs or restart without opening a new terminal.

---

## Research Context

Built as the experimental evaluation tool for a master's thesis on neural reranking for biomedical RAG using the [BioASQ](http://bioasq.org/) benchmark. The pipeline fixes BM25 as the first-stage retriever and Llama-3.1-8B as the generator, treating the reranker as the sole ablation variable across all experiments.

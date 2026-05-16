# RAG Retrieval & Generation Dashboard

> An end-to-end analysis platform for evaluating neural reranking in biomedical Retrieval-Augmented Generation pipelines, built as part of a master's thesis on the BioASQ benchmark.

---

## Overview

This full-stack application provides an interactive environment for running queries through a complete RAG pipeline and deeply analyzing both retrieval and generation quality across multiple reranker configurations. It was designed to answer a central research question: **does neural reranking meaningfully improve generation quality over BM25 alone?**

The dashboard covers the full evaluation loop — from live query execution, to retrieval metric comparison, generation quality scoring, statistical significance testing, and failure analysis.

---

## Pages

### Query Interface
Submit any biomedical question, select a reranker model, and receive a generated answer alongside retrieval and generation metrics in real time.

![Query Interface](https://private-user-images.githubusercontent.com/92827d54-323a-4214-95e4-09b9ed665ace)

---

### Retrieval Metrics
In-depth retrieval analysis per model and per query type (factoid, yes/no, list, summary). Tracks MRR, Recall@k, NDCG, and more across all pipeline configurations.

![Retrieval Metrics](https://private-user-images.githubusercontent.com/5e2f2613-4acb-8e80-b7384222d744)

---

### Generation Metrics
Side-by-side comparison of generation quality across all reranker models. Metrics include RAGAS Faithfulness, BERTScore, and BioASQ-native scores (accuracy, mean F1 by question type). Best-performing model per metric is automatically highlighted.

![Generation Metrics](https://private-user-images.githubusercontent.com/536fd2f1-4bc3-4fc2-a53f-e46499b43dd9)

---

### Statistical Analysis
Runs Wilcoxon signed-rank tests to determine whether reranking improvements are statistically significant or within noise. Answers the core thesis question with rigorous hypothesis testing.

![Statistical Analysis](https://private-user-images.githubusercontent.com/3e765b54-8792-44d8-b9a6-39da52faa266)

---

### Failure Analysis
Surfaces individual queries where a given reranker underperformed BM25 or another baseline. Helps identify systematic failure modes and informs iterative model improvement.

![Failure Analysis](https://private-user-images.githubusercontent.com/89db9ce4-5732-458f-acae-42fc69f0fa9a)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vite + React + TypeScript + Tailwind CSS |
| Backend | Python · FastAPI (Uvicorn) |
| IR / Retrieval | Pyserini · BM25 · Neural rerankers (monoT5, duoT5, LiT5, Qwen3) |
| Generation | Llama-3.1-8B via HuggingFace |
| Evaluation | RAGAS · BERTScore · BioASQ metrics · SciPy (Wilcoxon) |
| Environment | Conda (`pyml`) · CUDA · RTX 3060 |

---

## Running the Application

The app has two processes: a **Python/FastAPI backend** and a **Vite/React frontend**. Both are launched from the project root.

### Prerequisites

- [Conda](https://docs.conda.io/) with a `pyml` environment containing all Python dependencies
- Node.js + npm installed for the frontend

### Start the Backend

```bash
cd ~/Desktop/reranking_project
conda activate pyml
python3 -m uvicorn application.backend.main:app --port 8765
```

The API will be available at `http://localhost:8765`.

### Start the Frontend

```bash
cd ~/Desktop/reranking_project/application/frontend
npm run dev
```

The dashboard will be available at `http://localhost:5173` (or whichever port Vite assigns).

### One-liner (with Kitty terminal)

If you use the [Kitty](https://sw.kovidgoyal.net/kitty/) terminal, both processes can be launched simultaneously:

```bash
# Backend
kitty fish -c "
  cd ~/Desktop/reranking_project
  conda activate pyml
  python3 -m uvicorn application.backend.main:app --port 8765
  exec fish
" &

# Frontend
kitty fish -c "
  cd ~/Desktop/reranking_project/application/frontend
  npm run dev
  exec fish
" &
```

Each process opens in its own Kitty window with a persistent Fish shell after the process exits.

---

## Context

Built as the experimental evaluation tool for a master's thesis investigating neural reranking for biomedical RAG on the [BioASQ](http://bioasq.org/) benchmark. The pipeline uses BM25 as a fixed first-stage retriever and ablates neural rerankers as the variable, with Llama-3.1-8B as the fixed generator throughout.

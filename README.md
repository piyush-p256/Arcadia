# 🎮 Arcadia

**Esports Nexus** is a modular, AI-driven backend platform that powers real-time coaching, smart matchmaking, skill analytics, and personalized highlight generation for esports players, coaches, organizers, and fans.

---

## 🚀 Key Modules

### 🔹 Real-Time AI Coach (RL-based)
- Provides voice & HUD tips during gameplay
- Adapts to player behavior over time

### 🔹 Skill Gap Analyzer
- Uses unsupervised clustering (KMeans) to detect playstyle mismatches
- Enables dynamic team balancing & fair matchmaking

### 🔹 Automated Multi-Angle Highlight Generator
- Ingests raw camera feeds (POV, HUD, broadcast)
- Generates shareable reels based on fan-selected highlight profiles
- Adds captions + TTS ("Pentakill!", "Ace!") using CV + NLP

### 🔹 Esports Knowledge Graph
- Unifies player ↔ team ↔ match ↔ event data across titles
- Enables smart search, commentary summaries & cross-game career tracking

---

## 🧠 Tech Stack

| Layer             | Tech Used                                      |
|------------------|------------------------------------------------|
| Backend Framework| FastAPI (Python)                               |
| AI/ML            | scikit-learn, transformers, spaCy, OpenCV      |
| RL Agent         | Stable-Baselines3, PyTorch                     |
| CV/NLP           | OpenCV, TTS (gTTS), Transformers (HuggingFace) |
| Data Layer       | Neo4j (Knowledge Graph), JSON (Mocked DB)      |
| Others           | Uvicorn, Pydantic, NumPy, SciPy                |

---

## 📂 Project Structure
backend/
├── app.py                # FastAPI main app
├── models.py             # Pydantic models for requests/responses
├── ai_modules/
│   ├── init.py
│   ├── realtime_coach.py # RL agent for in-game coaching
│   ├── skill_gap_analyzer.py # Playstyle clustering
│   ├── highlight_generator.py # CV-driven highlight stitching
│   └── knowledge_graph.py # Neo4j knowledge base
├── utils/
│   ├── cv_utils.py       # Action recognition mock
│   ├── audio_utils.py    # TTS generation
│   └── nlp_utils.py      # Summarization / captions


---

## ⚙️ Setup & Run

### 🧩 Prerequisites
- Python 3.9+
- (Optional) Neo4j Desktop running locally

### 📦 Install Dependencies

```bash
pip install -r requirements.txt

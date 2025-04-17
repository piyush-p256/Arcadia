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

## ⚙️ Setup & Run

### 🧩 Prerequisites
- Python 3.9+
- (Optional) Neo4j Desktop running locally


## ▶️ Run API Server

```bash
uvicorn app:app --reload
Open API docs at: http://localhost:8000/docs

---
## 📡 Sample API Endpoints

- `POST /coach-feedback`  
  Get live coaching tips

- `POST /analyze-skill-gap`  
  Return player clustering & gaps

- `POST /generate-highlights`  
  Create highlight reel for a fan profile

- `GET /knowledge-graph/player/{id}`  
  Query player insights

---

## 🎯 Use Cases

- 🧠 **AI-Powered Coaching** for training maps  
- 🧩 **Matchmaking** for esports tournaments  
- 🎬 **Personalized Social Clips** for fans  
- 🧾 **Smart Dashboards** for analysts & casters  

---

## 🌱 SDG Alignment

- **SDG 4: Quality Education** – Learning through gamified coaching  
- **SDG 9: Industry, Innovation, and Infrastructure** – Modern AI infrastructure for gaming  
- **SDG 17: Partnerships for the Goals** – Empowering teams, platforms & sponsors alike  

---

## 🔮 Future Scope

- 🧩 **Game Plugin SDK** for Valorant, CS2, LoL  
- 🗣️ **Real-time Overlays and Voice Commands** powered by LLMs  
- 📊 **B2B Dashboards** for teams, sponsors, and esports orgs  
- 💰 **Data Monetization** with user-consented training sets  

---

## 👥 Contributors

Built with 💡 by the **Esports Nexus** team – powered by vision, caffeine & clutch plays.

# 🧩 I-m-Beside-You  

## 📌 Project Context  
At **IIT Delhi**, our annual cultural fest **Rendezvous (RDV)** involves building small apps/tools to manage:  
- Student event registrations  
- Payments and budgeting  
- Event scheduling  
- Notifications and announcements  

Traditionally, these apps are developed as a **monolithic system**:  
- One script or repo handles everything  
- If the “registration” logic breaks, the entire app may fail  
- Updates are risky and hard to manage  

To solve this, we developed an **AI-driven microservices conversion assistant**.  

---

## 🎯 Problem Statement  
Students often face challenges maintaining monolithic fest apps:  
- **High coupling** – a bug in one feature can break the whole system  
- **Low scalability** – difficult to add new modules like live voting, feedback, or analytics  
- **Slow iteration** – every change requires redeploying the entire app  

Due to **time constraints**, I could not build and demonstrate this on the actual RDV fest application.  
Instead, I implemented the same workflow on **another monolithic application** to validate the approach.  
The results and methodology are directly transferable to RDV apps.  

---

## 🤖 AI Agent Solution  
We built an **AI Agent Prototype** that:  
- Analyzes monolithic fest apps  
- Suggests a **microservices design**, e.g.:  
  - Registration Service  
  - Payments Service  
  - Scheduling Service  
  - Notifications Service  
- Automates **code transformation** from monolith → microservices  
- Provides **evaluation metrics** for service quality (e.g., modularity, coupling, maintainability)  

---

## 🚀 Features  
- **Static Code Analysis** (Java-ready, tested on another monolithic app)  
  - Extracts file structure, package/class/method relationships, and coupling metrics  
  - Builds a **knowledge graph** of the monolith  
- **GraphRAG Enrichment**  
  - Converts the structural graph into a **GraphRAG-compatible schema**  
  - Adds semantic embeddings for retrieval-augmented generation (RAG)  
- **Generative AI Decomposition**  
  - Uses **Google Gemini 2.0 Flash** to propose a microservices architecture  
  - Each service includes responsibilities, functions, dependencies, and API endpoints  
- **Code Generation**  
  - Auto-scaffolds **FastAPI-based microservices**  
  - Includes REST endpoints, modular folder structure, and `requirements.txt`  
- **Deployment**  
  - Cleaned and deployed with **Uvicorn + ngrok**, exposing each service via public URLs  

---

## 📂 Repository Structure  
```bash
.
├── monolith_inspector.py       # Static analysis & knowledge graph builder
├── graphrag_merger.py          # GraphRAG enrichment
├── analysis_output/            # Generated analysis results
│   ├── file_structure.md
│   ├── file_structure.json
│   ├── knowledge_graph.json
│   ├── knowledge_graph.graphml
│   └── coupling_metrics.csv
├── microservices/              # AI-generated microservices plan
│   └── microservices_plan.json
├── microservices_code/         # Generated FastAPI service code
│   └── <service_name>/app.py
├── reports/                    # Data science report & evaluation
│   ├── fine_tuning_setup.md
│   ├── evaluation_metrics.csv
│   └── summary.pdf
└── README.md                   # Documentation

## ⚙️ Workflow

1. **Static Analysis**
   ```bash
   python3 monolith_inspector.py --repo https://github.com/KimJongSung/jPetStore.git --out analysis_output
   ```

2. **GraphRAG Enrichment**
   ```bash
   python3 graphrag_merger.py
   ```

3. **Microservices Architecture Proposal**
   - Load `analysis_output/*`
   - Query **Gemini 2.0 Flash**
   - Generate `microservices/microservices_plan.json`

4. **Code Generation**
   ```bash
   python3 generate_microservices.py
   ```

5. **Deployment (FastAPI + Uvicorn + ngrok)**
   ```bash
   uvicorn app:app --reload --port 8000
   ```

---

## 📊 Outputs
- **File Structure** → Markdown + JSON representation  
- **Knowledge Graph** → Dependencies in GraphML + JSON  
- **Coupling Metrics** → Afferent/efferent dependencies (CSV)  
- **GraphRAG Context** → Enriched entities + relationships JSON  
- **Microservices Plan** → JSON with proposed services  
- **Service Code** → FastAPI scaffolding  

---

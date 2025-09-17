# I-m-Beside-You
📌 Project Context

At IIT Delhi, our annual cultural fest Rendezvous (RDV) involves building small apps/tools to manage:

Student event registrations

Payments and budgeting

Event scheduling

Notifications and announcements

Traditionally, these apps are developed as a monolithic system:

One script or repo handles everything.

If the “registration” logic breaks, the entire app may fail.

Updates are risky and hard to manage.

To solve this, we developed an AI-driven microservices conversion assistant.

🎯 Problem Statement

Students often face challenges maintaining monolithic fest apps:

High coupling – a bug in one feature can break the whole system.

Low scalability – difficult to add new modules like live voting, feedback, or analytics.

Slow iteration – every change requires redeploying the entire app.

🤖 AI Agent Solution

We built an AI Agent Prototype that:

Analyzes monolithic fest apps.

Suggests a microservices design:

Registration Service

Payments Service

Scheduling Service

Notifications Service

Automates code transformation from monolith → microservices.

Provides evaluation metrics for service quality (e.g., modularity, coupling, maintainability).

🔧 Core Features (Mandatory)

Manual Task Automated: Breaking monolithic fest management apps into independent microservices.

Fine-Tuned Model: Integrated parameter-efficient fine-tuning (LoRA) on code datasets to identify module boundaries.

Evaluation Metrics:

Code modularity score

Service dependency mapping

Error isolation tests

🌟 Optional Features (Bonus)

Multi-agent Collaboration: Planner agent (identifies microservices) + Executor agent (rewrites code).

External Integrations: Retrieval-Augmented Generation (RAG) for suggesting fest-specific features (e.g., live polls, budgeting).

User Interface: CLI-based prototype for uploading fest app code and receiving microservice suggestions.

📂 Repository Structure
├── src/                # Core AI agent implementation
├── models/             # Fine-tuned LoRA models
├── examples/           # Demo monolithic fest apps
├── outputs/            # Microservice-converted code
├── reports/            # Data science report & evaluation
└── README.md           # Project documentation

📊 Deliverables

✅ Source Code of the AI Agent Prototype

✅ Architecture Document – components, flow, and reasoning

✅ Data Science Report – fine-tuning setup & evaluation

✅ Interaction Logs – prompts and chat history with AI

🎥 (Optional) Demo video/screenshots

📬 Submission Info

Name: Atharva Patil

University: IIT Delhi

Department: Electrical Engineering (Power and Automation)

Expected Graduation: 2027

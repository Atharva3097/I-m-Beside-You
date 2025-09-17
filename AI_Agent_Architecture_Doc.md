# I'm-Beside-You: AI-Driven Microservices Conversion Assistant

## 1. Project Context and Problem Statement
Traditionally, monolithic applications, like those used for student event registrations at IIT Delhi, suffer from several drawbacks, including high coupling, low scalability, and slow iteration. A bug in one feature can cause the entire system to fail, and adding new modules is difficult and risky.
To address these challenges, we have developed an AI Agent Prototype designed to act as an AI-driven microservices conversion assistant. The agent analyzes a monolithic codebase and automates the transformation process. The results and methodology are transferable to other monolithic applications. 

---

## 2. AI Agent Components
The AI agent's architecture is a multi-stage pipeline, with each component specializing in a specific task. This layered approach ensures a clear separation of concerns and a logical workflow.
- **Static Code Analysis Module:** This is the agent's perception layer. It processes the raw source code of the monolithic application.
  - Tool: monolith_inspector.py
  - Functionality: Clones a GitHub repository, traverses the file system, and analyzes the code to extract its structure, including package, class, and method relationships. It generates a knowledge graph in .graphml and .json formats, and calculates package-level coupling metrics.
- **GraphRAG Enrichment Module:** This module enriches the structural data with semantic context.
  - Tool: graphrag_merger.py
  - Functionality: Takes the outputs from the static analysis (the knowledge graph, file structure, and coupling metrics) and combines them into a single, cohesive representation compatible with a GraphRAG schema. This enriched context includes nodes (entities) with text and embeddings and relationships (edges) between them. This is the agent's memory or knowledge base.
- **Generative AI Decomposition Module:** This is the agent's reasoning engine and planning component. It uses the enriched context to make architectural decisions
  - Model: Google Gemini 2.0 Flash.  
  - Functionality: The agent is given a detailed prompt that includes all the analysis files (graph_context.json, knowledge_graph.json, coupling_metrics.csv, etc.) and a request to propose a microservices architecture in a strict JSON format. The model's output is a microservices_plan.json file.
- **Code Generation Module:** This is the action execution module. It translates the high-level plan into concrete code.
  - Tool: generate_microservices.py
  - Functionality: For each proposed service in the microservices_plan.json, the agent generates a new prompt. This prompt instructs the Gemini model to scaffold a complete Python FastAPI project, including app.py, requirements.txt, and a modular folder structure.
- **UI Scaffolding Module:** This is an additional action taken by the agent.
  - Functionality: The agent is also prompted to generate a user interface in the form of interactive and good-looking code. This UI code is saved along with the respective microservice files so it can be hosted to see the results of the microservices. 

---

## 3.Interaction Flow
The AI agent operates in a sequential, multi-step process, with the output of one step serving as the input for the next. This can be described as a prompt chaining workflow.
- **Static Analysis :** The monolith_inspector.py script is executed with a GitHub repository URL, which clones the repository and performs the static analysis to produce the outputs in a designated analysis_output directory.
- **GraphRAG Enrichment :** The graphrag_merger.py script takes the files from the analysis_output directory and enriches them, generating graph_context.json and node_index.json.
- **Generative AI Decomposition :** The enriched analysis files are loaded into a single string and passed as context to the Gemini model with a prompt to generate a JSON microservices plan. This plan is saved as microservices/microservices_plan.json.
- **Code Generation :** The microservices_plan.json is read, and for each service defined in the plan, a new prompt is sent to the Gemini model to generate the actual FastAPI code. The generated code is then saved into a dedicated folder for each service.

---

## 4.Reasons for Architectural Choices
- **Modular Pipeline:** The architecture is broken down into distinct, independent components. This design makes the system easier to develop, test, and debug. Each module performs a single, specific function, such as analysis or code generation, which simplifies maintenance.
- **Gemini 2.0 Flash:** This model was chosen for its ability to handle complex reasoning tasks and generate structured, detailed output, which is crucial for proposing the microservices architecture in a specific JSON format.
- **GraphRAG Enrichment:** The use of GraphRAG is a key architectural decision. It allows the agent to build a comprehensive knowledge graph of the codebase, which enriches the context provided to the LLM. This approach improves the quality of the AI's reasoning and reduces the likelihood of hallucinations by providing a solid factual foundation for its decisions.
- **Framework:** FastAPI was chosen for the generated microservices due to its performance, asynchronous capabilities, and automatic documentation generation. This choice aligns with the goal of creating modern, efficient microservices.
- **Human-in-the-Loop:** The architecture is designed to be transparent. By generating human-readable intermediate files like microservices_plan.json, a developer can easily review the agent's proposed architecture and provide feedback before the final code is generated.




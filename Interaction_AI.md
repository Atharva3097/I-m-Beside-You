### Sequential Prompts from Development

#### **Log 1: Understanding the Problem**

* **Prompt:** "what doe sit mean by breaking a monolithic service into different microservices"
* **AI Response:** "A monolithic service (or application) is built as a single, large unit. All features, business logic, database access, and user interface are packaged together. If you want to change one small part, you need to re-deploy the entire application. Scaling is done by running multiple copies of the whole thing. Imagine an e-commerce app (monolith). It contains in one codebase: User authentication, Product catalog, Cart management, Payments, Order tracking."

#### **Log 2: Defining the High-Level Approach**

* **Prompt:** "i am thinking for first making a knowledge graph and then indexing according to tot heir context, and then query it to make microservices out of it using mcp along with for better understading and completing just like cursor ai suggest steps is it right and more things i can add in this for my objective problem"
* **AI Response:** "Got it—you're thinking of using a knowledge graph + indexing + query mechanism to guide the decomposition of a monolith into microservices (with MCP / Cursor-like guidance). That's an interesting, systematic approach. Let me break it down for you."
    * **Knowledge Graph:** "Nodes = entities (modules, functions, data tables, APIs, business domains). Edges = dependencies (calls, data flows, ownership, coupling)."
    * **Index by context:** "Group related modules around bounded contexts (like Domain-Driven Design). E.g., Auth functions cluster together, Cart functions cluster together."
    * **Query the graph:** "To see which functions are tightly coupled vs loosely coupled."

#### **Log 3: Generating a Detailed Workflow**

* **Prompt:** "okay now step by step for this generate the workflow with requirements at each step covering this thoroughly"
* **AI Response:** "Here's a thorough, step-by-step workflow you can follow to decompose a monolith using a knowledge graph, context indexing, and MCP-driven guidance. Each step lists purpose, inputs, activities, deliverables, tools, and acceptance criteria so you can run it like a project. 0) Clarify objectives, constraints, and success metrics. Purpose: Ensure the decomposition solves a real problem: agility, scalability, fault isolation, team autonomy. Inputs: Business drivers, SLAs/SLOs, compliance needs, cost constraints, team capacity. Activities: Write measurable goals (e.g., deploy lead time ≤ 1 day for Service X, p95 latency ≤ 150 ms, error budget = 0.1%), Identify critical domains and 'must not break' flows. Deliverables: One-page objectives with 3-5 success metrics."

#### **Log 4: Generating a Code Snippet**

* **Prompt:** "please follow the workflow i have defined first write the code for parsing the github repo which can be coverted into knowledge graph"
* **AI Response:** "Nice—here's a focused, ready-to-run Python script that parses a GitHub repo (PHP + JS + templates) and emits a machine-friendly inventory and a knowledge-graph (GraphML + JSON) you can feed into later pipeline steps. Save as `parse_repo_to_kg.py`."

#### **Log 5: Explaining the Architecture**

* **Prompt:** "Promoted how does cursor ai works?"
* **Prompt:** "Promoted explain its architecture how it works like makes a knwledge graph and then what it does how it changes code and all"
* **AI Response:** *(The AI response to this specific prompt is not visible in the provided screenshot, but it would have explained the full process of the AI agent's architecture, from creating the knowledge graph to generating code.)*

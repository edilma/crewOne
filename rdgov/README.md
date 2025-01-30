```markdown
# Multi-Agent Design Pattern App
## CrewAI Project: Stock Analysis Blog Generator

This project was created using **Autogen** by Deeplearning, and I recreated using  **CrewAI** .  CrewAI's structured YAML-based configuration and workflow management, so it's easier to work with.

The app does generate blog post about **Nvidia's stock price performance** using multiple multiple specialize AI agents. It demonstrates the power of hierarchical agent-based task management, where agents take on different roles to complete complex tasks.
---

## **Project Overview**

The goal of this project is to simulate a dynamic workflow that involves multiple AI agents to:
- Analyze a task request.
- Generate relevant data (e.g., stock price information).
- Write, execute, and refine Python code to extract and analyze the data.
- Generate a blog post in **Markdown format**.
- Collect and incorporate user feedback to refine the output.

---

## **Project Structure**

```
CREWONE/
│
├── src/
│   └── rdgov/
│       ├── crew.py        # Crew definition and task setup
│       ├── main.py        # Entry point to run the project
│       ├── __init__.py    # Package initialization
│       └── config/        # Configuration files (agents.yaml, tasks.yaml)
│
├── pyproject.toml         # Project metadata and dependencies
├── README.md              # Project documentation
└── output/                # Directory where Markdown blog posts are saved
```

---

## **Agents**

The following agents collaborate to complete the tasks:

1. **Admin (User Proxy)**  
   - Manages the overall workflow and collects user feedback.
   
2. **Planner**  
   - Determines the data and resources needed to complete the task.

3. **Engineer**  
   - Writes Python code to retrieve and process stock data.

4. **Executor**  
   - Executes the Python code and reports the results.

5. **Writer**  
   - Generates a Markdown-formatted blog post based on the execution results.
6. **Manager Agent**
    - Responsible for ensuring tasks are executed in the correct order.

---

## **Tasks**

The project is structured with the following tasks:

1. **Planning Task:** Analyze the task request and determine data requirements.
2. **Coding Task:** Write Python code to retrieve stock data.
3. **Execution Task:** Run the code and extract the results.
4. **Writing Task:** Generate the blog post based on the results.
5. **Feedback Task:** Request user feedback to refine the blog post.

---

## **How to Run the Project**

### **Step 1: Create the Project**
Run the following command to create a new CrewAI project template:

```bash
crewai create crew <project_name>
```

---

### **Step 2: Modify the Project Code**
Make necessary changes to the following files:
- **`tasks.yaml`**: Define tasks and expected outputs.
- **`agents.yaml`**: Define agents and their roles.
- **`crew.py`**: Set up the crew structure and process.

### ** Set the enviroment variables**

Before running your crew, make sure you have the following keys set as environment variables in your .env file:

An OpenAI API key (or other LLM API key): OPENAI_API_KEY=sk-...

---

### **Step 3: Lock and Install Dependencies**
Navigate to your project directory and install dependencies:

```bash
cd <project_name>
crewai install
```

This command locks your dependencies and installs them.

---

### **Step 4: Run the Crew**
To run your crew, execute the following command in the root of your project:

```bash
crewai run
```

---

## **Tips**

- **If you encounter issues with 'uv' or 'sync'**, run the following command to clean the cache:
  ```bash
  uv cache clean
  ```

- Use **Python 3.11** for compatibility with CrewAI.

---

## **Example Output**

```markdown
# Nvidia Stock Price Performance (April 2024)

In the past month, Nvidia's stock showed the following key performance trends:

- Opening price: $XXX
- Highest price: $XXX
- Lowest price: $XXX
- Closing price: $XXX

## Insights and Analysis

The stock demonstrated significant growth due to...
```

---

## **Configuration**

The project uses YAML configuration files located in the `config/` directory:

- **`agents.yaml`**: Defines agent roles, goals, and responsibilities.
- **`tasks.yaml`**: Defines tasks, expected outputs, and task dependencies.

---

## **Contributing**

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

---

## **License**

This project is licensed under the [MIT License](LICENSE).

---

## **Contact**

For questions or support, please contact:

**Project Owner:** Edilma Riano  

```
---

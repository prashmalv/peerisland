# This is SakilaProject Codebase Analyzer (LLM-Powered)

## 🎯 Objective

This project analyzes the [SakilaProject](https://github.com/jOOQ/jOOQ/tree/main/jOOQ-examples/jOOQ-sakila) codebase using OpenAI's GPT-4 via LangChain. 

It extracts structured knowledge about the code including:

- High-level summaries
- Key methods and their signatures
- Detected design patterns
- Complexity ratings
- Code improvement recommendations


## 🛠️ Tech Stack

| Component         | Usage                                           |
|------------------|--------------------------------------------------|
| Python            | Primary programming language                    |
| LangChain         | LLM integration and orchestration               |
| OpenAI GPT-4      | Language model for code comprehension           |
| tiktoken          | Token-level chunking of code                    |
| dotenv            | Securely load OpenAI API key from `.env`        |



## 🧩 Folder Structure

peerisland/
├── code_loader.py # Recursively loads relevant code files
├── chunker.py # Token-aware code chunking (uses tiktoken)
├── llm_agent.py # Interacts with OpenAI LLM to extract insights
├── extractor.py # Main pipeline to process and extract summaries
├── output.json # Final structured result from the LLM
├── .env # Contains OPENAI_API_KEY
├── requirements.txt # All dependencies listed
└── README.md # This file

## How to Run

### 1. Setup Virtual Environment

bash>python -m venv venv
source venv/Scripts/activate  # Use .\venv\Scripts\Activate.ps1 on PowerShell
pip install -r requirements.txt

Place your openai api key in .env file

Run the Extraction - python extractor.py

The result will be saved in: output.json


## Sample Output

[
  {
    "file": "src/main/java/com/sparta/.../FilmController.java",
    "analysis": {
      "summary": "Handles film CRUD operations",
      "methods": [
        {
          "name": "getAllFilms",
          "params": [],
          "returns": "List<Film>"
        }
      ],
      "design_patterns": ["Controller", "MVC"],
      "complexity": "Medium",
      "recommendations": "Refactor repeated code blocks into reusable methods"
    }
  }
]




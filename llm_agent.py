import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Load API key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the GPT model (you can switch to gpt-3.5-turbo if needed)
llm = ChatOpenAI(
    temperature=0,
    model="gpt-4",
    openai_api_key=OPENAI_API_KEY
)

def analyze_code_chunk(chunk):
    """
    Sends a code chunk to the LLM and returns structured JSON-like summary.
    """
    prompt = f"""
You are a senior software engineer.

Analyze the following Java code chunk and provide a structured JSON output with:
- summary: A short summary of the file/chunk
- methods: List of method names with parameters and return types (if found)
- design_patterns: Any observed design pattern(s) or architecture (if any)
- complexity: Subjective complexity estimate (Low/Medium/High)
- recommendations: Suggestions to improve (if any)

Code chunk from file: {chunk['path']}:

{chunk['content']}
"""
    response = llm([HumanMessage(content=prompt)])
    return response.content


# Optional test block
if __name__ == "__main__":
    from code_loader import load_code_from_directory
    from chunker import split_code_to_chunks

    code_files = load_code_from_directory(r"C:\Codebase\codeEval\sakillaCode\SakilaProject")
    chunks = split_code_to_chunks(code_files, max_tokens=3000)
    
    print("\n🔍 Sample LLM response:\n")
    print(analyze_code_chunk(chunks[0]))
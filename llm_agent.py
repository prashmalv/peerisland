import os
import json
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo",  # or gpt-4 if your key supports it
    openai_api_key=OPENAI_API_KEY
)

def analyze_code_chunk(chunk):
    """
    Sends a code chunk to the LLM and returns structured JSON-like summary.
    """
    prompt = f"""
        You are a senior software architect.

        Analyze the following Java code chunk and provide a structured JSON output with:
        - summary: A short summary of the file/chunk
        - methods: List of method names with parameters and return types (if found)
        - design_patterns: Any observed design pattern(s) or architecture (if any)
        - complexity: Subjective complexity estimate (Low/Medium/High)
        - recommendations: Suggestions to improve (if any)

        Code chunk from file: {chunk['path']}:
        {chunk['content']}
    
        IMPORTANT: Return only a valid JSON object. Do not include any commentary or explanation.

    """
    try:
        response = llm.invoke([HumanMessage(content=prompt)])  # ✅ use invoke()
        response_text = response.content                       # ✅ extract message text

        return json.loads(response_text)                       # ✅ parse JSON from string

    except json.JSONDecodeError:
        return {
            "raw_response": response_text,
            "note": "Response was not valid JSON"
        }


# Optional test block
if __name__ == "__main__":
    from code_loader import load_code_from_directory
    from chunker import split_code_to_chunks

    code_files = load_code_from_directory(r"C:\Codebase\codeEval\sakillaCode\SakilaProject")
    chunks = split_code_to_chunks(code_files, max_tokens=3000)
    
    print("\n🔍 Sample LLM response:\n")
    print(analyze_code_chunk(chunks[0]))

import json
import time
from code_loader import load_code_from_directory
from chunker import split_code_to_chunks
from llm_agent import analyze_code_chunk

def safe_analyze(chunk, retries=3):
    """
    Handles retries and connection errors during LLM analysis.
    """
    for attempt in range(retries):
        try:
            return analyze_code_chunk(chunk)
        except Exception as e:
            print(f"⚠️ Attempt {attempt+1} failed for {chunk['path']}: {e}")
            time.sleep(2 * (attempt + 1))  # exponential backoff
    return {
        "error": "Connection failed after retries"
    }

def run_extraction(project_path, output_file="output.json"):
    print("📥 Loading code files...")
    code_files = load_code_from_directory(project_path)

    print("🔀 Splitting files into LLM-friendly chunks...")
    chunks = split_code_to_chunks(code_files, max_tokens=3000)

    structured_data = []

    for idx, chunk in enumerate(chunks):
        print(f"\n🤖 Analyzing chunk {idx + 1}/{len(chunks)} from {chunk['path']}...")

        response = safe_analyze(chunk)

        structured_data.append({
            "file": chunk["path"],
            "analysis": response
        })

        # 💾 Save after each successful chunk to avoid total loss
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(structured_data, f, indent=2)

    print(f"\n✅ Extraction complete. Output saved to {output_file}")

# Entry point
if __name__ == "__main__":
    project_dir = r"C:\Codebase\codeEval\sakillaCode\SakilaProject"
    run_extraction(project_dir, output_file="output.json")

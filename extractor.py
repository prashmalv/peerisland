import json
from code_loader import load_code_from_directory
from chunker import split_code_to_chunks
from llm_agent import analyze_code_chunk

def run_extraction(project_path, output_file="output.json"):
    print("📥 Loading code files...")
    code_files = load_code_from_directory(project_path)

    print("🔀 Splitting files into LLM-friendly chunks...")
    chunks = split_code_to_chunks(code_files, max_tokens=3000)

    structured_data = []

    for idx, chunk in enumerate(chunks):
        print(f"🤖 Analyzing chunk {idx + 1}/{len(chunks)} from {chunk['path']}...")

        try:
            response = analyze_code_chunk(chunk)
            structured_data.append({
                "file": chunk["path"],
                "analysis": response
            })

        except Exception as e:
            print(f"❌ Error processing {chunk['path']}: {e}")

    print(f"\n💾 Saving output to {output_file} ...")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(structured_data, f, indent=2)

    print("✅ Extraction complete!")

# Entry point
if __name__ == "__main__":
    project_dir = r"C:\Codebase\codeEval\sakillaCode\SakilaProject"
    run_extraction(project_dir, output_file="output.json")

import tiktoken

def split_code_to_chunks(code_files, max_tokens=3000, model="gpt-4"):
    encoder = tiktoken.encoding_for_model(model)
    chunks = []

    for file in code_files:
        content = file["content"]
        tokens = encoder.encode(content)

        for i in range(0, len(tokens), max_tokens):
            chunk_text = encoder.decode(tokens[i:i+max_tokens])
            chunks.append({
                "path": file["path"],
                "content": chunk_text
            })

    print(f"✅ Total Chunks Created: {len(chunks)}")
    return chunks


# Optional test
if __name__ == "__main__":
    from code_loader import load_code_from_directory
    test_dir = r"C:\Codebase\codeEval\sakillaCode\SakilaProject"
    code_files = load_code_from_directory(test_dir)
    split_code_to_chunks(code_files)

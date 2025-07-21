import ollama

def extract_introduction(raw_text: str, model: str = "phi3") -> str:
    prompt = (
        "Extract only the 'Introduction' section from the academic paper below. "
        "End extraction at the next major section:\n\n"
        f"{raw_text}"
    )
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()

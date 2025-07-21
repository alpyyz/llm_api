import ollama

def summarize(text: str, model: str = "phi3") -> str:
    prompt = f"Summarize the following academic text:\n\n{text}"
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()

import ollama

def write_article(topic: str, model: str = "phi3") -> str:
    prompt = f"Write an academic article about: {topic}"
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()

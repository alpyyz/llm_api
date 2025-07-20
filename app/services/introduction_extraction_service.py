import openai

def extract_introduction(raw_text: str) -> str:
    prompt = (
        "Extract only the 'Introduction' section from the academic paper below. "
        "End extraction at the next major section:\n\n"
        f"{raw_text}"
    )
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=2048
    )
    return response.choices[0].message.content.strip()

def get_embedding(text: str) -> list:
    response = openai.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

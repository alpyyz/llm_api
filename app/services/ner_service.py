from app.services.gpt_client import call_gpt

def extract_entities(text):
    prompt = f"""
    Extract all named entities from the following text and return as a JSON list, each with type (PERSON, ORG, LOCATION, etc) and value:
    {text}
    """
    return call_gpt(prompt)

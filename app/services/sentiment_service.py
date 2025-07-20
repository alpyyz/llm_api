from app.services.gpt_client import call_gpt

def analyze_sentiment(text):
    prompt = f"""
    Analyze the sentiment of the following text and reply with only one word: Positive, Negative, or Neutral.
    {text}
    """
    return call_gpt(prompt)

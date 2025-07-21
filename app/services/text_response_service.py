import ollama
import yaml

with open("app/agent_config.yaml") as ff:
    info = yaml.safe_load(ff)["text_generating_agents"]


def extract_introduction(raw_text: str, service: str, model: str = "phi3") -> str:
    
    prompt = f"{info[service]["input"]}{raw_text}"
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content'].strip()

import openai
import psycopg2
import yaml
from psycopg2.extras import DictCursor
from app.services.introduction_extraction_service import extract_introduction, get_embedding

with open("config.yaml") as ff:
    info = yaml.safe_load(ff)
    
openai.api_key = f"{info['gpt_api_key']}"  # Set your key
DB_CONFIG = {
    "dbname": "academic_papers",
    "user": f"{info["db_info"]['username']}",
    "password": f"{info["db_info"]['password']}",
    "host": "localhost"
}


def fetch_papers():
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("SELECT id, raw FROM all_papers WHERE introduction_text IS NULL LIMIT 100;")
            return cur.fetchall()

def update_paper(paper_id, introduction_text, embedding):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE all_papers
                SET introduction_text = %s, introduction_embedding = %s
                WHERE id = %s
            """, (introduction_text, embedding, paper_id))
            conn.commit()

def extract_introduction(raw_text):
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

def get_embedding(text):
    response = openai.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

def process():
    papers = fetch_papers()
    for paper in papers:
        paper_id, raw_text = paper['id'], paper['raw']
        try:
            intro = extract_introduction(raw_text, model="phi3")
            embedding = get_embedding(intro, model="nomic-embed-text")
            update_paper(paper_id, intro, embedding)
            print(f"Updated paper {paper_id}")
        except Exception as e:
            print(f"Error processing paper {paper_id}: {e}")

if __name__ == "__main__":
    process()

from fastapi import FastAPI
from app.routers import ner, clustering, html_parser, sentiment, introduction_extraction

app = FastAPI(title="LLM Extended API")

app.include_router(ner.router, prefix="/ner", tags=["NER"])
app.include_router(clustering.router, prefix="/cluster", tags=["Clustering"])
app.include_router(html_parser.router, prefix="/html", tags=["HTML Understanding"])
app.include_router(sentiment.router, prefix="/sentiment", tags=["Sentiment Analysis"])
app.include_router(introduction_extraction.router, prefix="/introduction_extraction", tags=["Introduction Extraction"])

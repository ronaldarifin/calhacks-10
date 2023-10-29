from dotenv import load_dotenv
import os
from convex import ConvexClient

# my libraries
from embed import get_embed

load_dotenv(".env")

client = ConvexClient(os.getenv("CONVEX_URL"))

def query():
    username = input("Type in username: ")
    print(client.query("resume:get_resume", {"username" : username}))

def test_vector_search(text, user):
    text_embedding = get_embed(text)
    print(client.query("resume:get_similar_resumes", {"description_embedding": text_embedding, "username": user}))
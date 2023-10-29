from dotenv import load_dotenv
import os
from convex import ConvexClient
import json

# my libraries
from embed import get_embed

load_dotenv("../.env")

client = ConvexClient(os.getenv("CONVEX_URL"))

def query():
    username = input("Type in username: ")
    print(client.query("resume:get_resume", {"username" : username}))

def test_vector_search(text, user):
    text_embedding = get_embed(text).numpy()[0].tolist()
    json_array = json.dumps(text_embedding)
    print(client.action("resume:get_similar_resumes", {"description_embedding": json_array, "username": user}))

test_vector_search("job posting about creating the front end of an application", "test_user")
# query()
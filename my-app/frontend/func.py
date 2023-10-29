import openai
import extract_description as extract

from convex import ConvexClient
from dotenv import load_dotenv
import os
import json

from embed import *
load_dotenv("../.env")
client = ConvexClient(os.getenv("CONVEX_URL"))
api_key = os.getenv("OPENAI_KEY")
api_key = ''
jsonFormat = """
    {... include name, location, email, phone, links, education, and skills
    "work experience": [
        {
            "employer": "Tokenized",
            "position": "Senior Javascript Developer",
            "location": "Melbourne",
            "summary": "Tokenized is a Bitcoin wallet for issuing, managing and trading digital tokens. I built out the front end which was packaged as an electron app. It was a difficult frontend to build because we store the users keys locally and used them to sign transactions and contracts.",
            "website": "https://tokenized.com/",
            "startDate": "2020-05-05",
            "highlights": ["React", "Redux", "SCSS", "Product"]
        },
        ... // And so on for the rest of the objects
        ... we only care about "work experience and projects only"
    ]
}
"""

## create function here that takes resume and job posting
def query():
    username = input("Type in username: ")
    return client.query("resume:get_resume", {"username" : username})


def similarity_search(job_description):
    text_embedding = get_embed(job_description).numpy()[0].tolist()
    json_array = json.dumps(text_embedding)
    user = "test_user"
    output = client.action("resume:get_similar_resumes", {"description_embedding": json_array, "username": user})
    summaries = []
    for entry in output:
        summaries.append(entry["summary"])
    return summaries


# Takes cv and job description
# executes json parsing and embeddings. for each element of json, insert into convex
def input_processing(cv_content, job_description, username):
    # uncomment this when we have the json format
    # json_in_resume = cvToJson(cv_content, jsonFormat)
    # json_in_resume
    f = open("sample_json.json", "r")
    json_in_resume = json.loads(f.read())
    f.close()
    
    entry = {}
    employee = json_in_resume["name"]
    employer = json
    for category in json_in_resume:
        if category == "work experience" or category == "projects":
            experiences = extract.get_experience_in_category(json_in_resume, category)
            for exp in experiences:
                
                print("1")
            print("1")

    
    

    #add rows to resume_json_table and data_experiences
    # cv_json = cvToJson(cv_content)
    # cv_json
    insert_row = str({"username": "test_user", "resume_json": json_in_resume})
    client.mutation("cv_table:insert_cv", {"text": insert_row})
    experiences = add_embed(json_in_resume, "work experience")
    for exp in experiences:
        client.query("resume:insert_experience", {"text":exp})
    
    
    
    
    return 1

input_processing("dummy", "dummy", "test_user")

# given a username, rreturn all resume entry points of the user.
# INPUT TYPE: String
# RV TYPE: List of Resume Entries
def get_resume_entries(username):
    result = client.query("resume:get_resume", {"username": username})
    return result


def executeChatGptCall(inputToGpt, token):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=inputToGpt,
        max_tokens=token,  # Adjust the number of tokens as needed
        api_key=api_key
    )
    return response.choices[0].text.strip()

def cvToJson(userCV, jsonFormat):
    inputToGpt = f"This is my CV: {userCV} Now, I want you return me a json object about my CV. I only want the json object representation like this {jsonFormat}. Nothing else just the json string."
    return executeChatGptCall(inputToGpt, 1500)

def add_embed(json_obj, category):
    experiences = extract.get_experience_in_category(json_obj, category)
    for exp in experiences:
        # summary is a string
        summary = exp.get("summary")
        exp.embedding = get_embed(summary)
    return experiences #returns a list of work experience json objects


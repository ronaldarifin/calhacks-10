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
# api_key = ''
jsonFormat = """
{... include name, location, email, phone, links, education, and skills
    "work experience": [
        {
            "employer": ...,
            "position": ...,
            "location": ...,
            "summary": ...,
            "website": website if present,
            "startDate": ...,
            "endDate": ...,
            "highlights": contains a list of relevant technologies used in the experience
        },
    ]
    ... and so on for the rest of the objects
    ... we only care about "work experience and projects only"
}
"""

## create function here that takes resume and job posting
def query():
    username = input("Type in username: ")
    return client.query("resume:get_resume", {"username" : username})


def similarity_search(job_description):
    text_embedding = get_embed(job_description)
    json_array = json.dumps(text_embedding)
    user = "test_user"
    output = client.action("resume:get_similar_resumes", {"description_embedding": json_array, "username": user})
    summaries = []
    for entry in output:
        summaries.append(entry["summary"])
    return summaries


 #returns a list of work experience json objects
def add_embed(json_obj, category):
    experiences = extract.get_experience_in_category(json_obj, category)
    for exp in experiences:
        # summary is a string
        summary = exp.get("summary")
        exp["embedding"] = get_embed(summary)
    return experiences


# Takes cv and job description
# executes json parsing and embeddings. for each element of json, insert into convex
def input_processing(username="test_user", cv_content=None):
    # uncomment this when we have the json format
    useGPT = 0
    if useGPT:
        if cv_content == None or cv_content == "":
            return -1
        json_in_resume = cvToJson(cv_content, jsonFormat)
        print(json_in_resume)
        json_in_resume = json.dumps(json_in_resume)
    else:
        f = open("sample_json2.json", "r")
        json_in_resume = json.loads(f.read())
        f.close()
    
    # entry = {}
    # employee = json_in_resume["name"]
    # employer = json
    

    #add rows to resume_json_table and data_experiences
    # cv_json = cvToJson(cv_content)
    client.mutation("cv_table:insert_cv", {"username": username, "resume_json": json_in_resume})
    experiences = add_embed(json_in_resume, "work experience")
    for exp in experiences:
        exp["username"] = username
        client.mutation("resume:insert_experience", exp)    
    print("added mutations")
    
    return 0

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
    inputToGpt = f"This is my CV: {userCV} \nNow, I want you return me a json object about my CV. I only want the json object representation like this \n====================\n{jsonFormat} \nFollow the format exactly, and output just the resulting JSON object."
    print("running GPT call...")
    print(inputToGpt)
    return executeChatGptCall(inputToGpt, 1500)

import openai
import extract_description as extract

import re
from convex import ConvexClient
from dotenv import load_dotenv
import os
import json
from embed import *
load_dotenv("../.env")
client = ConvexClient(os.getenv("CONVEX_URL"))
api_key = os.getenv("OPENAI_KEY")
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
    # summaries = rewrite_resume(summaries, job_description)
    return '\n===============================\n'.join(summaries)


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
def input_processing(username="test_user", cv_content=None, option="File"):
    # uncomment this when we have the json format
    if username == "":
        username = "test_user"
    if option == "GPT":
        print("username: ", username)
        print("cv_content: \n", cv_content)
        if cv_content == None or cv_content == "":
            return -1
        json_in_resume = cvToJson(cv_content, jsonFormat)
        print(json_in_resume)
        json_in_resume = json.loads(json_in_resume)
    elif option == "File":
        f = open("sample_json3.json", "r")
        json_in_resume = json.loads(f.read())
        f.close()
    else:
        json_in_resume = json.loads(cv_content)
    
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
    print("getting gpt completion...")
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=inputToGpt,
        max_tokens=token,  # Adjust the number of tokens as needed
        api_key=api_key
    )
    print("gpt full response", response)
    return response.choices[0].text.strip()

def cvToJson(userCV, jsonFormat):
    inputToGpt = f"This is my CV:\n {userCV} \n====================\nInstrucition: Now, I want you return me a json object about my CV. I only want the json object representation like this \n{jsonFormat} \nFollow the format exactly, and output just the resulting JSON object."
    print("running GPT call...")
    print("gpt input......\n", inputToGpt)
    gpt_completion = executeChatGptCall(inputToGpt, 1500)
    print("gpt output.....\n", gpt_completion)
    gpt_completion = re.sub(r"```\n*.*$", "", gpt_completion)
    gpt_completion = re.sub(r".*\n+```json", "", gpt_completion)
    return gpt_completion

# original is a list of resume summaries
def rewrite_resume(original, job_desc):
    new_summaries = []
    for point in original:
        inputToGpt = f"I'm looking at this job description: \n{job_desc}\n ================ The following is the contents of my resume: \n{point}\n================== Instruction: I need your help to rewrite it in the same format, using at most 4 points and make it a better fit for the given job description"
        # inputToGpt = point(point)
        new_summary = executeChatGptCall(inputToGpt, 100)
        new_summaries.append(new_summary)
    return new_summaries
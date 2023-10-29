import openai
# import embed as e
import json
import extract_description as extract
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

# Takes cv and job description
# executes json parsing and embeddings. for each element of json, insert into convex
def input_processing(cv_content, job_description, username):
    # uncomment this when we have the json format
    # json_in_resume = cvToJson(cv_content, jsonFormat)
    with open('sample_json.json') as json_file:
        json_in_resume = json.load(json_file)
    print(json_in_resume)
    employee = json_in_resume["name"]
    # employer = json
    # print(cv_content, job_description, username)
    # for category in json_in_resume:
    #     if category == "work experience" or category == "projects":
    #         print(json_in_resume[category])
    #         # for job in json_in_resume[category]:
    #         #     job["embedding"] = e.get_embed(job["summary"])


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

# def get_embed(json_obj):
#     experiences = extract.get_work_experiences(json_obj)
#     for exp in experiences:
#         # summary is a string
#         summary = exp.get("summary")
#         # what is e?
#         exp.embedding = e.get_embed(summary)
#     return experiences #returns a list of work experience json objects


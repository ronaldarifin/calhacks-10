import json

def get_experience_in_category(data, category):
    result = data.get("category", [])
    print(result)
    return result

def get_summaries(json_lst):
    result = []
    for exp in json_lst:
        result.append(exp.get("summary"))
    return result

if __name__ == "__main__":
    json_lst = get_experience_in_category('sample_json.json', "work experience")
    
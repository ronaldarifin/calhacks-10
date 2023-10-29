import json

def get_work_experiences(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    result = data.get("work experience", [])
    print(result)
    return result

def get_summaries(json_lst):
    result = []
    for exp in json_lst:
        result.append(exp.get("summary"))
    return result

if __name__ == "__main__":
    json_lst = get_work_experiences('sample_json.json')
    
import json

result = """
{
    "name": "Matthew Kao",
    "location": "Berkeley, CA",
    "email": "matthewkao@berkeley.edu",
    "phone": "(925)-435-9524",
    "links": {
        "GitHub": "https://github.com/Matthew-Kao",
        "LinkedIn": "www.linkedin.com/in/mattkao"
    },
    "education": {
        "university": "University of California, Berkeley",
        "degree": "B.A. Computer Science",
        "graduationDate": "May 2023",
        "GPA": "3.7"
    },
    "skills": {
        "languages": [
            "Python",
            "C++",
            "C",
            "Java",
            "Javascript",
            "Ruby",
            "Dart"
        ],
        "front-end": [
            "HTML5",
            "CSS3",
            "Javascript",
            "React.js",
            "React Native",
            "Flutter"
        ]
    },
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
        {
            "employer": "ACME Corp",
            "position": "Software Engineer",
            "location": "San Francisco",
            "summary": "ACME Corp is a small start-up working on a new product. I was the only engineer on the team and was responsible for the full stack development of the product.",
            "website": "https://www.acmecorp.com/",
            "startDate": "2019-04-01",
            "endDate": "2020-03-31",
            "highlights": ["Python", "Django", "Postgres", "AWS"]
        }
    ],
    "projects": [
        {
            "name": "Action Map",
            "techStack": [
                "Ruby",
                "Model-View-Controller (MVC)",
                "CSS",
                "JavaScript",
                "Rspec Tests",
                "Cucumber Scenarios"
            ],
            "startDate": "2023-01-01",
            "endDate": "2023-05-31",
            "description": "Action Map is a web application that displays the US Map where the states and counties are clickable. When clicked, it will show the political candidates for that area. The purpose of this project was to allow users to visualize the political environment within all levels of government."
        },
        {
            "name": "Pacman",
            "techStack": [
                "Python",
                "BFS",
                "DFS",
                "A*",
                "Monte Carlo Tree Search",
                "Reinforcement Learning"
            ],
            "startDate": "2022-08-01",
            "endDate": "2022-12-31",
            "description": "Pacman is a classic video game where the goal is to collect as many points as possible while avoiding ghosts. The purpose of this project was to develop an AI agent that can play the game optimally and collect the most points."
        }
    ]
}
"""


def print_neatly(json_string):
    data = json.loads(json_string)
    pretty_data = json.dumps(data, indent=6)
    print(pretty_data)

print_neatly(result)

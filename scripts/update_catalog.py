import requests
import json
import os

LEETCODE_URL = "https://leetcode.com/api/problems/all/"

def update_catalog():
    print("Fetching all problems from LeetCode... (this may take a few seconds)")
    response = requests.get(LEETCODE_URL)
    if response.status_code != 200:
        print("Failed to fetch problems.")
        return

    data = response.json()
    problems = []
    
    for p in data['stat_status_pairs']:
        problems.append({
            "id": p['stat']['frontend_question_id'],
            "title": p['stat']['question__title'],
            "slug": p['stat']['question__title_slug'],
            "difficulty": {1: "Easy", 2: "Medium", 3: "Hard"}[p['difficulty']['level']]
        })
    
    # Sort by ID
    problems.sort(key=lambda x: int(x['id']))
    
    with open("problems.json", "w") as f:
        json.dump(problems, f, indent=2)
    
    print(f"Catalog updated! {len(problems)} problems saved to problems.json")

if __name__ == "__main__":
    update_catalog()

import os
import requests
import json
import argparse
import re

LEETCODE_URL = "https://leetcode.com/graphql"

QUERY = """
query getQuestionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    difficulty
    content
    codeSnippets {
      lang
      langSlug
      code
    }
  }
}
"""

def fetch_problem(title_slug):
    variables = {"titleSlug": title_slug}
    response = requests.post(LEETCODE_URL, json={'query': QUERY, 'variables': variables})
    if response.status_code == 200:
        return response.json()['data']['question']
    return None

def create_problem_files(problem):
    difficulty = problem['difficulty']
    id = problem['questionFrontendId']
    title = problem['title']
    title_slug = problem['titleSlug']
    
    # Format folder name: ID_Title (e.g., 1_TwoSum)
    safe_title = re.sub(r'[^a-zA-Z0-9]', '', title.replace(' ', ''))
    folder_name = f"P{id}_{safe_title}"
    target_dir = os.path.join("Sources", difficulty, folder_name)
    
    os.makedirs(target_dir, exist_ok=True)
    
    # Find Swift snippet
    swift_snippet = next((s['code'] for s in problem['codeSnippets'] if s['langSlug'] == 'swift'), "// No Swift snippet found")
    
    content = f"""/**
 * Problem: {id}. {title}
 * Difficulty: {difficulty}
 * Topic: 
 *
 * Complexity:
 * - Time: O(?)
 * - Space: O(?)
 *
 * Notes:
 * 
 */

import Foundation

{swift_snippet}
"""
    
    file_path = os.path.join(target_dir, f"{folder_name}.swift")
    with open(file_path, "w") as f:
        f.write(content)
    
    print(f"Created {file_path}")
    
    # Create Test file
    test_dir = os.path.join("Tests", difficulty)
    os.makedirs(test_dir, exist_ok=True)
    test_file_path = os.path.join(test_dir, f"{folder_name}Tests.swift")
    
    # Extract class name from snippet if possible, default to folder_name
    class_match = re.search(r'class\s+(\w+)', swift_snippet)
    class_name = class_match.group(1) if class_match else folder_name
    
    test_content = f"""import XCTest
@testable import LeetCode

final class {folder_name}Tests: XCTestCase {{
    func testSolution() {{
        // let solution = {class_name}()
        // XCTAssertEqual(...)
    }}
}}
"""
    with open(test_file_path, "w") as f:
        f.write(test_content)
    
    print(f"Created {test_file_path}")

def get_slug_by_id(problem_id):
    if not os.path.exists("problems.json"):
        print("problems.json not found. Run 'python3 scripts/update_catalog.py' first.")
        return None
    
    with open("problems.json", "r") as f:
        problems = json.load(f)
        for p in problems:
            if str(p['id']) == str(problem_id):
                return p['slug']
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch LeetCode problem details")
    parser.add_argument("--url", help="LeetCode problem URL")
    parser.add_argument("--id", help="LeetCode problem ID")
    args = parser.parse_args()
    
    slug = None
    if args.url:
        # Security: Basic URL sanitization
        if not args.url.startswith("https://leetcode.com/"):
            print("Security Error: Only official LeetCode URLs are allowed.")
            exit(1)
        match = re.search(r'problems/([^/]+)', args.url)
        if match:
            slug = match.group(1)
    elif args.id:
        # Security: Ensure ID is numeric to prevent injection/traversal
        if not args.id.isdigit():
            print("Security Error: Problem ID must be a number.")
            exit(1)
        slug = get_slug_by_id(args.id)
        if not slug:
            print(f"Problem ID {args.id} not found in catalog.")
    
    if slug:
        try:
            problem = fetch_problem(slug)
            if problem:
                create_problem_files(problem)
            else:
                print("Problem not found.")
        except Exception as e:
            print(f"Network or Processing Error: {str(e)}")
    else:
        print("Please provide a --url or a valid --id (after running ./leet catalog).")

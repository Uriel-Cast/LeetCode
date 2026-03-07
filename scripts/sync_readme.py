import os
import re

README_TEMPLATE = """# LeetCode - Swift Edition

A professional, scalable, and automated repository for LeetCode solutions in Swift.

## Automation

### Fetch and Generate
Use the script to automatically fetch problem details and code snippets:
```bash
python3 scripts/fetch_problem.py --url https://leetcode.com/problems/two-sum/
```

### Sync README
Update this progress table automatically:
```bash
python3 scripts/sync_readme.py
```

## Progress Overview

| # | Problem | Difficulty | Solution | Time | Space |
|---|---------|-------------|----------|------|-------|
{table_content}

## Testing
Run all tests:
```bash
swift test
```
"""

def sync_readme():
    table_rows = []
    sources_dir = "Sources"
    difficulties = ["Easy", "Medium", "Hard"]
    
    for diff in difficulties:
        diff_path = os.path.join(sources_dir, diff)
        if not os.path.exists(diff_path):
            continue
            
        folders = sorted(os.listdir(diff_path))
        for folder in folders:
            if "_" not in folder:
                continue
            
            problem_id, problem_name = folder.split("_", 1)
            swift_file = os.path.join(diff_path, folder, f"{folder}.swift")
            
            if not os.path.exists(swift_file):
                continue
            
            # Extract complexity from file
            with open(swift_file, "r") as f:
                content = f.read()
                time_complex = re.search(r'- Time: (.*)', content)
                space_complex = re.search(r'- Space: (.*)', content)
                
                time = time_complex.group(1).strip() if time_complex else "O(?)"
                space = space_complex.group(1).strip() if space_complex else "O(?)"

            solution_link = f"[{folder}.swift]({sources_dir}/{diff}/{folder}/{folder}.swift)"
            table_rows.append(f"| {problem_id} | {problem_name} | {diff} | {solution_link} | {time} | {space} |")

    # Sort by ID
    table_rows.sort(key=lambda x: int(x.split("|")[1].strip()))
    
    readme_content = README_TEMPLATE.format(table_content="\n".join(table_rows))
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    
    print("README.md updated successfully.")

if __name__ == "__main__":
    sync_readme()

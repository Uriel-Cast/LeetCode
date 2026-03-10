# LeetCode - Swift Edition

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

> [!NOTE]
> All problem-related identifiers (folders, files, classes) are prefixed with `P` (e.g., `P1_TwoSum`) because Swift identifiers cannot start with a number.

## Progress Overview

| # | Problem | Difficulty | Solution | Time | Space |
|---|---------|-------------|----------|------|-------|
| 9 | PalindromeNumber | Easy | [P9_PalindromeNumber.swift](Sources/Easy/P9_PalindromeNumber/P9_PalindromeNumber.swift) | O(?) | O(?) |

## Testing
Run all tests:
```bash
swift test
```

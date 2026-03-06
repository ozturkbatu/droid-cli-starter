#!/usr/bin/env python3
"""
Validate code changes before commits
This hook runs before file edits to ensure quality standards

Usage: Configure in .factory/settings.json under PreToolUse hook
"""

import json
import sys
import re

def validate_file_path(file_path: str) -> list[str]:
    """Validate file path and return list of issues"""
    issues = []
    
    # Block sensitive files
    sensitive_patterns = [
        r'\.env',
        r'\.git/',
        r'node_modules/',
        r'\.secret',
        r'id_rsa',
        r'\.pem$'
    ]
    
    for pattern in sensitive_patterns:
        if re.search(pattern, file_path):
            issues.append(f"Cannot modify sensitive file: {file_path}")
            break
    
    return issues

def validate_content(content: str, file_path: str) -> list[str]:
    """Validate file content and return list of issues"""
    issues = []
    
    # Check for potential secrets
    secret_patterns = [
        (r'password\s*=\s*["\'][^"\']+["\']', "Potential password in code"),
        (r'api[_-]?key\s*=\s*["\'][^"\']+["\']', "Potential API key in code"),
        (r'secret\s*=\s*["\'][^"\']+["\']', "Potential secret in code"),
        (r'token\s*=\s*["\'][^"\']+["\']', "Potential token in code"),
    ]
    
    for pattern, message in secret_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append(f"⚠️  {message}")
    
    return issues

def main():
    try:
        # Read JSON input from stdin
        input_data = json.load(sys.stdin)
        
        tool_name = input_data.get("tool_name", "")
        tool_input = input_data.get("tool_input", {})
        
        # Only validate Edit and Create operations
        if tool_name not in ["Edit", "Create"]:
            sys.exit(0)
        
        file_path = tool_input.get("file_path", "")
        content = tool_input.get("content", "") or tool_input.get("new_str", "")
        
        if not file_path:
            sys.exit(0)
        
        # Validate file path
        path_issues = validate_file_path(file_path)
        if path_issues:
            for issue in path_issues:
                print(issue, file=sys.stderr)
            sys.exit(2)  # Exit code 2 blocks the operation
        
        # Validate content
        content_issues = validate_content(content, file_path)
        if content_issues:
            for issue in content_issues:
                print(issue, file=sys.stderr)
            # Warning only, don't block
            sys.exit(0)
        
        sys.exit(0)
        
    except Exception as e:
        print(f"Hook error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

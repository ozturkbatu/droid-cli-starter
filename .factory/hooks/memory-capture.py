#!/usr/bin/env python3
"""
Automatic memory capture hook for Factory Droid CLI
Captures messages starting with # and saves to memories.md

Usage:
  # <content>     → Saves to project memories (.factory/memories.md)
  ## <content>    → Saves to personal memories (~/.factory/memories.md)

Examples:
  "# we use PostgreSQL for better ACID compliance"
  "## I prefer functional programming patterns"
"""

import json
import sys
import os
from datetime import datetime

def main():
    try:
        data = json.load(sys.stdin)
        prompt = data.get('prompt', '').strip()

        if not prompt.startswith('#'):
            # Not a memory capture, pass through
            sys.exit(0)

        # ## = personal, # = project
        if prompt.startswith('##'):
            content = prompt[2:].strip()
            mem_file = os.path.expanduser('~/.factory/memories.md')
            scope = 'personal'
        else:
            content = prompt[1:].strip()
            project_dir = os.environ.get('FACTORY_PROJECT_DIR', os.getcwd())
            project_factory = os.path.join(project_dir, '.factory')
            if os.path.exists(project_factory):
                mem_file = os.path.join(project_factory, 'memories.md')
                scope = 'project'
            else:
                # Fallback to personal if no .factory/ directory
                mem_file = os.path.expanduser('~/.factory/memories.md')
                scope = 'personal (no project .factory/ found)'

        if content:
            timestamp = datetime.now().strftime('%Y-%m-%d')
            
            # Ensure the directory exists
            os.makedirs(os.path.dirname(mem_file), exist_ok=True)
            
            # Create file if it doesn't exist
            if not os.path.exists(mem_file):
                with open(mem_file, 'w') as f:
                    f.write(f"# Memories\n\n")
            
            # Append the memory
            with open(mem_file, 'a') as f:
                f.write(f"- [{timestamp}] {content}\n")

            # Return success message
            output = {
                'systemMessage': f'✓ Memory saved to {scope} memories'
            }
            print(json.dumps(output))
            sys.exit(0)

    except Exception as e:
        # Silent fail - don't break the workflow
        pass

if __name__ == '__main__':
    main()

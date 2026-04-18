#!/usr/bin/env python3
"""
Configuration Validation Script
Validates network configuration files for common issues
"""

import os
import sys
import re
def validate_config(filename):
    """Validate a configuration file"""
    print(f"Validating {filename}...")
    
    with open(filename, 'r') as f:
        content = f.read()
    
    issues = []
    
    # Check for hostname
    if not re.search(r'^hostname\s+\S+', content, re.MULTILINE):
        issues.append("Missing hostname configuration")
    
    # Check for enable secret
    if not re.search(r'^enable secret', content, re.MULTILINE):
        issues.append("Missing enable secret")
    
    if issues:
        print("❌ Validation failed:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("✅ Validation passed!")
        return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_config.py <config-file>")
        sys.exit(1)
    
    result = validate_config(sys.argv[1])
    sys.exit(0 if result else 1)

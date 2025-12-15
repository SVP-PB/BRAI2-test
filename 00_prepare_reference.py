#!/usr/bin/env python3
"""
00_prepare_reference.py - Test script for BRAI framework
Simulates reference preparation step with 8-second execution time
"""
import time
import json
from utils.config import CONFIG


def main():
    print("=" * 60)
    print("00_prepare_reference.py - Starting execution")
    print("=" * 60)

    # Print the entire CONFIG contents
    print("\n[CONFIG Contents]:")
    print(json.dumps(CONFIG, indent=4, ensure_ascii=False))

    # Access specific config values
    print("\n[Accessing CONFIG values]:")
    if "reference" in CONFIG:
        print(f"  - reference: {CONFIG['reference']}")
    if "reference_file" in CONFIG:
        print(f"  - reference_file: {CONFIG['reference_file']}")

    # Simulate long-running execution (8 seconds)
    print("\n[Simulating long-running execution...]")
    for i in range(8):
        print(f"  Processing... {i+1}/8 seconds elapsed")
        time.sleep(1)

    print("\n[00_prepare_reference.py completed successfully]")
    print("=" * 60)


if __name__ == "__main__":
    main()

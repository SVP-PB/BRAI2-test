#!/usr/bin/env python3
"""
02_alignment.py - Test script for BRAI framework
Simulates alignment step with 8-second execution time
"""
import time
import json
import os
from utils.config import CONFIG

SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]


def main():
    print("=" * 60)
    print("02_alignment.py - Starting execution")
    print("=" * 60)

    # Print the entire CONFIG contents
    print("\n[CONFIG Contents]:")
    print(json.dumps(CONFIG, indent=4, ensure_ascii=False))

    # Access specific config values
    print("\n[Accessing CONFIG values]:")
    if "reference" in CONFIG:
        print(f"  - reference: {CONFIG['reference']}")
    if "bwa_dir" in CONFIG:
        print(f"  - bwa_dir: {CONFIG['bwa_dir']}")
    if "samtools_dir" in CONFIG:
        print(f"  - samtools_dir: {CONFIG['samtools_dir']}")

    # Simulate long-running execution (8 seconds)
    print("\n[Simulating long-running execution...]")
    for i in range(8):
        print(f"  Aligning... {i+1}/8 seconds elapsed")
        time.sleep(1)

    # Create output txt file in outDir
    if "outDir" in CONFIG:
        out_dir = CONFIG["outDir"]
        os.makedirs(out_dir, exist_ok=True)
        output_file = os.path.join(out_dir, f"{SCRIPT_NAME}.txt")
        with open(output_file, "w") as f:
            f.write(f"{SCRIPT_NAME} completed successfully\n")
        print(f"\n[Output file created: {output_file}]")

    print("\n[02_alignment.py completed successfully]")
    print("=" * 60)


if __name__ == "__main__":
    main()

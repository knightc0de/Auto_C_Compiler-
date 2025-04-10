#!/usr/bin/env python3
"""
Auto C Compiler for Linux

This script compiles and runs a C source file using GCC.
It provides user-friendly feedback for success or failure.

Author: Puneet Singh
GitHub: https://github.com/knightc0de
"""
import os            # Used to run system-level commands like 'gcc'
import argparse      # Used to deal with command-line arguments
import time          # Used to delay or wait for output readability

# Setting up the  parser with a helpful description
parser = argparse.ArgumentParser(description="Auto C Compiler for Linux - Compiles and runs C source code")

# Adding  arguments: source file and output binary name
parser.add_argument("src_file", help="C source file name (e.g., hello.c)")
parser.add_argument("output", help="Name of the output binary file (e.g., hello)")

# Parse the arguments and store them in the 'args' object
args = parser.parse_args()

# Compilation is starting
print("Starting compilation...\n")
time.sleep(1)  # Pause for a second for build process

# Compile the C file using gcc, redirecting output exit_code  to the specified name
exit_code = os.system(f"gcc {args.src_file} -o {args.output}")

# Check if compilation succeeded
if exit_code == 0:
    print("\nCompilation is successful ")
    time.sleep(1)  # Short pause before running the compiled binary
    os.system(f"./{args.output}")  # Run the compiled binary
else:
    print("Compilation failed !")














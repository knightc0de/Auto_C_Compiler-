#!/usr/bin/env python3
"""
Auto C Compiler for Linux

This script compiles and runs a C source file using GCC.
It provides user-friendly feedback for success or failure.

Author: @knightc0de
GitHub: https://github.com/knightc0de
"""
import os            
import argparse      
import time          


parser = argparse.ArgumentParser(description="Auto C Compiler for Linux - Compiles and runs C source code")

# Adding  arguments: source file and output binary name
parser.add_argument("src_file", help="C source file name (e.g., hello.c)")
parser.add_argument("output", help="Name of the output binary file (e.g., hello)")


args = parser.parse_args()


print("Starting compilation...\n")
time.sleep(1)  


exit_code = os.system(f"gcc {args.src_file} -o {args.output}")


if exit_code == 0:
    print("\nCompilation is successful ")
    time.sleep(1)  #
    os.system(f"./{args.output}")  
else:
    print("Compilation failed !")














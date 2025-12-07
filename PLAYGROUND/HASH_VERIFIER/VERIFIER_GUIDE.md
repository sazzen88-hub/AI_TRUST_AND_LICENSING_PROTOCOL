Hash Integrity Verifier — User Guide

This guide explains how to use the Hash Integrity Verifier tool in both
Python scripts and the command line.

1. What This Tool Does

The verifier calculates a file’s SHA-256 hash and checks whether it matches the
value you expect. This is commonly used for:

verifying downloaded files

ensuring files weren’t modified

checking integrity before sharing

2. Using It in Python
from hash_verifier import verify_file

result = verify_file("myfile.pdf", "expected_sha256_here")
print(result)


The function returns:

file_found (True/False)

match (True/False)

calculated_hash

expected_hash

3. Using It from the Command Line
python hash_verifier.py path/to/file.zip expected_hash_here


Example:

python hash_verifier.py photo.png a3c1f99d4e1b...

4. How to Generate a SHA-256 Hash Yourself

If you need the expected hash, you can calculate it manually:

Windows
certutil -hashfile file.txt SHA256

macOS / Linux
shasum -a 256 file.txt

5. Troubleshooting
File Not Found

Check that:

the path is correct

the file actually exists

you used quotes if the path has spaces

Hash Doesn’t Match

This could mean:

the file changed

the expected hash was typed incorrectly

you’re comparing the wrong file

6. Safe to Use

This tool:

performs no network operations

sends no data anywhere

reads files locally only

uses a standard hashing function
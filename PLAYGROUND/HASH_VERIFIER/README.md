# Hash Integrity Verifier

This tool verifies the integrity of any file by calculating its SHA-256 hash
and comparing it to a value provided by the user.

It is simple, transparent, and designed as a public demonstration of how
verifiable processes can improve trust in digital systems.

### Features
- Calculates SHA-256 hash of any file
- Compares against an expected hash
- Works on Windows, macOS, and Linux
- Can be imported into Python or run from the command line

### Basic Usage (Python)
```python
from hash_verifier import verify_file

result = verify_file("example.txt", "your_expected_hash_here")
print(result)

command line use
python hash_verifier.py path/to/file.txt expected_hash_here


Output Example
{
  "file_found": True,
  "match": False,
  "calculated_hash": "abcd1234...",
  "expected_hash": "ffff0000..."
}
Notes

This tool is for public experimentation and learning.

It does not contain or connect to any internal system logic.

SHA-256 is used because it is standard, open, and widely trusted.

See GUIDE.md in this folder for detailed instructions.
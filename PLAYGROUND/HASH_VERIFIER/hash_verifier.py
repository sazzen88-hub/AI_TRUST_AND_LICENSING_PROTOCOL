# Hash Integrity Verifier — Public Tool
# This tool allows users to verify file integrity using SHA-256.
# It is safe, simple, and does not reveal any internal logic.

import hashlib
import os

def calculate_sha256(file_path: str) -> str:
    """
    Calculate SHA-256 hash of a file.
    """
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def verify_file(file_path: str, expected_hash: str) -> dict:
    """
    Verifies whether the file's SHA-256 hash matches the expected hash.
    """
    if not os.path.exists(file_path):
        return {
            "file_found": False,
            "match": False,
            "calculated_hash": None,
            "expected_hash": expected_hash
        }

    calculated = calculate_sha256(file_path)

    return {
        "file_found": True,
        "match": calculated.lower() == expected_hash.lower(),
        "calculated_hash": calculated,
        "expected_hash": expected_hash
    }


# Optional CLI usage:
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Hash Integrity Verifier — Check SHA-256 of a file.")
    parser.add_argument("file", help="Path to the file you want to verify.")
    parser.add_argument("hash", help="Expected SHA-256 hash value.")
    args = parser.parse_args()

    result = verify_file(args.file, args.hash)

    print("\n--- Hash Verification Result ---")
    if not result["file_found"]:
        print("File not found.")
    else:
        print(f"Expected Hash:   {result['expected_hash']}")
        print(f"Calculated Hash: {result['calculated_hash']}")
        print("Match Status:    ", "MATCH" if result["match"] else "NO MATCH")

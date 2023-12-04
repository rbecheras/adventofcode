"""Main module."""
import os


def read_file(file_path: str) -> str:
    """Reads a file and returns its content as a string."""
    print("readFile", os.getcwd())
    with open(file_path, "+r", -1, encoding="utf-8") as f:
        content = f.read()
    return content

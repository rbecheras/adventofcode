"""Main module."""
import os


def read_file(file_path: str) -> str:
    """Reads a file and returns its content as a string."""
    with open(file_path, "+r", -1, encoding="utf-8") as f:
        content = f.read()
    return content


def calibrate(input_file_path: str) -> int:
    """Calibrates the frequency."""
    with open(file_path, "+r", -1, encoding="utf-8") as lines:
        for line in lines:
            print(line)

    return 42

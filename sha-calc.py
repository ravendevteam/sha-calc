import hashlib
import os
import tkinter as tk
from tkinter import filedialog

# Calculate
def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Process in chunks
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# File Explorer prompt
def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide root window
    file_path = filedialog.askopenfilename()  # Open file dialog
    return file_path

if __name__ == "__main__":
    file_path = select_file()
    if file_path:  # Make sure they actually selected a file
        # Calculate
        print(f"File: {file_path}")
        sha256_hash = calculate_sha256(file_path)
        print(f"SHA-256 Hash: {sha256_hash}")
        input("\nPress any key to quit...")
    else:
        print("No file selected, goober.")

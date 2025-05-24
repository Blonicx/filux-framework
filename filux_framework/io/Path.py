"""Path utilities for file operations."""

import os

from urllib.request import urlopen
from filux_framework.io.File import File

class Path:
    """A class for path utilities."""

    def __init__(self):
        pass

    def compare_files(self, path_one, path_two):
        """Compare two files by content, hash, and size."""
        file_1 = File(path_one)
        file_2 = File(path_two)
        return (
            file_1.get_file_hash() == file_2.get_file_hash() and
            file_1.file_size == file_2.file_size
        )

    def is_dir(self, file_path):
        """Checks if a File is a Folder"""
        return os.path.isdir(file_path)
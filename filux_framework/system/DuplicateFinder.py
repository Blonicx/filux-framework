import os
import filux_framework
from collections import defaultdict

class DuplicateFinder:
    def __init__(self, path):
        self.path = path
        self.files_by_size = defaultdict(list)

    def find_duplicates(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                full_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(full_path)
                    self.files_by_size[size].append(full_path)
                except Exception:
                    continue

        # Now check for hash duplicates
        duplicates = []
        for size, files in self.files_by_size.items():
            if len(files) < 2:
                continue
            hashes = defaultdict(list)
            for f in files:
                try:
                    h = filux_framework.File(f).get_file_hash()
                    hashes[h].append(f)
                except Exception:
                    continue
            for dup_list in hashes.values():
                if len(dup_list) > 1:
                    duplicates.append(dup_list)
        return duplicates

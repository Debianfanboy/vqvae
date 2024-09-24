import numpy as np
import os

class Loader():
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.total_files = 0
    def get_spectro_from_index(self, idx: int):
        """Get the spectrogram of a given index"""
        return os.listdir(self.root_dir)[idx]
    def get_split(self):
        total_files = 0
        total_data = []
        for file in os.listdir(self.root_dir):
            if os.path.isfile(file):
                total_files += 1
        self.total_files = total_files

        for i in range(total_files):
            spectro = self.get_spectro_from_index(i)

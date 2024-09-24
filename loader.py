import numpy as np
import os

class Loader():
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.total_files = 0
    def get_spectro_from_index(self, idx: int):
        """Get the spectrogram of a given index"""
        total_list = os.listdir(self.root_dir)
        real_list = []
        for file in total_list:
            if file.endswith(".npy"):
                real_list.append(file)
        return real_list[idx]
    def __len__(self):
        return self.total_files
    def get_train(self):
        print("Getting training data")
        total_files = 0
        print(self.root_dir)
        for file in os.listdir(self.root_dir):
            if os.path.isfile(file) and file.endswith(".npy"):
                total_files += 1
        self.total_files = total_files

        for i in range(total_files):
            if i % 5 != 0: 
                yield self.get_spectro_from_index(i)
    
    def get_val(self):
        print("Getting validation set")
        total_files = 0
        for file in os.listdir(self.root_dir):
            if os.path.isfile(file) and file.endswith(".npy"):
                total_files += 1
        self.total_files = total_files

        for i in range(total_files):
            if i % 5 == 0: 
                yield self.get_spectro_from_index(i)
            
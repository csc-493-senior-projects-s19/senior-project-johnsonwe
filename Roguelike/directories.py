# Creates directories for given information

import os


def create_dir(directory):
    """creates directory for test results"""
    if not os.path.isdir(directory):  # checks if directory had already been created
        os.makedirs(directory)


def write_file(path, data):
    """creates file for specific test results"""
    f = open(path, 'w')
    f.write(data)  # writes test results to file
    f.close()

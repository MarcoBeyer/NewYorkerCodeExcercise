"""Contains functions which will be used in multiple scripts ot functions which are not problem-specific"""

import json
import random


def generate_unique_random_numbers(start, stop, n):
    """
    Generates a set of unique random numbers in the range start to nstop
    function will fail if n is near or greater than stop - start + 1
    :param start: the minimum(inclusive) of the range of random numbers
    :param stop: the maximum(inclusive) of the range of random numbers
    :param n: n defines the number of unique numbers to return
    :return: a set of n unique numbers
    """
    unique_numbers = set()
    while len(unique_numbers) < n:
        unique_numbers.add(random.randint(start, stop))
    return unique_numbers


def count_rows(path):
    """
    Counts the rows of a given file and returns the number of rows
    :param path: path of the file
    :return: the number of rows of the given file
    """
    n_rows = 0
    with open(path, "rb") as file:
        for _ in file:
            n_rows += 1
    return n_rows


def copy_rows(from_file, to_file, row_numbers):
    """
    Copies selected rows from input file to the target file.
    The target file will be overwritten if already existent
    :param from_file: path to input file from which the rows are read
    :param to_file: path to target file
    :param row_numbers: set of row_numbers to be copied
    """
    with open(from_file, "rb") as user_file, open(to_file, "wb") as user_sample_file:
        i = 0
        for line in user_file:
            i += 1
            if i in row_numbers:
                user_sample_file.write(line)


def get_user_ids(user_file):
    """
    Extracts all user IDs of a yelp user file
    :param user_file: path of the user File
    """
    user_ids = set()
    with open(user_file, "rb") as file:
        for line in file:
            user = json.loads(line)
            user_ids.add(user["user_id"])
    return user_ids

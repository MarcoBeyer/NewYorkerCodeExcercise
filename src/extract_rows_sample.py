#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This script copies a random sample percentage of rows from one file to a new file. """
import argparse
from common_functions import count_rows, copy_rows, generate_unique_random_numbers


def extract_sample(input_file, output_file, sample_percentage):
    """
    Copies a random sample of rows from one file to a new file
    :param input_file: path to the file where the rows will be sampled
    :param output_file: path where the sampled rows will be stored
    :param sample_percentage: the percentage which should be sampled in decimal notation e.g. 20% = 0.2
    :return:
    """
    # Number of rows
    row_count = count_rows(input_file)
    sample_row_numbers = generate_unique_random_numbers(1, row_count, round(sample_percentage * row_count))
    copy_rows(input_file, output_file, sample_row_numbers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Writes all reviews from users which are in a given users file to "
                                                 "a given file")
    parser.add_argument("input_file", type=str,
                        help="path of the file which shall be sampled")
    parser.add_argument("output_file", type=str,
                        help="path of file where the sample should be stored")
    parser.add_argument("sample_percentage", type=float,
                        help="the percentage which should be randomly sampled in decimal notation e.g. 20% = 0.2")
    args = parser.parse_args()
    extract_sample(args.input_file, args.output_file, args.sample_percentage)

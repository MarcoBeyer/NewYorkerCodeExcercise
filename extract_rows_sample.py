#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This script copies a random sample percentage of rows from one file to a new file. """
from common_functions import count_rows, copy_rows, generate_unique_random_numbers


def extract_sample(input_file, output_file, sample_percentage):
    """

    :param input_file:
    :param output_file:
    :param sample_percentage: the percentage which should be sampled in decimal notation e.g. 20% = 0.2
    :return:
    """
    # Number of rows
    row_count = count_rows(input_file)
    sample_row_numbers = generate_unique_random_numbers(1, row_count, round(sample_percentage * row_count))
    copy_rows(input_file, output_file, sample_row_numbers)

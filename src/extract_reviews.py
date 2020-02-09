#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""extract yelp reviews from users in the given yelp user file"""
import json
import argparse
from common_functions import get_user_ids


def copy_reviews_from_users(review_file, output_file, user_file):
    """

    :param review_file:
    :param output_file:
    :param user_file:
    :return:
    """
    user_ids = get_user_ids(user_file)
    with open(review_file, 'rb') as review_file, open(output_file, 'wb') as review_sample_file:
        for line in review_file:
            review = json.loads(line)
            if review["user_id"] in user_ids:
                review_sample_file.write(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Writes all reviews from users which are in a given users file to '
                                                 'a given file')
    parser.add_argument('user_file', type=str,
                        help='path of the file where the user data is stored')
    parser.add_argument('review_file', type=str,
                        help='path of file which contains the reviews')
    parser.add_argument('output_file', type=str,
                        help='path of file where the sample of reviews will be stored')
    args = parser.parse_args()
    copy_reviews_from_users(args.review_file, args.output_file, args.user_file)
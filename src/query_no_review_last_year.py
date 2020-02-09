#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import json
import datetime as dt
import argparse
from common_functions import get_user_ids


def get_users_no_review_last_year(user_file, review_file, output_file, current_date):
    """
    Writes all users which have not written a review in the last year to a given file
    :param user_file:
    :param review_file:
    :param output_file:
    :param current_date: current date as string in the format YYYY-MM-DD e.g. 2018-11-20
    :return:
    """
    current_date = dt.datetime.strptime(current_date, "%Y-%m-%d")
    # subtract one year and handle leap years e.g. 2020-02-29
    try:
        last_year = current_date.replace(year=current_date.year - 1)
    except ValueError:
        last_year = current_date.replace(year=current_date.year - 1, day=current_date.day - 1)
    # get all user IDs and remove all users who have written a review in the last year
    user_ids = get_user_ids(user_file)
    with open(review_file, "rb") as review_file, open(output_file, "w") as query_output:
        for line in review_file:
            review = json.loads(line, encoding="utf-8")
            review_date = dt.datetime.fromisoformat(review["date"])
            if (review_date >= last_year) and (review_date < current_date):
                user_ids.discard(review["user_id"])
        json.dump(list(user_ids), query_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Writes all users which have not written a review in the last year '
                                                 'to a given file')
    parser.add_argument('user_file', type=str,
                        help='path of the file where the user data is stored')
    parser.add_argument('review_file', type=str,
                        help='path of file which contains the reviews')
    parser.add_argument('output_file', type=str,
                        help='path of file where the output will be stored')
    parser.add_argument('current_date', type=str,
                        help='the date in the format YYYY-MM-DD which should be handled as the current date')
    args = parser.parse_args()
    get_users_no_review_last_year(args.user_file, args.review_file, args.output_file, args.current_date)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import json
import datetime as dt
from common_functions import get_user_ids


def get_users_no_review_last_year(user_file, review_file, output_file, current_date):
    """
    Returns all users which have not written a review in the last year
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
    with open(review_file, "rb") as review_file, open(output_file, "wb") as query_output:
        for line in review_file:
            review = json.loads(line, encoding="utf-8")
            review_date = dt.datetime.fromisoformat(review["date"])
            if (review_date >= last_year) & (review_date < current_date):
                user_ids.discard(review["user_id"])
    json.dump(user_ids, output_file)


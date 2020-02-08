#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""extract yelp reviews from users in the given yelp users file"""
import json
from common_functions import get_user_ids


def copy_reviews_from_users(review_file, review_sample_file, users_file):
    """

    :param review_file:
    :param review_sample_file:
    :param users_file:
    :return:
    """
    user_ids = get_user_ids(users_file)
    with open(review_file, 'rb') as review_file, open(review_sample_file, 'wb') as review_sample_file:
        for line in review_file:
            review = json.loads(line, encoding="utf-8")
            if review["user_id"] in user_ids:
                review_sample_file.write(line)


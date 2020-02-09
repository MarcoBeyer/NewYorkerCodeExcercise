import subprocess
import argparse
import datetime as dt
import os

"""
"""

OUTPUT_FOLDER_NAME = "output"
USER_FILENAME = "user.json"
REVIEW_FILENAME = "review.json"
USER_SAMPLE_FILENAME = "user_sample.json"
REVIEW_SAMPLE_FILENAME = "review_sample.json"
QUERY_OUTPUT_FILENAME = "users_no_review_last_year.json"
SAMPLE_PERCENTAGE = 0.01

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Workflow script for sampling and querying yelp data')
    parser.add_argument('tar_file', type=str,
                        help='path of the yelp tar file to untar')
    parser.add_argument('current_date', type=str, default=dt.date.today().isoformat(),
                        help='the date in the format YYYY-MM-DD which should be handled as the current date (default: '
                             'current day from system clock)')
    args = parser.parse_args()

    # get folder of tar file and create target file paths
    output_dir = os.path.join(os.path.dirname(args.tar_file), OUTPUT_FOLDER_NAME)
    data_dir = ""
    review_file = os.path.join(output_dir, REVIEW_FILENAME)
    user_file = os.path.join(output_dir, REVIEW_FILENAME)
    os.mkdir(output_dir)
    print(output_dir)
    user_sample_file = os.path.join(output_dir, USER_SAMPLE_FILENAME)
    print(user_sample_file)
    review_sample_file = os.path.join(output_dir, REVIEW_SAMPLE_FILENAME)
    print(review_sample_file)
    output_file = os.path.join(output_dir, QUERY_OUTPUT_FILENAME)
    print(output_file)

    # Task 0: untar user and review file from yelp tar file
    print("Untar File")
    subprocess.run(["tar", "-C", output_dir, "-xf", args.tar_file, USER_FILENAME, REVIEW_FILENAME])

    # Task 1: Sample 0.1 percent of users and write them to disk
    print("Sample Users")
    subprocess.run(["python extract_rows_sample.py", user_file, user_sample_file, SAMPLE_PERCENTAGE])

    # Task 2: Extract all reviews from users in a given sample and write them to disk
    print("Extract Reviews")
    subprocess.run(["python extract_reviews.py", user_sample_file, review_file, review_sample_file])

    # Task 3: Get a list of user_ids that did not write any reviews in the last 1 year
    print("Query Users which have not written a review last year")
    subprocess.call(["python query_no_review_last_year.py", user_sample_file, review_sample_file,
                     output_file, args.current_date])
    print("Tasks completed!")

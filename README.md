# New Yorker - Data Engineering - Programming Exercise
## Goal
  - Get all users that did not write any reviews in the last year from the yelp data set
## Tasks
  - Randomly sample a small percentage (~= 1%) of users and write their data to disk in the same format as input
  - Select all reviews of this sample of users and write these reviews data to disk in the same format as input
  - Write to disk a list of user IDs that did not write any reviews in the last 1 year.
## Usage
The docker container runs all tasks and writes the outputs of the single tasks to a folder named output
 which will be created in the same folder where the yelp tar file is stored.
 
After running this program the created `users_no_review_last_year.json` will contain all users which have not written 
a review between the current day(exclusive) and the same day(inclusive) one year before.
 
The docker image can be build with:
```console
docker build -t newyorker/excercise . 
```
This will store the docker image with the tag newyorker/excercise.

The container which will do all tasks in order can be run with:
```console
$ docker run -it --rm -v path_of_yelp_dataset:/data newyorker/excercise /data/filename_yelp current_date
```
- `path_of_yelp_dataset` - the folder of the yelp dataset which will be hosted inside the container under the path /data
- `filename_yelp` - the name of the yelp tar file
- `current_date` (optional) - the current date can be passed if not the current date of the system clock will be taken

Example:

This example will run the query for the 2nd of February in 2017 on the file `yelp_dataset.tar`.
The `yelp_dataset.tar` is stored in the `/home/ubuntu` folder.
```console
$ docker run -it --rm -v /home/ubuntu/:/data newyorker/excercise /data/yelp_dataset.tar 2017-01-02
```

The names of input and output files and folders can be changed by passing this 
environment variables with the `-e "name=value"` parameter
- `EXERCISE_OUTPUT_FOLDER_NAME` - name of the folder which should be used/created to store the output
- `EXERCISE_USER_FILENAME` - name of the input yelp user file
- `EXERCISE_REVIEW_FILENAME` - name of the input yelp review file
- `EXERCISE_USER_SAMPLE_FILENAME` - name of the file to store the sample of users
- `EXERCISE_REVIEW_SAMPLE_FILENAME` - name of the file to store the reviews of the sampled users
- `EXERCISE_QUERY_OUTPUT_FILENAME` - name of the file to store the query result


## Files
- `workflow.py` calls the scripts of the different tasks and parametrises them correctly.   
The workflow script will call the scripts over the console so that they can be easily replaced with scripts in
 other programming languages.
 
- `common_functions.py` contains functions which will be used in multiple scripts ot functions 
which are not problem-specific

- `extract_rows_sample.py` a script which copies a random sample percentage of rows from one file to a new file.

- `extract_reviews.py` extract yelp reviews from users which are in the given yelp user file

- `query_no_review_last_year.py` a script which qu
# Concept
## Select User Data
- Download Yelp data
- Generate a set of (number of rows) * 0.1 unique random numbers
- Write the rows which index is in the set to a new file
## Select Reviews
- Get the user IDs as set
- Select all reviews where user id is in set and write them to disk
## Select user IDs that did not write any reviews in the last 1 year
- Store all user IDs in a set
- Go through every review and check if is has been written in the last year
- then remove the user_id from the set
- order by timestamp could improve performance

# Reputation algorithm

This directory includes the scripts needed to run the first version of the reputation algorithm (task 2.4), as well as the local database to be used.

## Files

sql/database_empty.sql: it contains the structure of the database that internally need the two algorithms (for the reputation of users and for the reputation of activities) to perform the queries and obtain the information on which to perform the reputation calculations. In this case, there is only the structure without data (ready to start inserting real information from scratch).

src/update_reputation.py: in charge of calculating the reputation of all system users.

src/update_reputation_activities.py: in charge of calculating the reputation of all activities within the system.

src/update_limits.py: in charge of adjusting the dynamic variables which allow to modify the limits of each factor that affects the reputation of users.

src/update_limits_activities.py: in charge of adjusting the dynamic variables which allow to modify the limits of each factor that affects the reputation of activities.


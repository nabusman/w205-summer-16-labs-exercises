How to run:

1. Install psycopg2 and tweepy
> pip install psycopg2 tweepy

2. Initialize PostgreSQL
> service postgresql initdb
> service postgresql start
> sudo -u postgres psql

3. Set password with "\password" to "siddiqi"

4. Enter the following commands in the psql shell:
$ create database tcount;
$ \c tcount;
$ create table tweetwordcount (word TEXT PRIMARY KEY NOT NULL, count INT NOT NULL);

5. Exit the shell with Ctrl + d

6. Open pg_hba.conf in Nano:
> nano /var/lib/pgsql/data/pg_hba.conf

7. Change all "ident" values to "password", close and save pg_hba.conf

8. Reload the settings to enable them:
> /etc/init.d/postgresql reload

9. Go to the Tweetcount folder

10. Run the code to populate the database:
> sparse run

11. Once you are satisfied with the data, go to the exercise_2 folder which contains finalresults.py and histogram.py

12. Execute finalresults.py with the following syntax:
> python finalresults.py the

13. Execute histogram.py with the following syntax:
> python histogram.py 3,8

# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users CASCADE"
song_table_drop = "DROP TABLE IF EXISTS songs CASCADE"
artist_table_drop = "DROP TABLE IF EXISTS artists CASCADE"
time_table_drop = "DROP TABLE IF EXISTS time CASCADE"

# CREATE TABLES

songplay_table_create = (""" 
CREATE TABLE songplays (
  id SERIAL PRIMARY KEY,
  start_time TIMESTAMP,
  user_id INT,
  level VARCHAR,
  song_id VARCHAR,
  artist_id VARCHAR,
  session_id INT,
  location VARCHAR,
  user_agent VARCHAR
  --FOREIGN KEY (start_time) REFERENCES time(start_time),
  --FOREIGN KEY (user_id) REFERENCES users(id),
  --FOREIGN KEY (song_id) REFERENCES songs(id),
  --FOREIGN KEY (artist_id) REFERENCES artists(id)
)
""")

user_table_create = ("""
CREATE TABLE users (
  id  INT, --PRIMARY KEY,
  first_name VARCHAR,
  last_name VARCHAR,
  gender VARCHAR,
  level VARCHAR
)
""")

song_table_create = ("""
CREATE TABLE songs (
  id VARCHAR, -- PRIMARY KEY,
  title VARCHAR,
  artist_id VARCHAR,
  year INT,
  duration FLOAT
  --FOREIGN KEY (artist_id) REFERENCES artists(id)
)
""")

artist_table_create = ("""
CREATE TABLE artists (
  id VARCHAR, -- PRIMARY KEY,
  name VARCHAR,
  location VARCHAR,
  latitude FLOAT,
  longitude FLOAT
)
""")

time_table_create = ("""
CREATE TABLE time (
  start_time VARCHAR, --PRIMARY KEY,
  hour INT,
  day INT,
  week INT,
  month INT,
  year INT,
  weekday INT
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users
(id, first_name, last_name, gender, level) 
VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
INSERT INTO songs
(id, title, artist_id, year, duration)
VALUES(%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists
(id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
INSERT INTO time
(start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT s.id AS songid,
       a.id AS artistid
FROM songs AS s
  LEFT JOIN artists AS a on s.artist_id = a.id
WHERE s.title = %s
  AND a.name = %s
  AND s.duration = %s 
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, time_table_create, song_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
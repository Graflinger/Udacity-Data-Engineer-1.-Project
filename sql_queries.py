# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, start_time date, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id int Primary Key, first_name varchar, last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id varchar Primary Key, title varchar, artist_id varchar, year int, duration decimal);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (artist_id varchar Primary Key, name varchar, location varchar, latitude decimal, longitude decimal);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time date Primary Key, hour int, day int, week int, month int, year int, weekday int);
""")

# INSERT RECORDS
songplay_table_insert =  ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
On Conflict(songplay_id) Do Nothing""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) 
VALUES (%s, %s, %s, %s, %s)
On Conflict(user_id) Do Nothing""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, duration) 
VALUES (%s, %s, %s, %s)
On Conflict(song_id) Do Nothing""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) 
VALUES (%s, %s, %s, %s, %s)
On Conflict(artist_id) Do Nothing""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
On Conflict(start_time) Do Nothing""")

# FIND SONGS

song_select = ("""
SELECT song_id, a.artist_id from songs as s 
    join artists as a ON s.artist_id = a.artist_id
    where s.title = %s and a.name = %s and s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
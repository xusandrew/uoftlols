import psycopg2

conn = psycopg2.connect(
    host="chatappdata.c1rgmh92t4a4.us-east-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432")

cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute('''CREATE TABLE users
            (
                id BIGSERIAL PRIMARY KEY,
                firstname VARCHAR(100) NOT NULL,
                lastname VARCHAR(100) NOT NULL
            );

            CREATE TABLE chatdata
            (
                id BIGSERIAL PRIMARY KEY,
                message VARCHAR(500) NOT NULL,
                sentuserid INT NOT NULL,
                receiveduserid INT NOT NULL,
                time TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE analytics
            (
                userid INT NOT NULL,
                emotion VARCHAR(30) NOT NULL,
                time TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
            );

            INSERT INTO users
            (firstname, lastname)
            VALUES
            ('Dave', 'Dover');

            INSERT INTO users
            (firstname, lastname)
            VALUES
            ('Alice', 'Bon');

            INSERT INTO chatdata
            (message, sentuserid, receiveduserid, time)
            VALUES
            ('Hello Alice.', 0, 1, '2023-1-21T13:49:51.141Z');

            INSERT INTO chatdata
            (message, sentuserid, receiveduserid, time)
            VALUES
            ('Hello Dave.', 1, 0, '2023-1-21T13:49:51.141Z');

            INSERT INTO analytics
            (userid, emotion, time)
            VALUES
            (0, 'Happy', '2023-1-21T13:49:51.141Z');

            INSERT INTO analytics
            (userid, emotion, time)
            VALUES
            (1, 'Sad', '2023-1-21T13:49:51.141Z');''')

cur.close()
conn.commit()

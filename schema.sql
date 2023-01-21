CREATE TABLE users
(
    id BIGSERIAL PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
);

CREATE TABLE chatdata
(
    id BIGSERIAL PRIMARY KEY,
    message VARCHAR(5000) NOT NULL,
    sentuserid INT NOT NULL,
    recieveduserid INT NOT NULL,
    time TIMESTAMP NOT NULL
);

CREATE TABLE analytics
(
    userid INT NOT NULL,
    emotion VARCHAR(30),
    time TIMESTAMP NOT NULL
);

INSERT INTO users
    (firstname,lastname)
VALUES
    ("Dave", "Dover");

INSERT INTO users
    (firstname,lastname)
VALUES
    ("Alice", "Bon");

INSERT INTO chatdata
    (message, sentuserid, recieveduserid, time)
VALUES
    ("Hello Alice.", 0, 1, "2023-1-21T13:49:51.141Z");

INSERT INTO chatdata
    (message, sentuserid, recieveduserid, time)
VALUES
    ("Hello Dave.", 1, 0, "2023-1-21T13:49:51.141Z");

INSERT INTO analytics
    (userid, emotion, time)
VALUES
    (0, "Happy", "2023-1-21T13:49:51.141Z")

INSERT INTO analytics
    (userid, emotion, time)
VALUES
    (1, "Sad", "2023-1-21T13:49:51.141Z")
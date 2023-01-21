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
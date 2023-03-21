CREATE TABLE PLAYER_ATTRIBUTES (
    attributes_id INT PRIMARY KEY,
    player_name VARCHAR(255),
    physicality INT,
    passion INT,
    skill_level INT,
    determination INT,
    sportsmanship INT,
    humility INT,
    sense_of_humor INT,
    love_of_social_aspect INT
);

ALTER TABLE PLAYER ADD COLUMN attributes_id INT;

ALTER TABLE PLAYER
ADD CONSTRAINT fk_PlayerAttributes
FOREIGN KEY (attributes_id)
REFERENCES PLAYER_ATTRIBUTES(attributes_id);
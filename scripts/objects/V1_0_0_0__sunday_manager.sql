CREATE TABLE LEAGUE(
league_id INT IDENTITY(1,1) PRIMARY KEY,
league_name VARCHAR(25) NOT NULL
);

CREATE TABLE TEAM(
 team_id INT IDENTITY(1,1) PRIMARY KEY,
 team_name VARCHAR(25) NOT NULL,
 league_name VARCHAR(25) NOT NULL 
);

ALTER TABLE TEAM
ADD CONSTRAINT fk_TeamInLeague
FOREIGN KEY (league_id)
REFERENCES LEAGUE(league_id);

CREATE TABLE PLAYER(
 player_id INT IDENTITY(1,1) PRIMARY KEY,
 player_name VARCHAR(25) NOT NULL,
 team_id VARCHAR(25)
);

ALTER TABLE PLAYER
ADD CONSTRAINT fk_PlayerInTeam
FOREIGN KEY (team_id)
REFERENCES TEAM(team_id);
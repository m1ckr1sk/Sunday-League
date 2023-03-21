from mysql_connection import MySqlConnection
from csvloader import CsvLoader
import random


class ConfigLoader:

    def __init__(self, db_connection:MySqlConnection):
        
        # list of fictional village names
        self.db_connection = db_connection

    def load_config(self):
        self.db_connection.connect()

        # Create league
        create_query = "INSERT INTO league (league_name, league_id) VALUES (%s, %s)"
        create_values = ("Barretts Butchers Sunday Premier", 1)
        self.db_connection.create(create_query, create_values)

        # Create teams
        village_names = ['Lavender', 'Willowdale', 'Greenhaven', 'Riverstone', 'Birchwood', 'Meadowbrook', 'Sunnyvale', 'Foxborough', 'Maplewood', 'Briarwood']
        create_query = "INSERT INTO team (team_name, league_id, team_id) VALUES (%s, %s, %s)"
        team_id = 0
        for vilage_name in village_names:
            create_values = (vilage_name, 1, team_id)
            self.db_connection.create(create_query, create_values)
            team_id += 1

        # create players
        csv_loader = CsvLoader()
        firstnames = csv_loader.load_csv("sundayleague\\database\\firstnames.csv")
        surnames = csv_loader.load_csv("sundayleague\\database\\surnames.csv")
        nicknames = csv_loader.load_csv("sundayleague\\database\\nicknames.csv")
        create_query = "INSERT INTO player (player_name, team_id, nickname, player_id) VALUES (%s, %s, %s, %s)"

        team_id = 0
        player_id = 0
        for village in village_names:
            squad_size = random.randint(12,20)
            for player_index in range(squad_size):
                player_name = random.choice(firstnames)[0] + " " + random.choice(surnames)[0]
                nickname = random.choice(nicknames) [0]
                create_values = (player_name, team_id, nickname, player_id)
                self.db_connection.create(create_query, create_values)
                player_id += 1
            team_id += 1


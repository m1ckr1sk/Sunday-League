import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.mysql_connection import MySqlConnection
from config.config_loader import ConfigLoader
from model.team import Team
from model.league import League

# Instantiate connection object
db = MySqlConnection('localhost', 'SUNDAY_MANAGER_ADMIN', 'SUNDAY_MANAGER_ADMIN', 'sunday_manager')
Config_loader = ConfigLoader(db)
Config_loader.load_config(data_path="C:\\Users\\mjbut\\repos\\Sunday-League\\sundayleague\\config")

league = League(db=db, league_id=1)
league_teams = league.get_teams()

team1 = Team(db=db, team_id=league_teams[0][0])
players = team1.get_players()


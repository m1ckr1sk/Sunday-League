from mysql_connection import MySqlConnection
from config_loader import ConfigLoader

# Instantiate connection object
db = MySqlConnection('localhost', 'SUNDAY_MANAGER_ADMIN', 'SUNDAY_MANAGER_ADMIN', 'sunday_manager')
Config_loader = ConfigLoader(db)
Config_loader.load_config()

# Get a team and its players
team_id = 0
select_team_squad = f"SELECT player_name, nickname, team_name FROM sunday_manager.player inner join sunday_manager.team on team.team_id=player.team_id where team.team_id = {team_id}"
squad_members = db.read(select_team_squad)
print(squad_members)
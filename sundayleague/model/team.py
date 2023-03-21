class Team:
    def __init__(self, db, team_id) -> None:
        self.db = db
        self.team_id = team_id

    def get_players(self):
        select_team_squad = f"SELECT player_name, nickname, team_name FROM sunday_manager.player inner join sunday_manager.team on team.team_id=player.team_id where team.team_id = {self.team_id}"
        squad_members = self.db.read(select_team_squad)
        print(squad_members)
        return squad_members

    def get_team(self):
        select_team = f"SELECT team_name where team.team_id = {self.team_id}"
        team = self.db.read(select_team)
        print(team)
        return team

class League:
    def __init__(self, db, league_id) -> None:
        self.db = db
        self.league_id = league_id

    def get_teams(self):
        select_teams = f"SELECT team_id, team_name FROM sunday_manager.team where league_id = {self.league_id}"
        teams = self.db.read(select_teams)
        print(teams)
        return teams

    def get_league(self):
        # Get a team and its players
        select_team = f"SELECT league_name where league_id = {self.league_id}"
        league = self.db.read(select_team)
        print(league)

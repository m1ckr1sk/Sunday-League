import random

class MatchEngine:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0

    def simulate_match(self):
        for minute in range(1, 91):
            self.simulate_minute(minute)

    def simulate_minute(self, minute):
        home_chance = self.calculate_chance(self.home_team.attack, self.away_team.defense)
        away_chance = self.calculate_chance(self.away_team.attack, self.home_team.defense)
        if random.random() < home_chance:
            self.home_score += 1
            print(f"{minute}': GOAL! {self.home_team.name} {self.home_score} - {self.away_team.name} {self.away_score}")
        elif random.random() < away_chance:
            self.away_score += 1
            print(f"{minute}': GOAL! {self.away_team.name} {self.away_score} - {self.home_team.name} {self.home_score}")
        else:
            print(f"{minute}': No goal")

    def calculate_chance(self, attack, defense):
        return min(0.5 + attack - defense, 0.95)

class Team:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

if __name__ == '__main__':
    # Example usage
    liverpool = Team("Liverpool", 1.5, 1)
    manchester_united = Team("Manchester United", 1, 1.5)
    match = FootballMatch(liverpool, manchester_united)
    match.simulate_match()
    print(f"Final score: {match.home_team.name} {match.home_score} - {match.away_team.name} {match.away_score}")

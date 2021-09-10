"""This is my first github project"""

print("Hello World")

teams = ['united', 'city', 'forrest']
new_teams = []

def sort_teams(teams, new_teams):
    while teams:
        for team in teams:
            moving_team=teams.pop()
            new_teams.append(moving_team)


sort_teams(teams, new_teams)

print(f"First list of teams, {teams}")
print(f"Second list of teams, {new_teams}")
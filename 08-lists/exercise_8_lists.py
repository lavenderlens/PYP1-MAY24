table = ["Bath", "Derby", "Gloucester", 
        "Lancaster", "Newcastle", "Plymouth", 
        "Salford", "Wakefield"]

table.remove('Newcastle')
table.insert(2,'Newcastle')

table.remove('Derby')
table.insert(3,'Derby')

table.remove('Salford')

table.append('Canterbury')

table[table.index("Plymouth")] = "York"

europe = table[:2]

print(europe)

if "Newcastle" in europe:
    print("Newcastle to play in Europe")

for team in table:
    print(team)

# EXTRA CHALLENGE:
# return a list of the teams with names of 5 characters or less, upper-cased.
# using a single list comprehension
# this combines a map and a filter in one line and returns a new list
short_uppercase_teams = [team.upper() for team in table if len(team) <= 5]
print(short_uppercase_teams) # ['BATH', 'DERBY', 'YORK'] original unchanged

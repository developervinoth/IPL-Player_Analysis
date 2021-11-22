import pandas as pd
team_details = pd.read_csv('Flat_files/Match.csv').info()
print(team_details)
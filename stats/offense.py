import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

#find teh rows in the event column that contain S, D, etc.
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]
#print(hits.head())

#converting in the inning elements from strings to numbers
hits.loc[:, 'inning'] = pd.to_numeric(hits.loc[:, 'inning'])

replacements = {r'^S(.*)': 'single',
                r'^D(.*)': 'double',
                r'^T(.*)': 'triple',
                r'^HR(.*)': 'hr'}

#renaming the values for the event column
hit_type = hits['event'].replace(replacements, regex = True)

hits = hits.assign(hit_type=hit_type)
#print(hit_type.head())

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
#print(hits.head())

#finding the count of hits in a givin inning and giving a title to the new count of hits in an inning
hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name = 'count')

#giving a title to the new count of hits in an inning
#hits = hits.reset_index(name = 'count')

hits.loc['hit_type'] = pd.Categorical(hits['hit_type'], ['single', 'double', 'triple', 'hr'])
#print(hits.head())

# organizes from lowest inning to highest inning and hit type from single to HR
hits = hits.sort_values(['inning', 'hit_type'])


hits = hits.pivot(index = 'inning', columns = 'hit_type', values = 'count')
#print(hits.head())

hits.plot.bar(stacked =True)
plt.show()

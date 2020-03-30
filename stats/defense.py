import pandas as pd
import matplotlib.pyplot as plt
from frames import games, info, events

plays = games.query("type == 'play' & event != 'NP'")

plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']
#print(plays.head())

#ensurng that consecutive player appearneces aren't duplicated but kept to one index per player
pa = plays.loc[plays['player'].shift() != plays['player'], ['year', 'game_id', 'inning', 'team', 'player']]
#print(pa.head())

pa = pa.groupby(['year', 'game_id', 'team']).size().reset_index(name = 'PA')

#print(events.head())

#makes the columns origianlly asigned to the data frame the indexes for the data frame
events = events.set_index(['year', 'game_id', 'team', 'event_type'])
#print(events.head())

#making a data frame that takes the values of a multi-index and makes the element in a column, into a column and making each row indexed like before
events = events.unstack().fillna(0).reset_index()

events.columns = events.columns.droplevel()
#print(events.head())

events.columns = ['year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', 'SO']

#ensures the index name is not evemnt_types and on the sme axis as the other column headers
events = events.rename_axis('None', axis = 'columns')
print(events.head())

#performing an outer merge wuth pa and events
events_plus_pa = pd.merge(events, pa, how = 'outer', left_on = ['year', 'game_id', 'team'], right_on = ['year', 'game_id', 'team'])

import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games[games['type'] == 'play']
#print(plays.head())
#print(plays['event'].str.contains('K'))
strike_outs = plays[plays['event'].str.contains('K')]
#print(strikeouts.head())
strike_outs = strike_outs.groupby(['year', 'game_id']).size()
print(strike_outs.head())

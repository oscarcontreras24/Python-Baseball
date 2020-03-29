import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games[games['type'] == 'play']
#print(plays.head())
#print(plays['event'].str.contains('K'))
strike_outs = plays[plays['event'].str.contains('K')]
#print(strikeouts.head())
# print(strike_outs.loc[strike_outs['year'] == '1933', 'year']) == 8

#counts how many data points exist for a gven gameid in a given year
strike_outs = strike_outs.groupby(['year', 'game_id']).size()
#print(strike_outs.head(50))

strike_outs = strike_outs.reset_index(name = 'strike_outs')
#print(strike_outs.head())

# converting year and strike_out elements from strings to numbers
strike_outs = strike_outs.loc[:, ['year', 'strike_outs']].apply(pd.to_numeric)

strike_outs.plot(x = 'year', y = 'strike_outs', kind = 'scatter').legend('Strike Outs')
plt.show()

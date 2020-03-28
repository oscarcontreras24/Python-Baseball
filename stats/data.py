import os
import glob
import pandas as pd

#a = os.path.join('/Users/I522537/Documents/pluralsight-projects-Python-Baseball-83868ef/', 'games', '*.EVE')

#game_files = glob.glob(os.path.join('/Users/I522537/Documents/pluralsight-projects-Python-Baseball-83868ef/', 'games', '*.EVE'))
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
game_files.sort()
#print(game_files)

game_frames = []
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

games = pd.concat(game_frames)

games.loc[games['multi5'] == '??', ['multi5']] = ''

identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
#print(identifiers.head())

identifiers = identifiers.fillna(method='ffill')
identifiers.columns = ['game_id', 'year']
#print(identifiers.head())

games = pd.concat([games, identifiers], sort=False, axis=1)
#print(games.head())
games = games.fillna(' ')
#print(pd.unique(games['type'].values.ravel()))
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

import os
import glob
import pandas as pd

#a = os.path.join('/Users/I522537/Documents/pluralsight-projects-Python-Baseball-83868ef/', 'games', '*.EVE')

#game_files = glob.glob(os.path.join('/Users/I522537/Documents/pluralsight-projects-Python-Baseball-83868ef/', 'games', '*.EVE'))
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))


#print(game_files)
game_files.sort()
#print(game_files)

game_frames = []

for game_file in game_files:
    game_frame = pd.read_csv(game_file, names = ['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)
#print(game_frames)
#print(game_frames)
games = pd.concat(game_frames)
#games = games[~games.index.duplicated()]
#print(games.head(100))
#print(games.shape)
games.loc[games['multi5'] == '??', ['multi5']] = ''
#print(games.shape)
#print(games.loc[games['multi5'] == '??', ['multi5']])

#for row in range(games.shape[0]):
#    if games.lookup(row, 'multi5') == '??':
#        print(games[row])
#games.loc[games['multi5'] == '??', 'multi5'] = ''
#print(games.head(50))

identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
#print(identifiers.head())

identifiers = identifiers.fillna(method = 'ffill')
identifiers.columns = ['game_id', 'year']
#print(identifiers.head())

games = pd.concat([games, identifiers], axis = 1, sort = False)
#print(games.head())
games = games.fillna(' ')
#print(games.head())

#print(pd.unique(games['type'].values.ravel()))
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

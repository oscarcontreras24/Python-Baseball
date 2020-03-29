import pandas as pd
import matplotlib.pyplot as plt
from data import games

#print(games.head())
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'), ['year', 'multi3']]
#print(attendance.head())

attendance.rename(columns = {'year': 'year', 'multi3': 'attendance'}, inplace = True)
#print(attendance.head())

attendance.loc[:, "attendance"] = pd.to_numeric(attendance.loc[:, "attendance"])
#print(type(attendance['attendance']))

attendance.plot(x = 'year', y = 'attendance', figsize = (15,7), kind = 'bar')
plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y = attendance['attendance'].mean(), label = 'Mean', linestyle = '--', color = 'green')
plt.show()

#libraries
import pandas as pd
import numpy as np

#read csv
weapon = pd.read_csv('weapon.csv')
size = pd.read_csv('size.csv')
quality = pd.read_csv('quality.csv')

#randon
d10 = np.random.randint(10)
d5  = np.random.randint(5)
d3  = np.random.randint(3)

#atributes
weapon_name = str(quality.iloc[d5,0] + ' ' + size.iloc[d3,0] + ' ' + weapon.iloc[d10,0]).replace('Normal ', '').replace('Medium ', '')
price = str(size.iloc[d3,1] * quality.iloc[d5,2] * 10)
damage = size.iloc[d3,2]
hand = weapon.iloc[d10,d3+3]
bonus = quality.iloc[3,1]
range = weapon.iloc[d10,1]
damage_type = weapon.iloc[d10,2]

if bonus > 0: bonus_str = ('+' + str(bonus))
elif bonus < 0: bonus_str = str(bonus)
else: bonus_str = ''
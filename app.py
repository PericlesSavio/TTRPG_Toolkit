from flask import Flask, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET',])
def index():    
    #read csv
    weapon = pd.read_csv('static/weapon.csv')
    size = pd.read_csv('static/size.csv')
    quality = pd.read_csv('static/quality.csv')
    #randon
    d10 = np.random.randint(10)
    d5  = np.random.randint(5)
    d3  = np.random.randint(3)
    #atributes
    weapon_name = str(quality.iloc[d5,0] + ' ' + size.iloc[d3,0] + ' ' + weapon.iloc[d10,0]).replace('Normal ', '').replace('Medium ', '')
    price = str(size.iloc[d3,1] * quality.iloc[d5,2] * 10)
    damage = size.iloc[d3,2]
    hand = weapon.iloc[d10,d3+3]
    bonus = quality.iloc[d5,1]
    range = weapon.iloc[d10,1]
    damage_type = weapon.iloc[d10,2]
    if bonus > 0: bonus_str = ('+' + str(bonus)) 
    elif bonus < 0: bonus_str = str(bonus)
    else: bonus_str = ''
    dmg = damage + bonus_str + ' (' + damage_type + ')'
    return render_template('weapons.html',
        weapon = weapon_name,
        range = range,
        damage = dmg,
        hand = hand,
        price = price)

@app.route('/weapon', methods=['GET',])
def rpg():    
    #read csv
    weapon = pd.read_csv('static/weapon.csv')
    size = pd.read_csv('static/size.csv')
    quality = pd.read_csv('static/quality.csv')
    #randon
    d10 = np.random.randint(10)
    d5  = np.random.randint(5)
    d3  = np.random.randint(3)
    #atributes
    weapon_name = str(quality.iloc[d5,0] + ' ' + size.iloc[d3,0] + ' ' + weapon.iloc[d10,0]).replace('Normal ', '').replace('Medium ', '')
    price = str(size.iloc[d3,1] * quality.iloc[d5,2] * 10)
    damage = size.iloc[d3,2]
    hand = weapon.iloc[d10,d3+3]
    bonus = quality.iloc[d5,1]
    range = weapon.iloc[d10,1]
    damage_type = weapon.iloc[d10,2]
    if bonus > 0: bonus_str = ('+' + str(bonus)) 
    elif bonus < 0: bonus_str = str(bonus)
    else: bonus_str = ''
    dmg = damage + bonus_str + ' (' + damage_type + ')'
    return render_template('weapons.html',
        weapon = weapon_name,
        range = range,
        damage = dmg,
        hand = hand,
        price = price)

app.run()
from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import joblib
import xgboost
df_statistiques=pd.read_csv("C:\\Users\\moham\\Downloads\\df_total.csv")
df_players=pd.read_csv("C:\\Users\\moham\\OneDrive\\Bureau\\ML project\\data\\players_id.csv")
next_round=14
features_attack=['round','position_encoded','team_difficulty_value','avg_goals_scored', 'avg_assists','avg_clean_sheets','team_oppent_difficulty_value', 'assists_rolling', 'bps_rolling','avg_bps' ,'clean_sheets_rolling',
            'creativity_rolling','avg_creativity',  'goals_scored_rolling', 'ict_index_rolling','avg_ict_index' ,'selected_rolling','avg_selected', 'transfers_balance_rolling','avg_transfers_balance',
            'influence_rolling','avg_influence' ,'minutes_rolling', 'avg_minutes','threat_rolling','avg_threat', 'total_points_rolling','avg_total_points',
             'was_home_encoded','value_rolling',  'result_encoded_rolling']
features_defence=['round','team_difficulty_value',
       'team_oppent_difficulty_value', 'was_home_encoded','avg_goals_scored', 'avg_assists',
       'avg_goals_conceded', 'avg_clean_sheets',
       'avg_yellow_cards', 'avg_red_cards', 'avg_own_goals','avg_selected',
       'avg_transfers_balance', 'avg_value', 'avg_result', 'avg_bps', 'avg_influence',
       'avg_minutes', 'avg_total_points', 'assists_rolling', 'bps_rolling',
       'clean_sheets_rolling',  'goals_conceded_rolling',
       'goals_scored_rolling',  'influence_rolling',
       'minutes_rolling',  'total_points_rolling', 'red_cards_rolling',  'own_goals_rolling',
       'selected_rolling', 'transfers_balance_rolling', 'value_rolling',
       'yellow_cards_rolling', 'result_encoded_rolling']
features_goal_kepper=['round','team_element','opponent_team','team_difficulty_value',
       'team_oppent_difficulty_value','was_home_encoded','avg_assists',
       'avg_goals_conceded', 'avg_clean_sheets', 'avg_saves',
       'avg_yellow_cards',
       'avg_penalties_saved',
       'avg_transfers_balance', 'avg_value', 'avg_result', 'avg_bps',

       'avg_total_points', 'assists_rolling', 'bps_rolling',
       'clean_sheets_rolling',  'goals_conceded_rolling',
        'total_points_rolling',
        'penalties_saved_rolling',
    'saves_rolling',
        'transfers_balance_rolling', 'value_rolling',
       'yellow_cards_rolling', 'result_encoded_rolling']
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def name_player():
    if request.method == 'POST':
        player_name = request.form['player_name'].title()  
        old_predections = df_statistiques.loc[(df_statistiques['name'] == player_name)][['round', 'element', 'total_points', 'predections']].values
        player_id = int(old_predections[0][1])
        position = df_players.loc[df_players['id'] == player_id, 'position'].values[0]
        
        
        prediction_data = []  # Pour stocker les données de chaque round
        for round in old_predections:
            round_number = int(round[0])
          
            total_points = float(round[2])
            points_pretected = float(round[2])
            prediction_data.append((round_number, total_points, points_pretected))
        
        photo_url = 'https://resources.premierleague.com/premierleague/photos/players/250x250/p118748.png'
        
        
        return render_template(
            'player.html',
            player_name=player_name,
            position=position,
            player_id=player_id,
            photo_url=photo_url,
            
            prediction_data=prediction_data  # Passer la liste de tuples
        )
    else:
        return render_template('statisques.html')
 
@app.route('/predection',methods=['GET','POST'])
def predection():
    if request.method == 'POST':
        player_name = request.form.get('player_name', 'Unknown')
        player_position=request.form.get('position_player','Unknown')
        player_id=request.form.get('player_id','Unknown')
        player_id=int(player_id)
        if player_position=='MID' or player_position=='FWD':
            model=joblib.load('C:/Users/moham/OneDrive/Bureau/ML project/model/model_attack.pkl')
            data=df_statistiques.loc[df_statistiques['element']==player_id][features_attack].tail(1)
            predection=model.predict(data)[0]
            
        return render_template('player.html',
         player_name=player_name,
         player_position=player_position,
         predection=predection)
        

        if player_position=='DEF':
            model=joblib.load('C:/Users/moham/OneDrive/Bureau/ML project/model/model_def.pkl')
        else:
            model=joblib.load('C:/Users/moham/OneDrive/Bureau/ML project/model/model_gk.pkl')

    
    return render_template('player.html')
    

if __name__ == '__main__':
    app.run(debug=True)

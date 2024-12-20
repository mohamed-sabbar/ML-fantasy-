import pandas as pd
import requests
df_players = pd.read_csv("C:\\Users\\moham\\OneDrive\\Bureau\\ML project\\data\\players_id.csv")
round_filter = 16 
all_statistics = []
def get_player_summary(player_id, round_filter):
    url = f"https://fantasy.premierleague.com/api/element-summary/{player_id}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            history = data.get('history', [])
            filtered_stats = [stat for stat in history if stat.get('round') == round_filter]
            if not filtered_stats:
                print(f"Aucune donnée pour le joueur {player_id} au round {round_filter}")
                return
            
            for stat in filtered_stats:
                all_statistics.append({
                    'element': stat['element'],
                    'opponent_team': stat['opponent_team'],
                    'total_points': stat['total_points'],
                    'was_home': stat['was_home'],
                    'kickoff_time': stat['kickoff_time'],
                    'team_h_score': stat['team_h_score'],
                    'team_a_score': stat['team_a_score'],
                    'round': stat['round'],
                    'minutes': stat['minutes'],
                    'goals_scored': stat['goals_scored'],
                    'assists': stat['assists'],
                    'clean_sheets': stat['clean_sheets'],
                    'goals_conceded': stat['goals_conceded'],
                    'own_goals': stat['own_goals'],
                    'penalties_saved': stat['penalties_saved'],
                    'penalties_missed': stat['penalties_missed'],
                    'yellow_cards': stat['yellow_cards'],
                    'red_cards': stat['red_cards'],
                    'saves': stat['saves'],
                    'bonus': stat['bonus'],
                    'bps': stat['bps'],
                    'influence': stat['influence'],
                    'creativity': stat['creativity'],
                    'threat': stat['threat'],
                    'ict_index': stat['ict_index'],
                    'starts': stat['starts'],
                    'expected_goals': stat['expected_goals'],
                    'expected_assists': stat['expected_assists'],
                    'expected_goal_involvements': stat['expected_goal_involvements'],
                    'expected_goals_conceded': stat['expected_goals_conceded'],
                    'value': stat['value'],
                    'transfers_balance': stat['transfers_balance'],
                    'selected': stat['selected'],
                    'transfers_in': stat['transfers_in'],
                    'transfers_out': stat['transfers_out']
                })
        else:
            print(f"Erreur lors de la récupération des données pour le joueur {player_id} (status: {response.status_code})")
    except Exception as e:
        print(f"Erreur pour le joueur {player_id} : {e}")

# Récupérer les IDs uniques des joueurs
ids_players = df_players['id'].unique().tolist()

# Boucle sur chaque joueur pour récupérer ses statistiques
for player_id in ids_players:
    get_player_summary(player_id, round_filter)

# Créer un DataFrame avec les statistiques collectées
df = pd.DataFrame(all_statistics)

# Afficher les premières lignes du DataFrame
print(df.head())
df.to_csv('new_round_data.csv')
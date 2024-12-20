import pandas as pd

def fill_name_team_element(row):
    matching_row = df_players_id[df_players_id['id'] == row['element']]
    if not matching_row.empty:
        row['name'] = matching_row.iloc[0]['full_name']
        row['position'] = matching_row.iloc[0]['position']
        row['team_element']=matching_row.iloc[0]['team_element']
    return row
def fill_result():
  df.loc[(df['was_home'] & (df['team_h_score']> df['team_a_score'])),'result' ]='W'
  df.loc[(df['was_home'] & (df['team_h_score']< df['team_a_score'])),'result' ]='L'
  df.loc[~(df['was_home'] & (df['team_h_score']< df['team_a_score'])),'result' ]='W'
  df.loc[~(df['was_home'] & (df['team_h_score']> df['team_a_score'])),'result' ]='L'
  df.loc[(df['team_h_score']== df['team_a_score']),'result' ]='D'
def fill_oppent_team(row):
    new_season=df_teams.loc[df_teams['season']=='2024-25']
    team=new_season[new_season['team']==row['team_element']]
    if not team.empty:
        row['team_x'] = team.iloc[0]['team_name']
    team_oppent=new_season[new_season['team']==row['opponent_team']]
    if not team_oppent.empty:
        row['opp_team_name'] = team_oppent.iloc[0]['team_name']

    return row


  


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


df = pd.read_csv('C:\\Users\\moham\\OneDrive\\Bureau\\ML project\\new_round_data.csv')
df_full_data = pd.read_csv("C:\\Users\\moham\\Downloads\\df_total (1).csv")
df_players_id = pd.read_csv("C:\\Users\\moham\\OneDrive\\Bureau\\ML project\\data\\players_id.csv")
df_teams=pd.read_csv("C:\\Users\\moham\\OneDrive\\Bureau\\ML project\\data\\final teams data.csv")

df = df[df_full_data.columns.intersection(df.columns)]
for col in df_full_data.columns.difference(df.columns):
    df[col] = None


df = df.apply(fill_name_team_element, axis=1)
fill_result()

result_mapping = {"L": -1, "W": 1, "D": 0}
df['result_encoded'] = df['result'].map(result_mapping)
was_home_mapping = {True: 1, False: 0}
df['was_home_encoded'] = df['was_home'].map(was_home_mapping)
position_mapping = {"GK": 1, "DEF": 2, "MID": 3, "FWD": 4}
df['position_encoded'] = df['position'].map(position_mapping)
df['season']='2024/2025'
df = df.apply(fill_oppent_team, axis=1)
print(df.head(1))
wrong = ["Andrew Robertson", "Alexandre Moreno Lopera", "Andriy Yarmolenko", "Antony Matheus dos Santos", "Benjamin Chilwell",
        "Carlos Henrique Casimiro", "Carlos Ribeiro Dias", "Conrad Egan-Riley", "Crysencio Summerville", "Daniel Bentley",
        "Daniel Chesters", "Danilo dos Santos de Oliveira", "Emerson Leite de Souza Junior", "Fabio Henrique Tavares",
        "Fabricio Agosto Ramírez", "Facundo Buonanotte", "Faustino Anjorin", "Fernando Luiz Rosa", "Fernando Marçal",
        "Francisco Jorge Tomás Oliveira", "Frederico Rodrigues de Paula Santos", "Fábio Ferreira Vieira",
        "Gabriel dos Santos Magalhães", "James Bree", "Jonathan Castro Otto", "Jordan Henderson", "Jordan Hugill",
        "Jorge Luiz Frello Filho", "Joseph Gomez", "Joseph Willock", "Josh Sims", "Joshua Sargent", "José Ignacio Peleteiro Romallo",
        "Joshua Wilson-Esbrand", "Joseph Johnson", "Callum Scanlon", "Benjamin Chrisene", "Juan Camilo Hernández Suárez",
        "Kell Watts", "Konstantinos Tsimikas", "Kyle Bartley", "Léo Bonatini", "Mahmoud Ahmed Ibrahim Hassan",
        "Marcus Oliveira Alencar", "Mathias Jorgensen", "Matthew Cash", "Matthew Clarke", "Matthew Longstaff", "Matthew Pollock",
        "Max Kilman", "Mohamed Dräger", "Norberto Bercique Gomes Betuncal", "Pelenda Joshua Dasilva", "Raphael Dias Belloli",
        "Robbie Brady", "Rodrigo Hernandez", "Rui Pedro dos Santos Patrício", "Shaqai Forde", "Solomon March", "Victor da Silva",
        "Vitor Ferreira", "Xande Nascimento da Costa Silva", "Yegor Yarmoliuk"]
fixable = ["Andy Robertson", "Álex Moreno", "Andrii Yarmolenko", "Antony", "Ben Chilwell", "Casemiro", "Cafú", "CJ Egan-Riley",
          "Crysencio Summerville", "Dan Bentley", "Dan Chesters", "Danilo", "Emerson Royal", "Fabinho", "Fabri", "Facundo Buonanotte",
          "Tino Anjorin", "Fernandinho", "Marçal", "Chiquinho", "Fred", "Fábio Vieira", "Gabriel Magalhães", "James Bree", "Jonny Otto",
          "Jordan Henderson", "Jordan Hugill", "Jorginho", "Joe Gomez", "Joe Willock", "Josh Sims", "Josh Sargent", "Jota",
          "Josh Wilson-Esbrand", "Joe Johnson", "Calum Scanlon", "Ben Chrisene", "Cucho Hernández", "Kelland Watts", "Kostas Tsimikas",
          "Kyle Bartley", "Léo Bonatini", "Trézéguet", "Marquinhos", "Zanka", "Matty Cash", "Matt Clarke", "Matty Longstaff",
          "Mattie Pollock", "Maximilian Kilman", "Mohamed Dräger", "Beto", "Josh Dasilva", "Raphinha", "Robert Brady", "Rodri",
          "Rui Patrício", "Shaq Forde", "Solly March", "Vitinho", "Vitinha", "Xande Silva", "Yehor Yarmoliuk"]
import pandas as pd



data = {
    'team': [
        "Man City", "Arsenal", "Liverpool", "Aston Villa", "Spurs", "Chelsea",
        "Newcastle", "Man Utd", "West Ham", "Crystal Palace", "Brighton",
        "Bournemouth", "Fulham", "Wolves", "Everton", "Brentford",
        "Nott'm Forest", "Luton", "Burnley", "Sheffield Utd"
    ],
    'points': [91, 89, 82, 68, 66, 63, 60, 60, 52, 49, 48, 48, 47, 46, 40, 39, 32, 26, 24, 16],
    'goals_scored': [96, 91, 86, 76, 74, 77, 85, 57, 60, 57, 55, 54, 55, 50, 40, 56, 49, 52, 41, 35],
    'goals_conceded': [34, 29, 41, 61, 61, 63, 62, 58, 74, 58, 62, 67, 61, 65, 51, 65, 67, 85, 78, 104],
    'games_played': [38] * 20
}


df_2023_2024 = pd.DataFrame(data)


df_2023_2024['goals_scored_per_game'] = df_2023_2024['goals_scored'] / df_2023_2024['games_played']
df_2023_2024['goals_conceded_per_game'] = df_2023_2024['goals_conceded'] / df_2023_2024['games_played']

# Fonction pour évaluer la difficulté d'une équipe
def evaluate_difficulty(row):
    offensive_strength = row['goals_scored_per_game']
    defensive_strength = 1 / (row['goals_conceded_per_game'] + 0.1)  # Ajout de 0.1 pour éviter la division par zéro
    ranking_factor = (21 - df_2023_2024.index[df_2023_2024['team'] == row['team']].tolist()[0]) / 20
    total_difficulty = offensive_strength * defensive_strength * ranking_factor
    return total_difficulty

# Appliquer la fonction d'évaluation de la difficulté
df_2023_2024['difficulty'] = df_2023_2024.apply(evaluate_difficulty, axis=1)

# Calcul des quartiles
Q1 = df_2023_2024['difficulty'].quantile(0.25)
Q3 = df_2023_2024['difficulty'].quantile(0.75)

# Catégoriser les équipes en fonction des quartiles
def categorize_difficulty(row):
    if row['difficulty'] <= Q1:
        return 'Easy'
    elif row['difficulty'] <= Q3:
        return 'Medium'
    else:
        return 'Hard'

df_2023_2024['difficulty_category'] = df_2023_2024.apply(categorize_difficulty, axis=1)
df_2023_2024['season'] = '2024/2025'



def set_team_difficulty(row):
  seasons_includes=['2024/2025']
  if row['season'] in seasons_includes:
    season = row['season']
    team = row['team_x']
    opponent = row['opp_team_name']

    # Filtrer les données pour la saison
    full_df = df_2023_2024[df_2023_2024['season'] == season]

    # Récupérer la difficulté de l'équipe et de l'adversaire
    # Vérifier si le DataFrame filtré est vide avant d'accéder aux valeurs
    team_df = full_df[full_df['team'] == team] # Create a separate dataframe for team
    opponent_df = full_df[full_df['team'] == opponent] # Create a separate dataframe for opponent

    if team_df.empty: #Vérifier si l'équipe ou l'adversaire ne sont pas trouvés
        row['team_difficulty'] = 'Easy' # Ou toute autre valeur par défaut que vous préférez
        row['team_difficulty_value'] = 0
    else:
        row['team_difficulty'] = team_df['difficulty_category'].values[0]
        row['team_difficulty_value'] = team_df['difficulty'].values[0]

    if opponent_df.empty:
        row['team_oppent_difficulty'] = 'Easy'
        row['team_oppent_difficulty_value'] = 0
    else:
        row['team_oppent_difficulty'] = opponent_df['difficulty_category'].values[0]
        row['team_oppent_difficulty_value'] = opponent_df['difficulty'].values[0]

  else:
        row['team_difficulty'] = None
        row['team_oppent_difficulty'] = None
        row['team_difficulty_value'] = None
        row['team_oppent_difficulty_value'] = None
  return row # Retourner la ligne modifiée
df = df.apply(set_team_difficulty, axis=1)

for true_name, wrong_name in zip(fixable, wrong):
    df.loc[df['name'] == wrong_name, 'name'] = true_name
#print(df.head(5))
print("#"*40)
df_full=pd.concat([df_full_data,df])

df_test=df_full.loc[df_full['name'] == 'Mohamed Salah']
#df_test['goals_scored_rolling'].iloc[-1] = df_test['goals_scored_rolling'].iloc[-4:-1].mean()
df_test['goals_scored_rolling'].iloc[-1] = df_test['goals_scored'].iloc[-4:-1].mean()

print(df_test[['goals_scored','goals_scored_rolling']].iloc[-4:])

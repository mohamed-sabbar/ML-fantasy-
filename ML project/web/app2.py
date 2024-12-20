from flask import Flask, render_template, Response, request
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import requests
from PIL import Image
import base64
import io
import pandas as pd

# Charger les données
df = pd.read_csv('C:\\Users\\moham\\Downloads\\df_total (1).csv')
round = 15
df = df.loc[df['round'] == round]
df = df.sort_values(by='predections', ascending=False)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('predictions.html')

@app.route('/plot', methods=['GET', 'POST'])
def plot_png():
    position = None
    filtered_df = df.copy()  # Créer une copie pour ne pas modifier l'original
    
    if request.method == 'POST':
        position = request.form.get('position')
        if position:
            filtered_df = filtered_df.loc[filtered_df['position'] == position]

    # Limiter à 5 meilleurs joueurs
    top_players = filtered_df.head(5)

    if top_players.empty:
        return "Aucun joueur trouvé pour cette position.", 404

    player_names = top_players['name']
    scores = top_players['predections']
    
    # Récupérer des images dynamiquement (ou utilisez une colonne d'URL si disponible)
    image_urls = [
        'https://resources.premierleague.com/premierleague/photos/players/250x250/p118748.png',
        'https://resources.premierleague.com/premierleague/photos/players/250x250/p232980.png',
        'https://resources.premierleague.com/premierleague/photos/players/250x250/p60706.png'
    ]
    
    # Créer le graphique
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(player_names, scores, color="#2c3e50")

    for bar, img_url in zip(bars, image_urls[:len(player_names)]):  # Ajuster au nombre de joueurs
        try:
            response = requests.get(img_url)
            response.raise_for_status()
            img = Image.open(io.BytesIO(response.content))

            # Ajuster et afficher l'image
            imagebox = OffsetImage(img, zoom=0.2)
            ab = AnnotationBbox(
                imagebox,
                (bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05),
                xycoords='data',
                frameon=False,
                box_alignment=(0.5, 0)
            )
            ax.add_artist(ab)
        except Exception as e:
            print(f"Erreur lors du chargement de l'image : {e}")
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylabel("Total points")
    
    plt.tight_layout()

    # Convertir le graphique en image
    output = io.BytesIO()
    plt.savefig(output, format="png", bbox_inches="tight", transparent=True)
    output.seek(0)
    plt.close()
    plot_data = base64.b64encode(output.getvalue()).decode('utf-8')

    return render_template('predictions.html', plot_url=plot_data, position=position)

if __name__ == '__main__':
    app.run(debug=True)

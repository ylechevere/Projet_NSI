# Importer les modules Flask et sqlite3
from flask import Flask, render_template, request
import sqlite3

# Créer une instance de l'application Flask
app = Flask(__name__)

# Route principale qui affiche tous les éléments de la table 'brawler'
@app.route('/', methods=['GET', 'POST'])
def homepage():
    # Connexion à la base de données SQLite
    connexion = sqlite3.connect("brawl_star.db")
    curseur = connexion.cursor()

    # Requête pour sélectionner tous les éléments de la table 'brawler'
    rep = f"""SELECT * FROM brawler ;"""
    result = curseur.execute(rep).fetchall()
    connexion.close()# Fermer la connexion à la base de données
    return render_template('homepage.html', repetition=result)# Rendre le modèle 'homepage.html' avec les résultats de la requête

# Route pour filtrer et afficher les détails d'un brawler en fonction du formulaire
@app.route('/brawler/', methods=['POST'])
def brawler():
    if request.method == 'POST': # Vérifier si la méthode de la requête est POST
        bs_nom = request.form['star']# Récupérer la valeur du formulaire avec le nom 'star'
        # Connexion à la base de données SQLite
        connexion = sqlite3.connect("brawl_star.db")
        curseur = connexion.cursor()
        # Requête pour sélectionner les éléments de la table 'brawler' avec un nom correspondant au formulaire
        X = curseur.execute(f"""SELECT * FROM brawler WHERE name LIKE '%{bs_nom}%' """)
        result = curseur.fetchall()
        connexion.close()# Fermer la connexion à la base de données
        # Si un seul résultat est trouvé, afficher les détails du brawler
        if len(result) == 1:
            result = result[0]
            return render_template('brawler.html', titre=bs_nom, id_B=result[0], name=result[1], classs=result[2], rarity=result[3],
                                   mastery=result[4], B_img=result[5], rangee=result[6], reload=result[7], damage=result[8],
                                   hp=result[9], speed=result[10], nameG1=result[11], nameG2=result[12], resumeG1=result[13],
                                   resumeG2=result[14], descG1=result[15], descG2=result[16], imgG1=result[17], imgG2=result[18],
                                   namePS1=result[19], namePS2=result[20], resumePS1=result[21], resumePS2=result[22],
                                   descPS1=result[23], descPS2=result[24], imgPS1=result[25], imgPS2=result[26])
        else:
            # Si aucun ou plusieurs résultats sont trouvés, afficher la page 'no_result.html'
            return render_template('no_result.html', result=result)

# Route pour afficher les détails d'un brawler en fonction de l'ID dans l'URL
@app.route('/brawler_2/<star>')
def brawler_2(star):
    # Connexion à la base de données SQLite
    connexion = sqlite3.connect("brawl_star.db")
    curseur = connexion.cursor()
    # Requête pour sélectionner les éléments de la table 'brawler' avec un ID correspondant
    X = curseur.execute(f"""SELECT * FROM brawler WHERE id_B='{star}' """)
    result = curseur.fetchall()
    connexion.close()# Fermer la connexion à la base de données
    if len(result) == 1:# Si un seul résultat est trouvé, afficher les détails du brawler
        result = result[0]
        return render_template('brawler.html', titre=result[1], id_B=result[0], name=result[1], classs=result[2], rarity=result[3],
                               mastery=result[4], B_img=result[5], rangee=result[6], reload=result[7],
                               damage=result[8], hp=result[9], speed=result[10], nameG1=result[11],
                               nameG2=result[12], resumeG1=result[13], resumeG2=result[14], descG1=result[15], descG2=result[16],
                               imgG1=result[17], imgG2=result[18], namePS1=result[19], namePS2=result[20], resumePS1=result[21], resumePS2=result[22], descPS1=result[23],
                               descPS2=result[24], imgPS1=result[25], imgPS2=result[26])
    else:
        # Si aucun ou plusieurs résultats sont trouvés, afficher la page 'no_result.html'
        return render_template('no_result.html', result=result)


if __name__ == "__main__":
    app.run(port=5000)

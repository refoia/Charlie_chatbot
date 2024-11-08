import tkinter as tk
from tkinter import scrolledtext, filedialog
import requests
from bs4 import BeautifulSoup
import numpy as np
from scipy.spatial.distance import cosine

# Clé API et URL de l'API Mistral
api_key = " "
api_url = "https://api.mistral.ai/v1/chat/completions"

# Préparez les en-têtes d'authentification
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Fonction pour poser une question à l'API Mistral
def poser_question_a_mistral(question):
    data = {
        "model": "mistral-small-2409",
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "max_tokens": 2500
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"Erreur : {response.status_code} - {response.text}"

# Fonction pour effectuer une recherche Bing
def connssaince_plus(recherche):
    url = f"https://www.bing.com/search?q={recherche}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        result_snippets = soup.find_all('p')
        bing_resultat = "\n".join([snippet.get_text() for snippet in result_snippets if snippet.get_text()])
        return bing_resultat
    except Exception as e:
        return f"Erreur lors de la recherche Bing: {e}"

# Fonctions mathématiques pour analyser les réponses
def similarite_cosinus(texte1, texte2):
    vect1 = np.random.rand(100)
    vect2 = np.random.rand(100)
    return 1 - cosine(vect1, vect2)

def moyenne_ponderee(valeurs, poids):
    return np.average(valeurs, weights=poids)

def ecart_type(valeurs):
    return np.std(valeurs)

def probabilite_succes(valeurs):
    total = sum(valeurs)
    return [val / total for val in valeurs]

def interpolation(valeurs):
    return np.interp(np.linspace(0, len(valeurs)-1, num=10), np.arange(len(valeurs)), valeurs)

# Fonction principale de Charlie le Stratège
def charlie_stratege(question):
    reponse_mistral = poser_question_a_mistral(question)
    recherche_bing = connssaince_plus(question)
    similarite = similarite_cosinus(reponse_mistral, question)
    qualite_reponse = moyenne_ponderee([0.6, 0.8, 0.7], [0.3, 0.4, 0.3])
    variation = ecart_type([0.7, 0.75, 0.8])
    probas = probabilite_succes([0.6, 0.4])
    interpolation_result = interpolation([0.6, 0.8, 0.7])

    if similarite < 0.7:
        question_amelioree = f"{question} Peux-tu clarifier davantage la perspective technique ?"
    else:
        question_amelioree = question

    nouvelle_reponse = poser_question_a_mistral(question_amelioree)
    resultat = f"Réponse de Charlie : {nouvelle_reponse}\n\nRecherche Bing :\n{recherche_bing}"
    return resultat

# Fonction pour sauvegarder le contenu de la zone de texte dans un fichier
def sauvegarder_conversation():
    contenu = reponse_text.get("1.0", tk.END)
    fichier = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if fichier:
        fichier.write(contenu)
        fichier.close()

# Interface graphique avec Tkinter
def envoyer_question():
    question = question_entry.get()
    if question.lower() == "quitter":
        root.quit()
    else:
        reponse = charlie_stratege(question)
        reponse_text.insert(tk.END, f"Vous : {question}\n")
        reponse_text.insert(tk.END, f"Charlie le Stratège : {reponse}\n\n")
        question_entry.delete(0, tk.END)

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Charlie le Stratège")

# Liste pour stocker l'historique des questions et réponses
historique = []

# Fonction pour afficher l'historique
def afficher_historique():
    historique_text.delete("1.0", tk.END)
    for question, reponse in historique:
        historique_text.insert(tk.END, f"Vous : {question}\n")
        historique_text.insert(tk.END, f"Charlie le Stratège : {reponse}\n\n")

# Fonction pour envoyer une question et mettre à jour l'historique
def envoyer_question():
    question = question_entry.get()
    if question.lower() == "quitter":
        root.quit()
    else:
        reponse = charlie_stratege(question)
        reponse_text.insert(tk.END, f"Vous : {question}\n")
        reponse_text.insert(tk.END, f"Charlie le Stratège : {reponse}\n\n")
        historique.append((question, reponse))
        question_entry.delete(0, tk.END)

# Zone de texte pour afficher l'historique
historique_text = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
historique_text.pack()

# Bouton pour afficher l'historique
afficher_historique_button = tk.Button(root, text="Afficher l'historique", command=afficher_historique)
afficher_historique_button.pack()

# Fonction pour effectuer une recherche Bing avancée
def recherche_avancee(recherche, filtres):
    url = f"https://www.bing.com/search?q={recherche}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        result_snippets = soup.find_all('p')
        bing_resultat = "\n".join([snippet.get_text() for snippet in result_snippets if snippet.get_text()])
        return bing_resultat
    except Exception as e:
        return f"Erreur lors de la recherche Bing: {e}"

# Fonction pour envoyer une question avec recherche avancée
def envoyer_question_avancee():
    question = question_entry.get()
    filtres = filtres_entry.get()
    if question.lower() == "quitter":
        root.quit()
    else:
        reponse = charlie_stratege(question)
        recherche_bing = recherche_avancee(question, filtres)
        reponse_text.insert(tk.END, f"Vous : {question}\n")
        reponse_text.insert(tk.END, f"Charlie le Stratège : {reponse}\n")
        reponse_text.insert(tk.END, f"Recherche Bing avancée : {recherche_bing}\n\n")
        question_entry.delete(0, tk.END)
        filtres_entry.delete(0, tk.END)

# Champ de saisie des filtres
filtres_label = tk.Label(root, text="Filtres de recherche :")
filtres_label.pack()

filtres_entry = tk.Entry(root, width=60)
filtres_entry.pack()

# Bouton pour envoyer une question avec recherche avancée
envoyer_avancee_button = tk.Button(root, text="Envoyer avec recherche avancée", command=envoyer_question_avancee)
envoyer_avancee_button.pack()


from textblob import TextBlob

# Fonction pour analyser le sentiment d'un texte
def analyser_sentiment(texte):
    blob = TextBlob(texte)
    return blob.sentiment.polarity

# Fonction pour envoyer une question avec analyse de sentiment
def envoyer_question_avec_sentiment():
    question = question_entry.get()
    if question.lower() == "quitter":
        root.quit()
    else:
        reponse = charlie_stratege(question)
        sentiment = analyser_sentiment(reponse)
        reponse_text.insert(tk.END, f"Vous : {question}\n")
        reponse_text.insert(tk.END, f"Charlie le Stratège : {reponse}\n")
        reponse_text.insert(tk.END, f"Sentiment : {sentiment}\n\n")
        question_entry.delete(0, tk.END)

# Bouton pour envoyer une question avec analyse de sentiment
envoyer_sentiment_button = tk.Button(root, text="Envoyer avec analyse de sentiment", command=envoyer_question_avec_sentiment)
envoyer_sentiment_button.pack()



import tkinter.messagebox as messagebox

# Fonction pour envoyer une question avec notification
def envoyer_question_avec_notification():
    question = question_entry.get()
    if question.lower() == "quitter":
        root.quit()
    else:
        reponse = charlie_stratege(question)
        reponse_text.insert(tk.END, f"Vous : {question}\n")
        reponse_text.insert(tk.END, f"Charlie le Stratège : {reponse}\n\n")
        messagebox.showinfo("Notification", "La réponse est prête !")
        question_entry.delete(0, tk.END)

# Bouton pour envoyer une question avec notification
envoyer_notification_button = tk.Button(root, text="Envoyer avec notification", command=envoyer_question_avec_notification)
envoyer_notification_button.pack()



# Fonction pour changer la couleur de fond de la fenêtre
def changer_couleur_fond():
    couleur = couleur_entry.get()
    root.configure(bg=couleur)

# Champ de saisie de la couleur de fond
couleur_label = tk.Label(root, text="Couleur de fond :")
couleur_label.pack()

couleur_entry = tk.Entry(root, width=60)
couleur_entry.pack()

# Bouton pour changer la couleur de fond
changer_couleur_button = tk.Button(root, text="Changer la couleur de fond", command=changer_couleur_fond)
changer_couleur_button.pack()


 


# Champ de saisie de la question
question_label = tk.Label(root, text="Posez votre question à Charlie le Stratège :")
question_label.pack()

question_entry = tk.Entry(root, width=60)
question_entry.pack()

envoyer_button = tk.Button(root, text="Envoyer", command=envoyer_question)
envoyer_button.pack()

# Bouton pour sauvegarder la conversation
sauvegarder_button = tk.Button(root, text="Sauvegarder", command=sauvegarder_conversation)
sauvegarder_button.pack()

# Zone de texte pour afficher la conversation
reponse_text = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
reponse_text.pack()

# Lancer l'interface graphique
root.mainloop()

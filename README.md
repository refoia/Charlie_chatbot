 

---

# Charlie le Stratège - Chatbot IA

**Charlie le Stratège** est un chatbot IA avancé conçu pour répondre aux questions, fournir des informations contextuelles, et effectuer des analyses de texte intelligentes. Basé sur l'intégration de l'API Mistral, des fonctionnalités de recherche Bing, et des algorithmes d'analyse mathématique, Charlie offre une expérience utilisateur enrichie et polyvalente.

## Fonctionnalités

- **Réponses IA** : Utilise l'API Mistral pour fournir des réponses personnalisées en fonction de la question de l'utilisateur.
- **Recherche web** : Effectue des recherches contextuelles via Bing pour compléter les réponses IA.
- **Analyses avancées** : Comprend des fonctions de similarité cosinus, moyenne pondérée, écart-type et interpolation pour évaluer la qualité des réponses.
- **Interface utilisateur** : Interface graphique simple avec Tkinter, permettant une interaction fluide avec Charlie.
- **Sauvegarde des conversations** : Option pour enregistrer la conversation dans un fichier texte.

## Technologies utilisées

- **Python** : Langage de programmation principal.
- **API Mistral** : Pour des réponses conversationnelles.
- **BeautifulSoup** : Pour l'extraction de contenu lors des recherches Bing.
- **NumPy & SciPy** : Pour les calculs mathématiques et les analyses de texte.
- **Tkinter** : Interface utilisateur graphique.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre_nom_utilisateur/charlie-le-stratege.git
   cd charlie-le-stratege
   ```
2. Installez les dépendances nécessaires :
   ```bash
   pip install requests beautifulsoup4 numpy scipy
   ```

3. Ajoutez votre clé API Mistral dans le code source (`api_key` variable).

4. Lancez l'application :
   ```bash
   python charlie_le_stratege.py
   ```

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez améliorer Charlie, proposer de nouvelles fonctionnalités ou corriger des bugs, n'hésitez pas à soumettre une pull request.

## Licence

Ce projet est sous licence MIT - consultez le fichier [LICENSE](LICENSE) pour plus de détails.
 

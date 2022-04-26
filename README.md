# csv_manipulation

## Documentation

1. Introduction
2. Librairies utilisées
3. Notre démarche
4. Détail du code

## Introduction
Consigne :
A partir d'une source de donnée choisies ou créées par vous, créer un programme Python d'acquisition (à partir d'un fichier CSV) et de restitution de données.

Nous avons décidé pour notre part, de partir sur l'option de la création de graphiques via différentes librairies.

## Librairies utilisées
Pour ce projet, nous avons eu recours aux librairies [matplotlib](https://matplotlib.org/) (notamment pour la création des différents graphiques) et de [pandas](https://pandas.pydata.org/) pour le traitement et l'interprétation des données du fichier .csv

## Notre démarche
Le but était de restituer de la donnée __réellement intéressante__ à analyser. Pour cela, quoi de mieux que visualiser les record-men de ce dataset? Dans chacuns des graphiques sont affichés les **5 à 10 collections de NFT** (Non-fungible token ou jetons non-fongibles) avec la valeur la plus *élevée* associée à la colonne du dataset précisée.

## Détail du code

Durant le développement de ce script, deux fonctions furent créées : `plot_bar_chart` et `plot_pie_chart`

```python
def plot_bar_chart(data: p.DataFrame, name: str, color: str, fig_id: int):
    ...

def plot_pie_chart(data: p.DataFrame, name: str, fig_id: int) -> any:
    ...
```

Comme leur nom l'indique, ces deux fonctions permettent d'afficher à partir d'un dataset, les 5 à 10 plus grandes valeurs d'une colonne `name` à partir d'un DataFrame panda `data`, récupérée d'un dataset. Les paramètres `color` et `fig_id` ne sont que des ints qui s'incrémentent, présents pour qu'il n'y ai pas de conflits lors de l'affichage des différents graphiques.

## Contribuer au projet
Si vous souhaitez aider au développement du projet et y contribuer (beginner-friendly, créée uniquement pour les amis du lycée), rendez vous sur [CONTRIBUTE.md](CONTRIBUTE.md)

**Projet de parralélisme maximal**

*Objectifs*

Développer une libraire en Python pour automatiser la parallélisation maximale de systèmes de tâches. L’utilisateur doit pouvoir spécifier des tâches quelconques, interagissant à travers un ensemble arbitraire de variables, et pouvoir :
  
1. obtenir le système de tâches de parallélisme maximal réunissant les tâches en entrée,
2. exécuter le système de tâches de façon séquentielle, tout en respectant les contraintes
de précédence,
3. exécuter le système de tâches en parallèle, tout en respectant les contraintes de précédence.

*Fonctionnalités*

- dupliquer(): Vérifie qu'il n'y a pas de doublon dans la liste de tâches
- getDependencies(): Renvoie les dépendances d'une tâche
- bernstein(): Verifie les conditions de Bernstein
- isExistingTask(): Vérifie que les tâches existes bien dans le dictionnaire
- isTaskDict(): Vérifie si toutes les tâches ont leur dépendances spécifiées dans le dictionnaire
- firstTasks(): Retourne la première tâche sans dependances
- nexTasks(): Retourne les tâches suivantes d'une tâche en fonction de ses dépendances
- runTask(): Execute les tâches dans l'ordre des dépendances
- maxParDependencies(): Méthode pour optimiser le parallélisme des tâches 

*Installation*

$ pip install graphviz

## Fait Par
- [mathieu Riera]
- [Wessim Azlouk]
- [Hugo Marques ]
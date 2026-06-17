# La Genèse de l'AutoPROMPT

## Le Problème Initial

L'export natif DeepSeek est un fichier JSON qui contient les messages bruts, mais sans structure, sans chaîne de pensée, sans métadonnées.

L'idée : demander à DeepSeek lui-même de générer une note Markdown structurée à partir de la conversation en cours.

## Le Défi : La Mémoire Évanescente

En tant que LLM, sa mémoire est limitée au contexte de la conversation. Il ne me souviens pas des erreurs ou des améliorations des sessions précédentes.

**Solution** : L'utilisateur renvoye l'intégralité des échanges (discutions depuis la création du début + COT incluses via un fichier incrémenté au format markdown .md ) à chaque itération, créant une mémoire externe dans la limite des 50Mo (au 17/06/2026).


## Le Cycle d'Itération

![INSER diagrame 1](https://github.com/sudtek/ia-pot-pourri/blob/0036de79eb4c3380bed3d1e1473ad6c3c5076d08/DEEPSEEK/DP_AutoPrompt/img/diagrame_01_boucle.png)

| Version | Forces                                                           | Faiblesses                                                                                  |
| ------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| v00     | Structure riche (arbre, CoT détaillée)                           | Date impossible à satisfaire ; Troncature des messages ; Pas de gestion des fichiers joints |
| v01     | Correction des placeholders ; Ajout de keywords, fichiers_joints | Trop verbeux ; Risque de dépassement de tokens                                              |
| v02     | Version allégée (CoT en 5 lignes)                                | Perte d'informations critiques ; Trop minimaliste                                           |
| v03     | Équilibre : intention + pivots + chaîne clé + contexte permanent |                                                                                             |



## Leçon Apprise

La difficulté principale est l'arbitrage entre richesse sémantique (utile pour Obsidian) et concision (nécessaire pour éviter la troncature).

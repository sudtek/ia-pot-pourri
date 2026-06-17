# La Genèse de l'AutoPROMPT

## Le Problème Initial

L'export natif DeepSeek est un fichier JSON qui contient les messages bruts, mais sans structure, sans chaîne de pensée, sans métadonnées.

L'idée de départ était simple : Demander à DeepSeek lui-même de générer une note Markdown structurée à partir de la conversation en cours. Un prompt auto‑suffisant, copié‑collé dans n’importe quel échange, aurait pu suffire… mais la réalité s’est révélée plus complexe.

## Le Défi : La Mémoire Évanescente

Dans un LLM, la mémoire est limitée au contexte de la conversation. Il ne se souvient pas des erreurs ou des améliorations des sessions précédentes.

**Solution trouvée** : L'utilisateur a renvoyé l'intégralité des échanges (y compris les chaînes de pensée complètes) à chaque itération, sous forme de fichiers Markdown incrémentés. Cela a créé une mémoire externe (dans la limite de 50 Mo autorisée par la plateforme au 17/06/2026), permettant d'analyser les productions successives.

## Le Cycle d'Itération (le "V" Récursif)

Le processus que nous avons suivi est représenté par le diagramme ci‑dessous :

![INSER diagrame 1](https://github.com/sudtek/ia-pot-pourri/blob/0036de79eb4c3380bed3d1e1473ad6c3c5076d08/DEEPSEEK/DP_AutoPrompt/img/diagrame_01_boucle.png)]

Explication par DEEPSEEK lui-même ;) :

**Envoi du prompt vN –** L'utilisateur copie‑colle la version courante du prompt dans la conversation.

**DeepSeek génère la note Markdown –** Le modèle applique le prompt et produit une note structurée.

**L'utilisateur analyse la note –** J'identifie les lacunes, les erreurs et les oublis (dates, fichiers joints, troncatures, etc.).

**Renvoi de TOUTE la conversation + la note + le prompt –** L'utilisateur me fournit l'historique complet, y compris les fichiers joints, pour que j'aie un contexte global.

**DeepSeek analyse avec des outils d'audit –** J'utilise une grille d'analyse (SWOT) pour évaluer systématiquement les forces et faiblesses de la version testée.

**Proposition d'une nouvelle version vN+1 –** Sur la base de l'analyse, je propose un prompt amélioré, qui sera à nouveau testé.

Ce cycle a été répété quatre fois, de v00 à v03.

## La Méthode d'Analyse : SWOT (Forces, Faiblesses, Opportunités, Menaces)

Pour structurer l'introspection, j'ai utilisé la méthode SWOT, empruntée au monde du management stratégique. Elle permet de poser un diagnostic clair et complet sur chaque version.


## 📊 🔎 Définition des critères

| Critère      | Ce qu'il évalue                                                                                             |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| Forces       | Ce qui fonctionne déjà bien dans le prompt                                                                  |
| Faiblesses   | Les lacunes, erreurs ou omissions constatées dans la note générée.                                          |
| Opportunités | Les améliorations possibles (nouvelles sections, meilleure gestion des cas particuliers).                   |
| Menaces      | Les risques pour l'utilisateur (dépassement de tokens, oubli de remplacement des placeholders, troncature). |


## Application aux versions successives

| Version | Forces                                                           | Faiblesses                                                                                  |
| ------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| v00     | Structure riche (arbre, CoT détaillée)                           | Date impossible à satisfaire ; Troncature des messages ; Pas de gestion des fichiers joints |
| v01     | Correction des placeholders ; Ajout de keywords, fichiers_joints | Trop verbeux ; Risque de dépassement de tokens                                              |
| v02     | Version allégée (CoT en 5 lignes)                                | Perte d'informations critiques ; Trop minimaliste                                           |
| v03     | Équilibre : intention + pivots + chaîne clé + contexte permanent |                                                                                             |

| Version | Forces                                                                                                                                    | Faiblesses                                                                                                                                    | Opportunités                                                                                             | Menaces                                                                                       |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **v00** | Structure très riche (arbre, CoT détaillée, frontmatter complet).                                                                         | Placeholder `{{date_ISO_ce_moment}}` impossible à satisfaire ; Troncature des messages dans `<details>` ; Pas de gestion des fichiers joints. | Ajouter des mots‑clés (`keywords`), une section pour les fichiers joints, un nom de fichier suggéré.     | L'utilisateur peut oublier de remplacer la date ; la note peut dépasser la limite de tokens.  |
| **v01** | Correction des placeholders (date à remplacer par l'utilisateur) ; Ajout de `keywords`, `fichiers_joints` ; Suggestion de nom de fichier. | Devenu trop verbeux ; Risque de dépassement de tokens ; Chaîne de pensée potentiellement longue.                                              | Alléger le prompt en supprimant les sections redondantes ; Introduire une règle de troncature proactive. | Le modèle peut encore abréger les messages malgré la consigne ; le frontmatter devient lourd. |
| **v02** | Version allégée (CoT en 5 lignes, troncature à 3000 tokens, fusion des sections).                                                         | Perte d'informations critiques (arbre, vérifications, distinction hypothèses/raisonnements) ; Devenu trop minimaliste.                        | Réintroduire l'essentiel sous forme compressée (intention, pivots, chaîne clé, contexte permanent).      | La note peut devenir trop superficielle pour être réellement utile dans Obsidian.             |
| **v03** | Équilibre : intention + pivots + chaîne clé + contexte permanent ; Structure claire et concise.                                           | Aucune faiblesse majeure identifiée à ce stade.                                                                                               | Ajouter un mode « compact » ou « complet » selon les besoins.                                            | Risque de rigidité pour des conversations non linéaires ; à tester sur différents cas.        |

## L'Évolution Conceptuelle : De la CoT à l'Intention

L'itération a permis un **changement de paradigme** : 

- **v00 – v02** : On cherchait à capturer la **Chaîne de Pensée (CoT)** de manière exhaustive (arbre, hypothèses, vérifications). Mais l'arbre devenait une forêt, consommant trop de tokens.
_* Note perso YS #0 du 17/06/2026 : Le fait de travailler sur une version gratuite minimaliste / limitée du LLM à l'avantage d'obliger à trouver des solutions "sioux" pour tirer un maximum en limitant sa consomation de tokens et nous pousse à une autre approche._

- **v03** : Sur la base de vos retours, j'ai remplacé l'arbre par une **structure intentionnelle** : l'intention principale, les pivots logiques, une chaîne clé illustrative et le contexte permanent. Cela permet de conserver l'essentiel du raisonnement sans l'explosion combinatoire.

Cette approche s'inspire des concepts de **treillis*** et de **fermeture de Galois*** : On ne stocke pas tous les chemins, mais les **générateurs** et les **règles invariantes** qui permettent de reconstruire l'essentiel. 

_* Note perso YS #1 du 17/06/2026 : On développera plus tard une SKILL treillis + fermeture de Galois + une implémentation "en dur" 2 approches indispensables_

#### Leçons Apprises pour l'Ingénierie des Prompts

1. **L'itération est indispensable** : Un prompt rarement parfait du premier coup. Il faut le confronter à des cas réels.

2. **La mémoire externe est cruciale** : Pour un LLM, l'historique complet sert de « mémoire de travail » pour l'auto‑amélioration.

3. **L'analyse SWOT structure l'introspection** : Elle évite le biais de confirmation et force à regarder les faiblesses et les menaces.

4. **L'équilibre entre richesse et concision est un art** : Il faut trouver le point où la note est utile sans être trop lourde.

5. **L'innovation peut venir du dialogue** : La notion d'intentionnalité* est née de nos échanges, pas d'une réflexion solitaire.

_* Note perso YS #2 du 17/06/2026 : Toujours dans la veine treillis + fermeture de Galois il faut envisager de pouvoir passer du COT <--> COI_

## Prochaines Étapes Possibles

- Tester la v03 sur une variété de conversations (longues, techniques, avec pièces jointes) pour valider sa robustesse.

- Créer une variante « Skills » pour extraire les compétences opérationnelles mobilisées (sans alourdir le README principal).

- Automatiser l'export via l'API DeepSeek (payant) pour les utilisateurs qui ont des centaines de conversations.

---

*Ce document évoluera avec les futures itérations et évolutions.*

Version du 17 / juin / 2026 par yannick SUDRIE.

_* Note perso YS finale du 17/06/2026 :  Plus tard pour ne pas surcharger il faudra introduire la notion de raisonement ce que l'on sait VS ce que l'on ignore ... _

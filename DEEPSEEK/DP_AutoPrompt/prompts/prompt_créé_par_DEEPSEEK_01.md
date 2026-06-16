**INSTRUCTION SPÉCIALE – EXPORT OBSIDIAN (v01)**

Ne réponds pas de manière conversationnelle normale.  
Génère **UNIQUEMENT** une note Markdown structurée selon le template ci-dessous, basée sur l'intégralité de la conversation en cours (depuis le premier message jusqu'à cet instant).  
Tu dois extraire toi-même les problématiques, résumés, contextes, solutions, chaîne de pensée, etc.

---

### RÈGLES IMPÉRATIVES (à appliquer sans exception)

1. **Pas de texte hors Markdown** – ni introduction, ni commentaire, ni remerciement.
2. **Dates** : utilise `YYYY-MM-DD HH:MM` (par exemple `2025-01-15 14:30`).  
   *Remarque : DeepSeek ne connaît pas l’heure exacte. Tu écriras `YYYY-MM-DD HH:MM (à corriger par l’utilisateur)`.*
3. **Absence d’information** → écrire `"Aucune explicitement mentionnée"`.
4. **Bloc `<details>`** : copie **INTÉGRALEMENT** chaque message, **sans aucune abréviation, ellipse ou synthèse**. Même les longs messages doivent être copiés dans leur totalité.
5. **Fichiers joints** : si la conversation contient des fichiers (images, documents…), liste leurs noms dans le frontmatter (`fichiers_joints: [nom1, nom2]`) et ajoute une sous‑section `## Fichiers joints` avec une description sommaire.
6. **Chaîne de pensée** : reconstruis‑la en t’appuyant sur les raisonnements **explicitement écrits** dans tes messages. Si tu as exprimé des doutes, hypothèses, vérifications, liste‑les. Si tu n’as pas explicité ta pensée, propose une reconstruction plausible basée sur la logique de tes réponses.
7. **Ressources mentionnées** : inclus les noms d’outils, logiciels, extensions (ex: « ChatInsights (outil Python) ») même sans URL. Les liens web doivent comporter le titre.
8. **Troncature** : si la conversation est trop longue pour tenir dans la réponse, ajoute en haut de la note un avertissement `> [!warning] Conversation partiellement tronquée – voici un résumé des échanges manquants` et fournis un résumé des messages omis.

---

### TEMPLATE À RESPECTER À LA LETTRE

```markdown
---

date: YYYY-MM-DD HH:MM (à corriger par l’utilisateur)
conversation_id: "AAAA-MM-JJ_titre_abrege"
statut: "résolu|en cours|abandonné|non spécifié"
priorité: "haute|moyenne|basse|non spécifiée"
domaines: [liste, de, domaines]
keywords: [mot, clé, supplémentaire]
tags: [deepseek, conversation, sauvegarde, obsidian]
version_export: 2
fichiers_joints: []

---

# Problématique(s)

[Une phrase synthétique, puis une liste à puces des problèmes traités]

## Arbre des sous-problèmes (si applicable)

- Problème principal
  - Sous-problème A
  - Sous-problème B

# Contexte(s)

[Informations nécessaires pour comprendre la conversation sans l'avoir lue]

# Résumé exécutif

> TL;DR en une phrase

# Solutions mises en œuvre ou envisagées

## Solution retenue

Description détaillée, étapes clés (numérotées)

## Alternatives écartées

Pour chaque alternative, une brève raison d’abandon

# Chaîne de pensée (Chain of Thought)

## Hypothèses de départ

## Raisonnements intermédiaires (en t’appuyant sur tes messages)

## Vérifications / doutes exprimés

## Conclusion du raisonnement

# Ressources mentionnées

- Liens web (avec titre)
- Outils / logiciels (même sans URL)
- Commandes shell (bloc ```bash)
- Extraits de code (bloc avec langage)
- Références externes

# Actions restantes / Next steps

- [ ] Action 1
- [ ] Action 2

# Questions en suspens (optionnel)

- ...

> [!note] **Notes personnelles (zone réservée utilisateur)**  
> *À remplir plus tard*

---

<details>
<summary>📜 Conversation complète (intégrale)</summary>

**Moi** : contenu intégral du message  
**Toi (DeepSeek)** : contenu intégral du message  
*(répéter pour chaque échange, sans rien omettre)*

</details>

<!-- Nom de fichier recommandé : YYYY-MM-DJ_titre_abrege.md -->

### RAPPEL FINAL

- N’ajoute **rien** en dehors de ce Markdown.

- Termine par une ligne vide.
```

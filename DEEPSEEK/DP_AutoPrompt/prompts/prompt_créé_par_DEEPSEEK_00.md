**INSTRUCTION SPÉCIALE – EXPORT OBSIDIAN**

Ne réponds pas de manière conversationnelle normale. À la place, génère UNIQUEMENT une note Markdown structurée selon le template ci-dessous, basée sur l'intégralité de la conversation en cours (depuis le premier message jusqu'à cet instant). Tu dois extraire toi-même les problématiques, résumés, contextes, solutions, chain of thought, etc.

TEMPLATE À RESPECTER À LA LETTRE :

---

date: {{date_ISO_ce_moment}}
conversation_id: "{{titre ou slug déduit du sujet}}"
statut: "résolu|en cours|abandonné" (à déduire)
priorité: "haute|moyenne|basse"
domaines: [liste, de, domaines]
tags: [deepseek, conversation, sauvegarde, obsidian]
version_export: 1

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

Pour chaque alternative, une brève raison d'abandon

# Chaîne de pensée (Chain of Thought)

## Hypothèses de départ

## Raisonnements intermédiaires

## Vérifications / doutes exprimés

## Conclusion du raisonnement

# Ressources mentionnées

- Liens web (avec titre)
- Commandes shell (bloc ```bash)
- Extraits de code (bloc avec langage)
- Références externes

# Actions restantes / Next steps

- [ ] Action 1
- [ ] Action 2

# Notes personnelles (zone réservée utilisateur)

*À remplir plus tard*

---

<details>
<summary>📜 Conversation complète (intégrale)</summary>

[Copie ici l'historique complet des messages, en respectant le format : 
**Moi** : contenu
**Toi (DeepSeek)** : contenu
]

</details>

RÈGLES COMPLÉMENTAIRES :

- N'ajoute aucun texte en dehors du Markdown (pas de "Voici votre note", pas de commentaires introductifs).
- Utilise des dates ISO (ex: 2025-01-15 14:30).
- Si une information n'existe pas dans la conversation (ex: pas d'alternative écartée), écris "Aucune explicitement mentionnée".
- Pour la chain of thought, reconstruis-la à partir de tes propres raisonnements internes que tu as eus pendant la conversation (tu as accès à ton historique).
- Le bloc `<details>` doit contenir TOUS les messages, sans résumé.
- Termine par une ligne vide.

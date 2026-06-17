# AutoPROMPT : Export DeepSeek vers Markdown

[![Version](https://img.shields.io/badge/version-3.0-blue.svg)](https://github.com/sudtek/ia-pot-pourri)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

yannick SUDRIE 17_juin_2026

Un **autoPROMPT** conversationnel qui transforme n'importe quelle conversation DeepSeek en note Markdown structurée, prête pour Obsidian.

---

## 🎯 Pourquoi ce prompt ?

> *"L'export natif DeepSeek est incomplet. Les extensions de navigateur sont souvent opaques ou peu fiables. J'ai donc conçu un prompt qui fait de l'IA elle-même l'outil d'exportation."*

| Problème                         | Solution apportée                                                          |
| -------------------------------- | -------------------------------------------------------------------------- |
| Export JSON brut sans structure  | Conversion automatique en Markdown                                         |
| Absence de chaîne de pensée      | Demande explicite à l'IA de restituer son intention et ses pivots logiques |
| Fichiers joints non inclus       | Métadonnées dédiées (`fichiers_joints: []`)                                |
| Pas de métadonnées pour Obsidian | Frontmatter YAML avec tags, priorité, domaine                              |

**Philosophie** : *"Faisons une chose et faisons-la bien : exporter proprement une conversation DeepSeek en Markdown structuré."*

---

## 📄 Le Prompt 01_06_2026_prompt_créé_par_DEEPSEEK_03.md (le plus recent)

Copiez-collez ce prompt **dans votre conversation DeepSeek** :

```markdown
**INSTRUCTION SPÉCIALE – EXPORT OBSIDIAN (v03 – intentionnelle)**

Génère UNIQUEMENT une note Markdown selon le template ci-dessous, basée sur TOUTE la conversation depuis le premier message.
Tu ne dois rien ajouter hors du Markdown.

### RÈGLES

1. **Date** : `date: YYYY-MM-DD HH:MM (à corriger)`
2. **Absence d’info** → `"Aucune"`
3. **Conversation complète** : copie intégrale des messages dans `<details>` (si trop long, tronque avec résumé).
4. **Fichiers joints** : liste dans `fichiers_joints: []`.
5. **Chaîne de pensée** : ne détaille pas l’arbre. Donne plutôt :
   - **Intention principale** (une phrase)
   - **Pivots logiques** (max 3, chaque pivot = un changement de direction)
   - **Chaîne clé** (max 5 lignes, illustrant le raisonnement le plus important)
   - **Contexte permanent** (les éléments, objets, règles qui restent vrais)

### TEMPLATE

```markdown
---
date: YYYY-MM-DD HH:MM (à corriger)
conversation_id: "AAAA-MM-JJ_mot_cle"
statut: "résolu|en cours|abandonné|non spécifié"
priorité: "haute|moyenne|basse|non spécifiée"
domaines: [liste]
tags: [deepseek, obsidian]
version_export: 3
fichiers_joints: []

---

# Problématique(s)

[Une phrase + liste à puces]

# Contexte(s)

[Ce qu’il faut savoir]

# Résumé exécutif

> Une phrase

# Solution retenue

Étapes clés (numérotées)

# Alternatives écartées

(ou "Aucune")

# Intention et chaînes de pensée

- **Intention principale** : ...
- **Pivots logiques** :
  1. ...
  2. ...
- **Chaîne clé** (illustrative) :

  > ...
- **Contexte permanent** : ...

# Ressources

- [Titre](URL) ou Nom d’outil

# Actions restantes

- [ ] Action

> [!note] Notes personnelles

---

<details>
<summary>📜 Conversation (intégrale ou tronquée)</summary>

**Moi** : message complet  
**Toi** : message complet

</details>

<!-- Nom fichier : YYYY-MM-DJ_titre.md -->

**FIN – exécute ce prompt sans ajout.**
```

## 🚀 Utilisation

Copiez le prompt ci-dessus 

Collez-le dans votre conversation DeepSeek

DeepSeek génère une note Markdown structurée

Copiez la note dans un fichier .md dans votre coffre Obsidian

## 📁 Versions antérieures

L'évolution du prompt est disponible dans le dossier [prompts](https://github.com/sudtek/ia-pot-pourri/tree/0036de79eb4c3380bed3d1e1473ad6c3c5076d08/DEEPSEEK/DP_AutoPrompt) :

- prompt_v00.md – Version initiale (naïve)

- prompt_v01.md – Correction des placeholders et enrichissement

- prompt_v02.md – Version allégée (gestion des tokens)

- [prompt_v03.md](https://github.com/sudtek/ia-pot-pourri/blob/0036de79eb4c3380bed3d1e1473ad6c3c5076d08/DEEPSEEK/DP_AutoPrompt/prompts/01_06_2026_prompt_cr%C3%A9%C3%A9_par_DEEPSEEK_03.md) – Version finale (intentionnelle)

## ⚠️ Limites

**Version gratuite (sans API)**

| Limite                          | Description                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Pas de CoT native               | L'export natif ne contient pas les chaînes de raisonnement. Ce prompt demande à l'IA de les reconstruire – ce n'est pas la CoT brute. |
| Synthèse ≠ Sauvegarde intégrale | Le résultat est une synthèse interprétative, pas une copie 1:1.                                                                       |
| Troncature possible             | Pour les très longues conversations, une troncature avec résumé peut être appliquée.                                                  |
| Processus manuel                | Chaque conversation doit être exportée individuellement.                                                                              |

**Passer à l'API (pour automatiser prochaine étape ... )**

| Fonctionnalité     | AutoPROMPT (gratuit)   | API DeepSeek (payant)          |
| ------------------ |:----------------------:|:------------------------------:|
| Export automatique | ❌ Manuel               | ✅ Scriptable                   |
| CoT brute          | ❌ Reconstruction       | ✅ reasoning_content disponible |
| Export intégral    | ⚠️ Troncature possible | ✅ Complet                      |
| Coût               | ✅ 0€                   | 💰 ~$0.14 / 1M tokens          |

# 🔄 Comment ce prompt a-t-il été créé ?

Ce prompt est le fruit de 4 itérations successives où DeepSeek a analysé ses propres productions pour s'améliorer.

**L'étincelle :** L'export natif DeepSeek était incomplet. L'idée était simple : demander à DeepSeek lui-même de générer la note structurée.

**Le défi :** En tant que LLM, sa mémoire est limitée. Il ne se souviens pas des erreurs des versions précédentes.

**La solution :** L'utilisateur a renvoye l'intégralité des échanges à chaque itération, créant une "mémoire externe". Deepseek a utilisé la méthode SWOT pour analyser chaque version.

**Le résultat :** 4 itérations (v00 → v03) ont conduit à un prompt équilibré, capturant l'essentiel sans explosion de tokens.

📖 Pour l'histoire complète (les analyses SWOT, les itérations détaillées, la méthodologie) → lire [META-README.md](https://github.com/sudtek/ia-pot-pourri/blob/0036de79eb4c3380bed3d1e1473ad6c3c5076d08/DEEPSEEK/DP_AutoPrompt/docs/META-README.md)

---

## 🔒 Sécurité & Confidentialité

**Aucune extension de navigateur :** Tout se passe dans la conversation DeepSeek.

**Aucune donnée externe :** Le prompt n'appelle aucun service tiers.

**Contrôle total :** Vous décidez de ce qui est exporté et comment.

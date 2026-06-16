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

# Intention et chaînes de pensée (approche par treillis)

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

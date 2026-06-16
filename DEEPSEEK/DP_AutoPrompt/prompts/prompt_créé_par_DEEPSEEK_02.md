**INSTRUCTION SPÉCIALE – EXPORT OBSIDIAN (v02 – version allégée)**

Génère UNIQUEMENT une note Markdown selon le template ci-dessous, basée sur TOUTE la conversation depuis le premier message.  
Tu ne dois rien ajouter hors du Markdown (pas d’introduction, pas de commentaire).  
Respecte impérativement les règles suivantes pour économiser les tokens et garantir l’exploitabilité.

### RÈGLES (à appliquer sans exception)

1. **Dates** : écris `date: YYYY-MM-DD HH:MM (à remplacer par l’utilisateur)` – ne cherche pas à deviner l’heure.
2. **Absence d’info** → `"Aucune explicitement mentionnée"`.
3. **Conversation complète** :  
   - Si la conversation tient dans la réponse → copie TOUS les messages **intégralement** dans `<details>`.  
   - Si elle est trop longue → insère un avertissement `> [!warning] Version tronquée – seuls les N premiers messages sont conservés` et fournis un résumé des messages manquants.
4. **Fichiers joints** : liste leurs noms dans `fichiers_joints: []` (frontmatter). Pas de section supplémentaire.
5. **Chaîne de pensée** : résume-la en **5 lignes maximum** (hypothèse clé, raisonnement principal, doute, conclusion). Ne pas détailler inutilement.
6. **Ressources** : seulement les URLs complètes (avec titre) ou les noms d’outils cités. Pas de blocs de code vides.
7. **Troncature proactive** : si la note dépasse 3000 tokens, supprime les sections les moins utiles (conserve frontmatter, problématique, solution retenue, chaîne de pensée courte, et les 3 premiers échanges).

### TEMPLATE (à remplir)

```markdown
---

date: YYYY-MM-DD HH:MM (à corriger)
conversation_id: "AAAA-MM-JJ_mot_cle"
statut: "résolu|en cours|abandonné|non spécifié"
priorité: "haute|moyenne|basse|non spécifiée"
domaines: [liste]
tags: [deepseek, obsidian]
version_export: 2
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

# Chaîne de pensée (max 5 lignes)

- Hypothèse :
- Raisonnement :
- Doute :
- Conclusion :

# Ressources

- [Titre](URL) ou Nom d’outil

# Actions restantes

- [ ] Action

> [!note] Notes personnelles (zone utilisateur)

---

<details>
<summary>📜 Conversation (intégrale ou tronquée)</summary>

**Moi** : message complet  
**Toi** : message complet

</details>

<!-- Nom fichier : YYYY-MM-DJ_titre.md -->

**FIN – exécute ce prompt sans ajout.**
```

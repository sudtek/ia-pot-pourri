# Easy Grok Chat Exporter 🔧 (version sécurisée – fork DeepSeek)

https://github.com/Owlock/easy-grok-chat-exporter

> **Le seul exportateur Grok qui extrait les traces de raisonnement de l’IA.**  
> Convertit vos conversations Grok en fichiers Markdown, Texte ou JSONL — avec ou sans la démonstration étape par étape du raisonnement de l’IA. Aucune dépendance, interface CLI interactive.

**Ce fork et sa documentation ont été entièrement produits par [DeepSeek](https://deepseek.com) à partir du projet original d’Owlock, afin d’en corriger deux failles mineures et d’améliorer la clarté des exports.**

---

## 🧭 Table des matières

1. [Présentation du projet](#présentation-du-projet)
2. [Comment récupérer vos données depuis X / Grok](#comment-récupérer-vos-données-depuis-x--grok)
3. [Pourquoi ce fork ?](#pourquoi-ce-fork-)
4. [Principales fonctionnalités](#principales-fonctionnalités)
5. [Ce qui rend cet outil unique](#ce-qui-rend-cet-outil-unique)
6. [Guide d’utilisation étape par étape](#guide-dutilisation-étape-par-étape)
7. [Structure typique du fichier JSON](#structure-typique-du-fichier-json)
8. [Autres solutions recommandées](#autres-solutions-recommandées)
9. [Importation dans d’autres modèles d’IA](#importation-dans-dautres-modèles-dia)
10. [Commandes et options](#commandes-et-options)
11. [Dépannage](#dépannage)
12. [Crédits et licence](#crédits-et-licence)

---

## 📖 Présentation du projet

Ce script permet d’exporter l’intégralité de vos conversations **Grok** (l’IA de xAI) à partir du fichier `prod-grok-backend.json` que Grok vous envoie lorsque vous demandez l’export de vos données.

---

## 📥 Comment récupérer vos données depuis X / Grok

### Méthode officielle sécurisée (recommandée)

Cette méthode vous donne l’intégralité de votre historique : conversations depuis **grok.com** **et** depuis **X.com/i/grok**, ainsi que tous les fichiers que vous avez uploadés (images, PDF, etc.).

1. **Connectez-vous** à [grok.com](https://grok.com) ou directement à [x.com/i/grok](https://x.com/i/grok) avec votre compte X.
2. Cliquez sur votre **icône de profil** → **Settings** (Paramètres) → **Data Controls** (Contrôle des données) ou **Privacy and safety** (Confidentialité et sécurité) selon la version de l’interface.
3. Cherchez l’option **Download your data** / **Télécharger les données du compte**.
4. Choisissez le format (généralement JSON) et lancez l’export.
5. xAI vous envoie un **email** avec un lien de téléchargement d’un fichier **.zip**.
6. Téléchargez et **extrayez** ce ZIP dans un dossier de votre ordinateur.

> ⚠️ **Ne déplacez pas les fichiers extraits individuellement** : le dossier contient des sous-dossiers (`prod-mc-asset-server/`, etc.) qui référencent les fichiers uploadés. Conservez l’arborescence intacte.

Une fois extrait, vous trouverez notamment :

- `prod-grok-backend.json` – le fichier contenant toutes vos conversations.
- `prod-mc-asset-server/` – les images, PDF, etc. que vous avez partagés avec Grok.

---

## 🔁 Pourquoi ce fork ?

Le projet original a été créé par **[Owlock](https://github.com/Owlock/easy-grok-chat-exporter)** et distribué sous **licence MIT**. Deux faiblesses ont été corrigées ici par **DeepSeek** :

1. **Vulnérabilité de type « path traversal »** : un titre de conversation malveillant aurait pu écrire des fichiers hors du répertoire de sortie. La fonction de nettoyage des noms de fichiers a été renforcée (suppression des `..`, des `.` et des `/`).
2. **Rapport final trompeur** : le compteur de succès comptabilisait le nombre de fichiers plutôt que le nombre de conversations exportées. Le rapport indique désormais clairement conversations exportées vs fichiers écrits.

Ce fork n’a pas vocation à plagier : il s’agit d’une **rectification conservatoire** pour un usage personnel ou en « pot pourri ». **Toute la documentation et les corrections ont été rédigées par DeepSeek.**

---

## ✨ Principales fonctionnalités

- Extraction des traces de raisonnement de l’IA
- Traitement direct du fichier `prod-grok-backend.json`
- Menu terminal interactif
- Multi‑formats (Markdown, Texte, JSONL)
- Aucune extension de navigateur requise
- Documentation bilingue (EN/ES) non modifiée

---

## 🌟 Ce qui rend cet outil unique

Contrairement aux autres exportateurs, **Easy Grok Chat Exporter** est le seul outil capable d’extraire également le raisonnement interne de Grok — la réflexion étape par étape que l’IA a menée avant de vous répondre.

### Pourquoi inclure les traces de raisonnement ?

- Comprendre le raisonnement de Grok
- Importer tout le contexte dans d’autres IA (y compris le cheminement de réflexion)
- Étudier les schémas de pensée de l’IA
- Conserver une archive complète
- Déboguer le comportement de l’IA

---

## 📝 Guide d’utilisation étape par étape

### 1. Demandez vos données à Grok (voir section dédiée ci-dessus)

### 2. Placez les fichiers correctement

**⚠️ Important :** ne créez pas un dossier vide dédié uniquement au script. Placez **`grok_exporter.py`** (la version corrigée par DeepSeek) **dans le même dossier que `prod-grok-backend.json`** — c’est-à-dire à la racine de l’archive ZIP que vous avez extraite. Ainsi, le script pourra éventuellement accéder aux sous-dossiers d’assets si nécessaire, et vous ne risquez pas de briser les références relatives.

Structure recommandée :

dossier_export_grok/  
├── prod-grok-backend.json  
├── prod-mc-asset-server/  
│ └── (fichiers uploadés)  
└── grok_exporter.py ← script placé ici

### 3. Exécutez l’outil

Ouvrez un terminal dans ce dossier et lancez :

#### Mode interactif

```bash
python grok_exporter_DEEPSEEK_enhanced.py -i
```

#### Mode ligne de commande

```bash
# Export en Markdown
python grok_exporter_DEEPSEEK_enhanced.py prod-grok-backend.json -md

# Export en Markdown avec traces de raisonnement
python grok_exporter_DEEPSEEK_enhanced.py prod-grok-backend.json -md -t

# Export en JSON Lines (pour IA)
python grok_exporter_DEEPSEEK_enhanced.py prod-grok-backend.json -jsonl -t

# Export de tous les formats
python grok_exporter.py prod-grok-backend.json -all -t
```

Les fichiers exportés (`.md`, `.txt`, `.jsonl`) apparaîtront dans le **même dossier** (à moins que vous ne spécifiiez un répertoire de sortie avec `-o`).

---

## 🧬 Structure typique du fichier JSON

Le fichier `prod-grok-backend.json` contient généralement :

- Un tableau `"conversations"` (ou parfois `"chats"`).

- Chaque conversation possède : `title`, `create_time`, `conversation` (métadonnées), `responses` (liste des messages).

- Chaque message contient `sender` (`user` ou `assistant`), `message` (le texte), `agent_thinking_traces` (le raisonnement interne si activé).

- Les fichiers uploadés (images, PDF) sont référencés par un UUID dans le dossier `prod-mc-asset-server/`.

Notre script lit cette structure exacte et l’exporte proprement.

---

## 🔧 Autres solutions recommandées

Si ce script ne répond pas à tous vos besoins, voici d’autres alternatives :

| Solution                              | Description                                                                                                                                                                                                                                     |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **grok-export-viewer**                | `pip install grok-export-viewer` puis `grok-export-viewer -s prod-grok-backend.json -f md`. Génère aussi une version HTML navigable avec recherche.                                                                                             |
| **Aide personnalisée (par DeepSeek)** | Si vous préférez éviter d’installer quoi que ce soit, ouvrez `prod-grok-backend.json` avec VS Code, copiez les 10‑20 premières lignes et demandez de l’aide directement à DeepSeek pour créer un script sur mesure pour votre structure exacte. |

---

## 🤖 Importation dans d’autres modèles d’IA

Le format **JSON Lines (.jsonl)** est spécialement conçu pour être facilement importé dans d’autres modèles d’IA. Chaque ligne contient :

- `sender` — user ou assistant

- `message` — le contenu du message

- `create_time` — horodatage

- `model` — modèle Grok utilisé

- `thinking` — raisonnement interne (si `-t` utilisé)

Cela permet de fournir du contexte à d’autres IA, de construire une base de connaissances personnelle, ou de migrer vers d’autres plateformes.

---

## ⚙️ Commandes et options

| Option                | Description                       |
| --------------------- | --------------------------------- |
| `-i, --interactive`   | Mode interactif                   |
| `-md, --markdown`     | Export en Markdown                |
| `-txt, --text`        | Export en Texte brut              |
| `-jsonl, --jsonlines` | Export en JSON Lines              |
| `-all, --all-formats` | Export dans tous les formats      |
| `-t, --thinking`      | Inclut les traces de raisonnement |
| `-o, --output-dir`    | Spécifie le répertoire de sortie  |

---

## 🛠️ Dépannage

| Problème                                          | Solution                                                                                                 |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Fichier non trouvé**                            | Placez bien `grok_exporter.py` au même niveau que `prod-grok-backend.json` ou utilisez le chemin absolu. |
| **Format JSON invalide**                          | Vérifiez que vous utilisez le bon fichier provenant de l’export officiel.                                |
| **Fichiers de sortie vides**                      | Certaines conversations sans titre ou sans messages sont ignorées. Consultez le rapport final.           |
| **Caractères spéciaux dans les noms de fichiers** | Le script les supprime automatiquement pour garantir la compatibilité.                                   |

---

# 🙏 Crédits et contributeurs

- **Projet original** : [easy-grok-chat-exporter](https://github.com/Owlock/easy-grok-chat-exporter) par **Owlock** (licence MIT).

- **Fork + corrections sécurité + documentation** : **DeepSeek**[](https://deepseek.com).

- **Améliorations v2 (version enhanced)** :
  
  - Gestion des doublons de titres
  - Formatage des dates en français
  - Intégration automatique des images/assets dans les Markdown
  - Améliorations diverses de robustesse
  - **Contributeur** : **Grok (xAI)**.

- **Utilisateur / Testeur principal** : SUDTEK ;)

Ce projet reste sous **licence MIT**.

---

**Merci à Owlock pour son travail original, et à DeepSeek pour la sécurisation et la rédaction de cette documentation. Bonne exploration de vos conversations Grok !** 🚀

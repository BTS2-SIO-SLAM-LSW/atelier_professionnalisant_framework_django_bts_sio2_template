# Atelier Django – BTS SIO SLAM 2e année

## Étude de cas : Service Support Informatique "TechFix"

L’entreprise **TechFix** est un prestataire spécialisé dans le **support informatique** auprès de PME de la région.
Elle gère pour ses clients :
- la prise en charge des incidents techniques,
- l’attribution des tickets à un technicien,
- le suivi des interventions,
- la résolution des problèmes,
- l’ajout éventuel de pièces jointes (captures d’écran, logs, documents).

Votre rôle est de **concevoir le Modèle Conceptuel de Données (MCD)** de cette application,
avant la mise en place d’une API Django utilisée dans le reste de l’atelier.

---

## Description fonctionnelle (résumé)

### 1. Clients
- Chaque client correspond à une entreprise cliente.
- On conserve : nom, adresse, email de contact, téléphone.
- Un client peut ouvrir plusieurs incidents, ou aucun.

### 2. Techniciens
- Les techniciens ont : nom, prénom, spécialité (réseau, dev, système, cybersécurité).
- Ils traitent les incidents des clients.

### 3. Incidents
- Un incident est un problème technique ouvert par un client.
- On garde : titre, description, priorité (basse, moyenne, haute, critique), statut (ouvert, en cours, résolu, fermé),
  date de création, date de mise à jour.
- Un incident est toujours lié à un client.
- Un incident peut être **affecté** à un technicien responsable, ou à aucun technicien (au moment de la création).

### 4. Interventions (association plurielle)
- Un incident peut faire l’objet de plusieurs interventions techniques.
- Une intervention est réalisée par un technicien sur un incident à une date donnée, avec un commentaire.
- Plusieurs techniciens peuvent intervenir sur un même incident.
- L’entité **Intervention** est une **association porteuse d’attributs** entre INCIDENT et TECHNICIEN.
- Attention : ce lien est **distinct** du lien d’affectation du technicien responsable.
  Il s’agit donc d’une **association plurielle** entre TECHNICIEN et INCIDENT.

### 5. Pièces jointes
- Une pièce jointe est un fichier lié à un incident (capture d’écran, log, document, etc.).
- On conserve : fichier, date de dépôt, incident concerné.
- Un incident peut avoir 0, 1 ou plusieurs pièces jointes.
- Une pièce jointe appartient à un seul incident.

---

## Travail demandé (partie MCD)

1. Identifier toutes les entités du système et leurs attributs (avec identifiants).
2. Modéliser les associations, y compris :
   - l’affectation d’un technicien responsable à un incident,
   - les interventions (association porteuse d’attributs entre technicien et incident).
3. Déterminer les cardinalités pour chaque association.
4. Représenter le MCD dans un outil comme **Looping**.
5. Exporter le MCD (.loo + capture d’écran ou PDF) et le déposer dans ce dépôt.

Vous expliquerez dans un fichier `REFLEXION.md` :
- pourquoi il existe **deux associations différentes** entre TECHNICIEN et INCIDENT,
- en quoi cela constitue une **association plurielle**,
- comment vous l’avez représentée dans votre MCD.

---

## Mise en route du projet Django (pour la suite de l’atelier)

### Option A – GitHub Codespaces (recommandé)

1. Cliquez sur **"Code" > "Codespaces" > "Create codespace on main"**.
2. Attendez l’ouverture de VS Code dans le navigateur.
3. Le projet est automatiquement configuré (dépendances installées via `requirements.txt`).

### Option B – Local avec VS Code

1. Créez un environnement virtuel dans le dossier du projet :
   ```bash
   python -m venv venv
   ```
2. Activez-le :
   - Windows :
     ```bash
     venv\Scripts\activate
     ```
   - macOS / Linux :
     ```bash
     source venv/bin/activate
     ```
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Appliquez les migrations et lancez le serveur :
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Ouvrez le navigateur à l’adresse :
   `http://127.0.0.1:8000/`

Vous devriez voir :
> Bienvenue dans l'atelier Django BTS SIO 👨‍💻

À partir de ce socle, vous implémenterez progressivement les modèles,
vues, API REST et interfaces nécessaires pour gérer les clients, incidents,
interventions et pièces jointes.

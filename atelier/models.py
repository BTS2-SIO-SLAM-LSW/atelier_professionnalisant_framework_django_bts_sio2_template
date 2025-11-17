from django.db import models


class Client(models.Model):
    nom = models.CharField(max_length=150)
    adresse = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.nom


class Technicien(models.Model):
    RESEAU = "reseau"
    DEV = "dev"
    SYSTEME = "systeme"
    CYBER = "cyber"

    SPECIALITES = [
        (RESEAU, "Réseau"),
        (DEV, "Développement"),
        (SYSTEME, "Système"),
        (CYBER, "Cybersécurité"),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=120, choices=SPECIALES, default=DEV)

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom}"


class Incident(models.Model):
    PRIORITE_BASSE = "basse"
    PRIORITE_MOYENNE = "moyenne"
    PRIORITE_HAUTE = "haute"
    PRIORITE_CRITIQUE = "critique"

    PRIORITES = [
        (PRIORITE_BASSE, "Basse"),
        (PRIORITE_MOYENNE, "Moyenne"),
        (PRIORITE_HAUTE, "Haute"),
        (PRIORITE_CRITIQUE, "Critique"),
    ]

    STATUT_OUVERT = "ouvert"
    STATUT_EN_COURS = "en_cours"
    STATUT_RESOLU = "resolu"
    STATUT_FERME = "ferme"

    STATUTS = [
        (STATUT_OUVERT, "Ouvert"),
        (STATUT_EN_COURS, "En cours"),
        (STATUT_RESOLU, "Résolu"),
        (STATUT_FERME, "Fermé"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    technicien = models.ForeignKey(
        "Technicien",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    titre = models.CharField(max_length=200)
    description = models.TextField()
    priorite = models.CharField(max_length=20, choices=PRIORITES, default=PRIORITE_MOYENNE)
    statut = models.CharField(max_length=20, choices=STATUTS, default=STATUT_OUVERT)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"[{self.statut}] {self.titre}"


class Intervention(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    technicien = models.ForeignKey(Technicien, on_delete=models.PROTECT)
    commentaire = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Intervention #{self.id} sur {self.incident}"


class PieceJointe(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    fichier = models.FileField(upload_to="pieces_jointes/")
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"PJ {self.id} pour {self.incident}"


# Creation d'une exception pour les retraits depassant le solde
class SoldeInsuffisantException(Exception):

    def __init__(self, message):
        super().__init__(message)


# Gestion d'un compte bancaire
class CompteBancaire:

    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    # Ajouter de l'argent au compte
    def deposer(self, montant):
        if montant > 0:
            self.solde += montant

    # Effectuer un retrait
    def retirer(self, montant):
        if montant > self.solde:
            raise SoldeInsuffisantException(
                "Solde insuffisant pour ce retrait."
            )

        self.solde -= montant

    # Montrer les informations du compte
    def afficher(self):
        print(f"Compte: {self.nom}, Solde: {self.solde}€")


# Verification du fonctionnement du compte
try:
    compte = CompteBancaire("Alice", 100)

    compte.afficher()
    compte.retirer(150)

except SoldeInsuffisantException as e:
    print("Erreur:", e)

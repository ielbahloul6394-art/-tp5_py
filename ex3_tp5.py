
import os

# Classe generale pour les erreurs CSV
class CsvException(Exception):
    pass


class FichierIntrouvableException(CsvException):
    pass


class LigneInvalideException(CsvException):
    pass


class PrixNegatifException(CsvException):
    pass


# Fonction pour lire et verifier les articles
def charger_csv(chemin):

    if not os.path.isfile(chemin):
        raise FichierIntrouvableException("Fichier introuvable.")

    articles = []

    with open(chemin, "r", encoding="utf-8") as fichier:

        for numero, ligne in enumerate(fichier, start=1):

            ligne = ligne.strip()

            if not ligne:
                continue

            # Ignorer le titre des colonnes
            if numero == 1 and ligne == "id;nom;prix":
                continue

            colonnes = ligne.split(";")

            if len(colonnes) != 3:
                raise LigneInvalideException(
                    f"Ligne {numero} : nombre de colonnes incorrect."
                )

            identifiant, nom, prix = colonnes

            if not identifiant.strip() or not nom.strip():
                raise LigneInvalideException(
                    f"Ligne {numero} : information manquante."
                )

            try:
                prix = float(prix)
            except ValueError:
                raise LigneInvalideException(
                    f"Ligne {numero} : prix non numerique."
                )

            if prix <= 0:
                raise PrixNegatifException(
                    f"Ligne {numero} : prix invalide."
                )

            articles.append({
                "id": identifiant.strip(),
                "nom": nom.strip(),
                "prix": prix
            })

    return articles


# Programme principal
if __name__ == "__main__":

    try:
        articles = charger_csv("articles.csv")

        print("Liste des articles :")

        for article in articles:
            print(article)

    except FichierIntrouvableException as e:
        print("Erreur :", e)

    except LigneInvalideException as e:
        print("Erreur :", e)

    except PrixNegatifException as e:
        print("Erreur :", e)

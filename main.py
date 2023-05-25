from vehicle import Voiture, Moto, Autobus
from statistics import Statistiques

class GestionnaireVehicules:
    def __init__(self):
        self.vehicules = []

    def ajouter_vehicule(self, vehicule):
        self.vehicules.append(vehicule)

    def supprimer_vehicule(self, vehicule):
        self.vehicules.remove(vehicule)

    def afficher_tous_les_vehicules(self):
        for vehicule in self.vehicules:
            print(vehicule)

    def rechercher_vehicule(self, critere):
        vehicules_trouves = []
        for vehicule in self.vehicules:
            if vehicule.correspond_critere(critere):
                vehicules_trouves.append(vehicule)
        return vehicules_trouves

    def demarrer_application(self):
        while True:
            print("----- Système de Gestion des Véhicules -----")
            print("1. Ajouter un Véhicule")
            print("2. Supprimer un Véhicule")
            print("3. Afficher Tous les Véhicules")
            print("4. Rechercher un Véhicule")
            print("5. Quitter")

            choix = input("Entrez votre choix : ")

            if choix == "1":
                self.menu_ajouter_vehicule()
            elif choix == "2":
                self.menu_supprimer_vehicule()
            elif choix == "3":
                self.afficher_tous_les_vehicules()
            elif choix == "4":
                self.menu_rechercher_vehicule()
            elif choix == "5":
                print("Fermeture de l'application...")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    def menu_ajouter_vehicule(self):
        print("----- Ajouter un Véhicule -----")
        print("1. Voiture")
        print("2. Moto")
        print("3. Autobus")

        choix = input("Entrez le type de véhicule : ")

        if choix == "1":
            self.ajouter_voiture()
        elif choix == "2":
            self.ajouter_moto()
        elif choix == "3":
            self.ajouter_autobus()
        else:
            print("Choix invalide. Veuillez réessayer.")

    def ajouter_voiture(self):
        marque = input("Entrez la marque de la voiture : ")
        modele = input("Entrez le modèle de la voiture : ")
        annee = input("Entrez l'année de la voiture : ")
        couleur = input("Entrez la couleur de la voiture : ")
        energie = input("Entrez l'énergie de la voiture (diesel, essence, électrique) : ")

        voiture = Voiture(marque, modele, annee, couleur, energie)
        self.ajouter_vehicule(voiture)
        print("Voiture ajoutée avec succès.")

    def ajouter_moto(self):
        marque = input("Entrez la marque de la moto : ")
        modele = input("Entrez le modèle de la moto : ")
        annee = input("Entrez l'année de la moto : ")
        couleur = input("Entrez la couleur de la moto : ")
        energie = input("Entrez l'énergie de la moto (diesel, essence, électrique) : ")

        moto = Moto(marque, modele, annee, couleur, energie)
        self.ajouter_vehicule(moto)
        print("Moto ajoutée avec succès.")

    def ajouter_autobus(self):
        marque = input("Entrez la marque de l'autobus : ")
        modele = input("Entrez le modèle de l'autobus : ")
        annee = input("Entrez l'année de l'autobus : ")
        couleur = input("Entrez la couleur de l'autobus : ")
        energie = input("Entrez l'énergie de l'autobus (diesel, essence, électrique) : ")

        autobus = Autobus(marque, modele, annee, couleur, energie)
        self.ajouter_vehicule(autobus)
        print("Autobus ajouté avec succès.")

    def menu_supprimer_vehicule(self):
        if len(self.vehicules) == 0:
            print("Aucun véhicule à supprimer.")
            return

        self.afficher_tous_les_vehicules()

        index = input("Entrez l'index du véhicule à supprimer : ")

        try:
            index = int(index)
            if index < 1 or index > len(self.vehicules):
                print("Index invalide. Veuillez réessayer.")
            else:
                vehicule = self.vehicules[index - 1]
                self.supprimer_vehicule(vehicule)
                print("Véhicule supprimé avec succès.")
        except ValueError:
            print("Index invalide. Veuillez réessayer.")

    def menu_rechercher_vehicule(self):
        if len(self.vehicules) == 0:
            print("Aucun véhicule à rechercher.")
            return

        print("----- Rechercher un Véhicule -----")
        print("1. Par Numéro d'Immatriculation")
        print("2. Par Marque")
        print("3. Par Modèle")
        print("4. Par Année")
        print("5. Par Couleur")

        choix = input("Entrez le critère de recherche : ")

        if choix == "1":
            critere = input("Entrez le numéro d'immatriculation : ")
        elif choix == "2":
            critere = input("Entrez la marque : ")
        elif choix == "3":
            critere = input("Entrez le modèle : ")
        elif choix == "4":
            critere = input("Entrez l'année : ")
        elif choix == "5":
            critere = input("Entrez la couleur : ")
        else:
            print("Choix invalide. Veuillez réessayer.")
            return

        vehicules_trouves = self.rechercher_vehicule(critere)

        if len(vehicules_trouves) == 0:
            print("Aucun véhicule trouvé correspondant au critère.")
        else:
            print("----- Véhicules Trouvés -----")
            for vehicule in vehicules_trouves:
                print(vehicule)


if __name__ == "__main__":
    gestionnaire = GestionnaireVehicules()
    gestionnaire.demarrer_application()

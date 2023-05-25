from vehicle import Vehicule

class Statistiques:
    def __init__(self, vehicules):
        self.vehicules = vehicules

    def obtenir_nombre_vehicules(self):
        return len(self.vehicules)

    def obtenir_statistiques_vehicules(self):
        statistiques = {}

        for vehicule in self.vehicules:
            if vehicule.marque not in statistiques:
                statistiques[vehicule.marque] = 1
            else:
                statistiques[vehicule.marque] += 1

            if vehicule.modele not in statistiques:
                statistiques[vehicule.modele] = 1
            else:
                statistiques[vehicule.modele] += 1

            if vehicule.energie not in statistiques:
                statistiques[vehicule.energie] = 1
            else:
                statistiques[vehicule.energie] += 1

            if vehicule.couleur not in statistiques:
                statistiques[vehicule.couleur] = 1
            else:
                statistiques[vehicule.couleur] += 1

            if vehicule.annee not in statistiques:
                statistiques[vehicule.annee] = 1
            else:
                statistiques[vehicule.annee] += 1

        return statistiques

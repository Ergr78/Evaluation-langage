class Vehicule:
    count = 0

    def __init__(self, marque, modele, annee, couleur, energie):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = couleur
        self.energie = energie
        Vehicule.count += 1

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee}) - {self.couleur}, {self.energie}"

    def correspond_critere(self, critere):
        return (
            critere.lower() == self.marque.lower()
            or critere.lower() == self.modele.lower()
            or critere.lower() == self.annee.lower()
            or critere.lower() == self.couleur.lower()
        )


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, couleur, energie):
        super().__init__(marque, modele, annee, couleur, energie)


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, couleur, energie):
        super().__init__(marque, modele, annee, couleur, energie)


class Autobus(Vehicule):
    def __init__(self, marque, modele, annee, couleur, energie):
        super().__init__(marque, modele, annee, couleur, energie)

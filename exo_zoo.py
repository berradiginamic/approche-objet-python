class Animal:
    def __init__(self, nom, categorie, comportement):
        self._nom = nom
        self._categorie = categorie
        self._comportement = comportement

class Zone:
    def __init__(self, nom):
        self._nom = nom
        self._animaux = []

    def ajouter_animal(self, animal):
        self._animaux.append(animal)

    def get_quantite_nourriture(self):
        raise NotImplementedError("Cette méthode doit être implémentée dans les classes dérivées.")


class SavaneAfricaine(Zone):
    def get_quantite_nourriture(self):
        return len(self._animaux)*100

class FermeAuxReptiles(Zone):
    def get_quantite_nourriture(self):
        return len(self._animaux)*0.1

class Aquarium(Zone):
    def get_quantite_nourriture(self):
        return len(self._animaux)*1

class ZoneCarnivore(Zone):
    def get_quantite_nourriture(self):
        return len(self._animaux)*10

class Voliere(Zone):
    def get_quantite_nourriture(self):
        return len(self._animaux)*0.25


class Zoo:
    def __init__(self, nom):
        self._nom = nom
        self._zones = []

    def ajouter_zone(self, zone):
        self._zones.append(zone)

    def ajouter_animal(self, animal):
        for zone in self._zones:
            if animal._categorie == "Poisson" and isinstance(zone, Aquarium):
                zone.ajouter_animal(animal)
                return
            elif animal._categorie == "Carnivore" and isinstance(zone, ZoneCarnivore):
                zone.ajouter_animal(animal)
                return
            elif animal._categorie == "Oiseau" and isinstance(zone, Voliere):
                zone.ajouter_animal(animal)
                return
            elif animal._categorie == "Reptile" and isinstance(zone, FermeAuxReptiles):
                zone.ajouter_animal(animal)
                return

    def get_quantite_nourriture(self):
        total_nourriture = 0
        for zone in self._zones:
            total_nourriture += zone.get_quantite_nourriture()
        return total_nourriture

    def afficher_infos(self):
        for zone in self._zones:
            print(f"Zone: {zone._nom}")
            for animal in zone._animaux:
                print(f"{animal._nom} ({animal._categorie}, {animal._comportement}")


zoo = Zoo("Zoo1")

savane = SavaneAfricaine("Savane Africaine")
ferme_reptiles = FermeAuxReptiles("Ferme aux Reptiles")
aquarium = Aquarium("Aquarium")
carnivore_zone = ZoneCarnivore("Zone Carnivore")
voliere = Voliere("Volière")

zoo.ajouter_zone(savane)
zoo.ajouter_zone(ferme_reptiles)
zoo.ajouter_zone(aquarium)
zoo.ajouter_zone(carnivore_zone)
zoo.ajouter_zone(voliere)

lion = Animal("Lion", "Carnivore", "Chasseur")
girafe = Animal("Girafe", "Herbivore", "Mangeur de feuilles")
poisson = Animal("Poisson", "Poisson", "Nageur")
serpent = Animal("Serpent", "Reptile", "Serpenteur")
perroquet = Animal("Perroquet", "Oiseau", "Voleur")

zoo.ajouter_animal(lion)
zoo.ajouter_animal(girafe)
zoo.ajouter_animal(poisson)
zoo.ajouter_animal(serpent)
zoo.ajouter_animal(perroquet)

# Affichage des informations du zoo
print(f"Quantité totale de nourriture à acheter : {zoo.get_quantite_nourriture()} kg")
zoo.afficher_infos()




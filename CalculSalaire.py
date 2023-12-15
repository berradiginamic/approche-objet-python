from abc import abstractmethod


class Intervenant:
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

    @abstractmethod
    def get_salaire(self):
        pass


class Salarie(Intervenant):
    def __init__(self, nom, prenom, salaire_mensuel):
        super().__init__(nom, prenom)
        self._salaire_mensuel = salaire_mensuel

    def get_salaire(self):
        return self._salaire_mensuel

    def afficher_donnees(self):
        print(f"Nom: {self._nom}, Prenom: {self._prenom}, Salaire mensuel: {self.get_salaire()}, Statut: Salarié")


class Pigiste(Intervenant):
    def __init__(self, nom, prenom, jours_travailles, montant_journalier):
        super().__init__(nom, prenom)
        self._jours_travailles = jours_travailles
        self._montant_journalier = montant_journalier

    def get_salaire(self):
        return self._jours_travailles * self._montant_journalier


    def afficher_donnees(self):
        print(f"Nom: {self._nom}, Prenom: {self._prenom}, Salaire mensuel: {self.get_salaire()}, Statut: Pigiste")


salarie = Salarie("Berrabah", "Fatima", 3000)
pigiste = Pigiste("Benmira", "Maria", 10, 150)

salarie.afficher_donnees()
pigiste.afficher_donnees()

class Theatre:
    def __init__(self, nom, capacite_max):
        self._nom = nom
        self._capacite_max = capacite_max
        self._total_clients_inscrit = 0
        self._recette_totale = 0

    def inscrire(self, nbre_clients, prix_place):
        if self._total_clients_inscrit + nbre_clients <= self._capacite_max:
            self._total_clients_inscrit += nbre_clients
            recette = nbre_clients*prix_place
            self._recette_totale += recette
            print(f"inscription réussie pour {nbre_clients} clients, et la recette est {recette} €")
        else:
            print("Erreur!! Impossible d'inscrire")

theatre1 = Theatre("Théatre de Châtelet", 2036)
theatre1.inscrire(2000, 30)
print(f"total des clients inscrits est: {theatre1._total_clients_inscrit}")
print(f"recette totale est: {theatre1._recette_totale} € ")


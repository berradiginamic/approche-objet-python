from datetime import datetime


class Etudiant:
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

class Discipline:
    def __init__(self, nom):
        self._nom = nom
        self._notes = []

    def ajouter_note(self, valeur, date, categorie):
        note = Note(valeur, date, categorie)
        self._notes.append(note)


class Note:
    def __init__(self, valeur, date, categorie):
        self._valeur = valeur
        self._date = date
        self._categorie = categorie


class Bulletin(Etudiant):
    def __init__(self, etudiant):
        super().__init__(etudiant._nom, etudiant._prenom)
        self._etudiant = etudiant
        self._disciplines = []

    def ajouter_discipline(self, discipline):
        self._disciplines.append(discipline)

    def ajouter_note(self, discipline, valeur, date, categorie):
        note = Note(valeur, date, categorie)
        for d in self.disciplines:
           if d.nom == discipline:
               d._notes.append(note)



    def calculer_moyenne(self):
        moyenne = {}
        for discipline in self._disciplines:
            moyenne[discipline._nom] = sum(note._valeur for note in discipline._notes)/len(discipline._notes)
        return moyenne

    def afficher_moyenne(self):
        moyenne = self.calculer_moyenne()
        if not moyenne:
            print("pas de discipline avec des notes")
            return
        print(f"moyenne de l'etudiant {self._etudiant._nom} {self._etudiant._prenom}")
        for discipline, moy in moyenne.items():
            print(f"{discipline}: {moy}")

etudiant = Etudiant("Benmira", "Ishak")
bulletin = Bulletin(etudiant)

math = Discipline("Mathématiques")
math.ajouter_note(18, datetime(2023, 12, 14), "devoir")
math.ajouter_note(17, datetime(2023, 12, 2), "Interrogation")
math.ajouter_note(18, datetime(2023, 12, 20), "examen")
bulletin.ajouter_discipline(math)
print(f"la moyenne de l'etudiant en mathématiques ")

physique = Discipline("Physique")
physique.ajouter_note(15, datetime(2023, 11, 30), "devoir")
physique.ajouter_note(15, datetime(2023, 12, 4), "Interrogation")
physique.ajouter_note(15, datetime(2023, 12, 15), "examen")
bulletin.ajouter_discipline(physique)

chimie = Discipline("Chimie")
chimie.ajouter_note(16, datetime(2023, 11, 29), "devoir")
chimie.ajouter_note(15, datetime(2023, 12, 5), "Interrogation")
chimie.ajouter_note(15, datetime(2023, 12, 14), "examen")
bulletin.ajouter_discipline(chimie)

anglais = Discipline("Anglais")
anglais.ajouter_note(13.5, datetime(2023, 11, 29), "devoir")
anglais.ajouter_note(12.25, datetime(2023, 12, 5), "Interrogation")
anglais.ajouter_note(14, datetime(2023, 12, 14), "examen")
bulletin.ajouter_discipline(anglais)

français = Discipline("Français")
français.ajouter_note(15, datetime(2023, 11, 29), "devoir")
français.ajouter_note(14, datetime(2023, 12, 5), "Interrogation")
français.ajouter_note(15.5, datetime(2023, 12, 14), "examen")
bulletin.ajouter_discipline(français)

espagnol = Discipline("Espagnol")
espagnol.ajouter_note(11, datetime(2023, 11, 29), "devoir")
espagnol.ajouter_note(14, datetime(2023, 12, 6), "Interrogation")
espagnol.ajouter_note(12, datetime(2023, 12, 14), "examen")
bulletin.ajouter_discipline(espagnol)

sport = Discipline("sport")
sport.ajouter_note(17, datetime(2023, 12, 14), "examen")
bulletin.ajouter_discipline(sport)

bulletin.afficher_moyenne()




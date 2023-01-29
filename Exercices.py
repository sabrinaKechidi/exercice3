'''
###exercice  5
montant_restant=200
monnaie=0

while True :
 print("montant restant :", montant_restant)
 prix = int (input("prix de l'article:"))
 somme= int (input("montant fourni:"))
 monnaie= somme - prix
 if monnaie >  montant_restant:
    print("Je ,n'ai pas assez de monnaie!")
 else:
    billet5 = monnaie //5
    pieces = monnaie %5
    print("je vous rends la monnaie: ", monnaie," euros")
    print(billet5," de 5 euros et ", pieces," de 1 euro")
    montant_restant= montant_restant - monnaie
'''



'''
###exercice 6
from random import randint
Binf = int(input("saisir la borne inf :"))
Bsup = int(input("saisir la borne sup :"))
rand = randint(Binf, Bsup)
print(rand)
nbTentatives = 0
while nbTentatives >= 0:
    nbTentatives = nbTentatives + 1
    nb = int(input("saisir le nombre : "))
    if rand < nb: else:
        break
      print("Plus grand!")
    elif rand > nb:
      print("plus petit ")
    else:
        break
if nbTentatives != 0 :
    print("Gangné en ", nbTentatives ,"coups")
'''

'''
###exercice 7
from random import randint
nbr_atrouver = int (input(" le nombre à trouver est : "))
b_inf= 1
b_sup = 1000
while True:
 rand = randint (b_inf, b_sup)
 print (rand)
 if rand > nbr_atrouver:
   b_sup = rand

 elif rand < nbr_atrouver:
   b_inf = rand
 elif rand == nbr_atrouver:
     break
print( "le nbr à trouver =" ,rand)
'''
notes = {"AlgoProg": 10.20, "Algorithmique": 12.33, "AlgèbreBase": 13.75, "Anglais": 9, \
         "PPP": 17.5, "Méthodo": 8, "PIX": 16.87, "OIL": 18, "InfoBase": 14.50}

ued1 = ("Algèbre de base", ["AlgèbreBase"])
ued2 = ("Informatique de base", ["InfoBase"])
ued3 = ("Algorithmique et Programmation 1", ["AlgoProg"])
uet = ("Anglais et MTU 1", ["Anglais", "PPP", "Méthodo", "PIX", "OIL"])
uep = ("Personnalisée", ["Algorithmique", "AnalyseBase", "Physique"])

ueds = [ued1, ued2, ued3]
ues = ueds + [uet, uep]


def calcul_note_ue(ue, notes):
    nb_notes = 0
    total_notes = 0
    for matiere in ue[1]:
        if matiere in notes and notes[matiere] is not None:
            nb_notes += 1
            total_notes += notes[matiere]
    if nb_notes > 0:
        note_ue = total_notes / nb_notes
        print("Note pour l'UE", ue[0], ":", note_ue)
    else:
        note_ue = None
    return note_ue


def validation_bloc(nom, liste_ue, notes):
    nb_ue = 0
    total_ue = 0
    for ue in liste_ue:
        note_ue = calcul_note_ue(ue, notes)
        if note_ue is not None:
            nb_ue += 1
            total_ue += note_ue
    if nb_ue is not None:
        moyenne = total_ue / nb_ue
        print("Moyenne sur", nom, ":", moyenne)
        if moyenne >= 10:
            validation = True
        else:
            validation = False
    else:
        validation = None
    return validation


def valider_semestre(notes, ueds, ues):
    validation1 = validation_bloc("les UE disciplinaires", ueds, notes)
    if validation1 is None:
        print("Validation non définie")
    else:
        if not validation1:
            print("Semestre non validé")
        else:
            validation2 = validation_bloc("l'ensemble des UE", ues, notes)
            if validation2 is None:
                print("Validation non définie")
            else:
                if validation2:
                    print("Semestre validé")
                else:
                    print("Semestre non validé")


if __name__ == "__main__":
    valider_semestre(notes, ueds, ues)

    

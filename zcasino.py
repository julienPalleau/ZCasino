from random import randrange
from math import ceil
credit = 100
reponse = 'O'


def debug(*param):
    result = ""
    for i in param:
        result += " " + str(i)
    return print(result)


def tirageRoulette():
    return randrange(50)


print("Bonjour et bienvenu au casino !")
print("vous aves 100$ sur votre compte afin de les jouer à la roulette")
miseJoueur = int(input("combien desirez vous miser ?"))


while (reponse.upper() != "N" and reponse.upper() == "O" and miseJoueur < credit):
    # tirage du numero aleatoir à la roulette
    roulette = tirageRoulette()

    # On determine la couleur du numero issu de la roulette
    if (roulette % 2):
        rouletteCouleur = "rouge"
    else:
        rouletteCouleur = "noir"

    # Pari du joueur
    pari = input("Pariez sur un numero compris entre 0 et 49 : ")
    try:
        pari = int(pari)
        assert 0 < pari < 50
    except ValueError:
        print("vous n'avez pas saisi un nombre entier !")
    except AssertionError:
        print("Le Pari doit etre strictement superieur à 0 et strictement inferieur à 50")
    else:
        if pari % 2:
            pariCouleur = "rouge"
        else:
            pariCouleur = "noir"

        print("vous avez parie sur le: {0} {1}".format(pari, pariCouleur))
        print("Attention rien ne va plus\n")

        print("Le numero sortant est le: {0} {1} Vous aviez joue le: {2} {3}".format(
            roulette, rouletteCouleur, pari, pariCouleur))

        if (roulette == pari):
            print("Bravo, vous avez gagne 3 fois votre mise !")
            credit += int(3 * miseJoueur)
            print("Vous possedez maintenant {0} dollars".format(credit))

        elif (pariCouleur == rouletteCouleur):
            print("Bravo, vous avez gagne 0.5 fois votre mise, soit",
                  int(0.5 * miseJoueur), "dollars")
            credit += ceil(0.5 * miseJoueur)
            print("Vous possedez maintenant {0} dollars".format(credit))
        else:
            debug(miseJoueur, credit)
            print("vous avez perdu votre mise! {0} dollars".format(miseJoueur))
            credit -= int(miseJoueur)
            print("Vous possedez maintenant {0} dollars".format(credit))

            if miseJoueur >= credit:
                print(
                    "Vous ne possedez plus assez d'argent pour faire un nouveau pari !")
                break

        reponse = input("desirez-vous re-jouer O/N?\n")

print("Au revoir, en esperant vous revoir bientot au Casino !")

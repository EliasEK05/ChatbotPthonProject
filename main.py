from function import *
import time

print("Bienvenue dans menu du chatbot.\nDans ce menu, vous pouvez accéder à différentes focntionnalités")
time.sleep(2)
while True:
    print("Voici les différentes fonctionnalités disponible")
    time.sleep(1)
    print("1. Consulter la liste des mots les moins importants dans le corpus des disours")
    print("2. Consulter le(s) mot(s) ayant le score TD-IDF le plus élevé")
    print("3. Consulter le(s) mot(s) le(s) plus répété(s) par le président Chirac")
    print("4. Consulter le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois")
    print("5. Conulster le premier président à parler du climat et/ou de l’écologie")
    print('6. Consulter le(s) mot(s) que tous les présidents ont évoqués en dehors des mots "non importants" ')
    time.sleep(1)
    user = int(input("Afin d'accéder a la focntionnalité souhaitée, veuillez taper dans la console le numéro de la fonctionnalité "))
    if user == 1:
        print("Les mots pas important sont : ", end = "")
        time.sleep(2)
        print("Veillez attendre un instant svp...")

        liste = fonctionnalite_1()
        for mot in liste:
            print(mot, end = ", ")

    if user == 2:
        #print("le(s) mot(s) ayant le score TD-IDF le plus élevé sont : ")
        print("Cette fonctionnalité n'est malheureusement pas encore dispoible. Veuillez nous en excuser")

    if user == 3:
        "Veillez attends un instant svp"
        liste = fonctionnalite_3()
        print("Le mot le plus répété dans les discours du président Chirac est le mot {} qui a été répété {} fois.".format(liste[0][0], liste[1]))


    if user == 4:
        liste = fonctionnalite_4()
        print("Les président ayant parler de la Nation sont :", end= "")
        for president in liste[0]:
            print(president, end=", ")
        print("\n Le président ayant répété le plus de fois nation est {} qui l'a répété {} fois.".format(liste[1], liste[2]))

    if user == 5:
        print("le premier président ayant parler du climat et/ou de l’écologie est :", fonctionnalite_5())

    if user == 6:
        print("Cette fonctionnalité n'est malheureusement pas encore dispoible. Veuillez nous en excuser")

    time.sleep(5)

from function import *
import time

print("Bienvenue dans menu du chatbot.\nDans ce menu, vous pouvez poser une question ou accéder aux différentes fonctionnalités.")
time.sleep(2)
while True:
    fonction = int(input("Ecrivez 1 si vous voulez poser une question. Ou écrivez 2 si vous voulez accéder aux fonctionnalités."))
    if fonction == 1:
        question = input("Quel est votre question?")
        if mot_corpus_question(question_(question)) == []:
            print("Désolé, je n'ai pas compris votre question.")
        elif question.split()[0] not in ["Pourquoi", "Comment", "Peux-tu"]:
            print(reponse(score_idf(vecteur_question(question)), doc_pertinent(matrice_transposed(tfidf("cleaned")), vecteur_question(question), list_of_files("speeches", 'txt'))))
        else:
            affiner_reponse(question, reponse(score_idf(vecteur_question(question)), doc_pertinent(matrice_transposed(tfidf("cleaned")), vecteur_question(question), list_of_files("speeches", 'txt'))))

    elif fonction == 2:
        print("Voici les différentes fonctionnalités disponible")
        time.sleep(1)
        print("1. Consulter la liste des mots les moins importants dans le corpus des disours")
        print("2. Consulter le(s) mot(s) ayant le score TD-IDF le plus élevé")
        print("3. Consulter le(s) mot(s) le(s) plus répété(s) par le président Chirac")
        print("4. Consulter le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois")
        print("5. Conulster le premier président à parler du climat et/ou de l’écologie")
        print('6. Consulter le(s) mot(s) que tous les présidents ont évoqués en dehors des mots "non importants" ')
        user = int(input("Afin d'accéder a la focntionnalité souhaitée, veuillez tapper dans la console le numéro de la fonctionnalité "))
        if user == 1:
            print("Les mots pas important sont : ", end="")
            liste = fonctionnalite_1()
            for mot in liste:
                print(mot, end=", ")

        elif user == 2:
            print("Le(s) mot(s) ayant le score TD-IDF le plus élevé est : ", fonctionnalite_2()[0])


        elif user == 3:
            liste = fonctionnalite_3()
            print('Le mot le plus répété dans les discours du président Chirac est le mot "{}" qui a été répété {} fois.'.format(liste[0][0], liste[1]))


        elif user == 4:
            liste = fonctionnalite_4()
            print("Les président ayant parler de la Nation sont :", end= ", ")
            for president in liste[0]:
                print(president, end=" ")
            print()
            print('Le président ayant répété le plus de fois "nation" est {} qui l a répété {} fois.'.format(liste[1], liste[2]))

        elif user == 5:
            print("Le premier président ayant parler du climat et/ou de l’écologie est :", fonctionnalite_5())

        elif user == 6:
            print("Les mots que tous les présidents ont évoqués en dehots des mots pas importants sont : ", end = "")
            for mot in fonctionnalite_6():
                print(mot, end= ", ")
        else:
            print("Désolé, je n'ai pas compris. Veillez recommencer")

    else:
        print("Je n'ai pas compris. Veillez recommencer")

    print()
    time.sleep(5)



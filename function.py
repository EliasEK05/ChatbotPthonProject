import os
from random import *
from math import *


# fonction permetant de faire une liste des nom nom des fichier dans le dossier speeches ( fonction donné dans l'éononcé du projet
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


# Fonction pour extraire les noms des présidents à partir des noms des fichiers texte fournis
def extraction_nom():
    list_nom_fichier = list_of_files("speeches", "txt")
    list_nom_president = []
    for nom in list_nom_fichier:
        nom = nom[11:-4]
        if nom[-1] in "123456789":
            nom = nom[:-1]
        list_nom_president.append(nom)
    return list_nom_president


# Associer à chaque président un prénom (add dans le dico info president)
def prenom_president():
    list_nom_president = extraction_nom()
    dico_noms = {}
    for nom in list_nom_president:
        if nom == "Chirac":
            dico_noms[nom] = "Jacques"
        elif nom == "Giscard dEstaing":
            dico_noms[nom] = "Valery"
        elif nom == "Hollande" or nom == "Mitterrand":
            dico_noms[nom] = "François"
        elif nom == "Sarkozy":
            dico_noms[nom] = "Nicolas"
    return dico_noms


# Afficher la liste des noms des présidents (attention aux doublons)
def list_president():
    list_nom_president = extraction_nom()
    list_nom_president_clean = []
    for nom in list_nom_president:
        if nom not in list_nom_president_clean:
            list_nom_president_clean.append(nom)
    return list_nom_president_clean


'''Convertir  les textes des 8 fichiers en minuscules et stocker les contenus dans de nouveaux fichiers. Les
nouveaux fichiers doivent être stockés dans un nouveau dossier appelé « cleaned ». Ce dossier doit se
situer dans le répertoire principal où se trouve le programme main.py et au même niveau que le répertoire
« speeches »'''


def nettoyage_fichier():
    list_nom_fichier_speeches = list_of_files("speeches", "txt")
    chemin_dossier_cleaned = r"C:\Users\elias\PycharmProjects\pythonProject\cleaned"  # le r permet à ce que la chaine de caractère soit interpreter correctement et qu'il n'y ai pas d'erreur d'interprétation
    chemin_dossier_speeches = r"C:\Users\elias\PycharmProjects\pythonProject\speeches"
    for i in list_nom_fichier_speeches:
        nom_fichier_clean = i[:-4] + "_clean" + ".txt"
        chemin_fichier = os.path.join(chemin_dossier_cleaned, nom_fichier_clean)
        nom_fichier_discours = os.path.join(chemin_dossier_speeches, i)
        with open(nom_fichier_discours, "r", encoding='utf-8') as a, open(chemin_fichier, "w", encoding='utf-8') as b:
            texte = a.read()
            for car in texte:
                b.write(minuscule(car))


# Fonction permettant de mettre une lettre en minuscule, utilisé pour la fonction nettoyage_fichier
def minuscule(lettre):
    if ord(lettre) >= 65 and ord(lettre) <= 90:
        lettre = chr(ord(lettre) + 32)
    return lettre


'''Pour chaque fichier stocké dans le répertoire « cleaned », parcourir son texte et supprimer tout caractère
de ponctuation. Le résultat final doit donner un fichier avec des mots séparés par des espaces. Attention,
certains caractères comme l’apostrophe (‘) ou le tiret (-) nécessitent un traitement spécial pour ne pas
causer une concaténation de deux mots (exemple : « elle-même » devrait devenir « elle même » et non
pas « ellemême »). Les modifications réalisées à cette étape devraient être stockées dans les mêmes
fichiers du répertoire « cleaned ».'''


def suppresion_ponctuation():
    liste_nom_fichier_cleaned = list_of_files("cleaned", "txt")
    chemin_dossier_cleaned = r"C:\Users\elias\PycharmProjects\pythonProject\cleaned"
    i = 0
    for i in liste_nom_fichier_cleaned:
        chemin_fichier = os.path.join(chemin_dossier_cleaned, i)
        with open(chemin_fichier, 'r', encoding='utf-8') as F1:
            texte = F1.read()

        with open(chemin_fichier, 'w', encoding='utf-8') as F2:
            for car in texte:
                if car in ['.', ',', '"', '!', '?', ';', ':']:
                    car = ''
                elif car in ["-", "'"]:
                    car = ' '
                F2.write(car)


# fonction permettant de return la liste des texte des fichiers cleaned
def liste_texte():
    liste = list_of_files("cleaned", "txt")
    liste_texte = []
    for fichier in liste:
        with open("cleaned//" + fichier, 'r', encoding='utf-8') as F:
            texte = F.read()
            liste_texte.append(texte)
    return liste_texte


# foncion permettant de return la liste des fichiers cleaned en combinant les deux discours de Chirac et les deux discours de Miterrand
def liste_texte_president():
    liste = liste_texte()
    txt_chirac = liste[0] + liste[1]
    txt_mitterand = liste[5] + liste[6]
    liste[0] = txt_chirac
    liste.pop(1)
    liste[4] = txt_mitterand
    liste.pop(5)
    return liste


# Écrire une fonction qui prend en paramètre une chaine de caractères et qui retourne un dictionnaire
# associant à chaque mot le nombre de fois qu’il apparait dans la chaine de caractères.

def TF(chaine):
    dico = {}
    mots = chaine.split()
    for mot in mots:
        if mot in dico:
            dico[mot] += 1
        else:
            dico[mot] = 1
    return dico


# Écrire une fonction qui prend en paramètre le répertoire où se trouve l’ensemble des fichiers du corpus
# et qui retourne un dictionnaire associant à chaque mot son score IDF.

def IDF(directory):
    liste_mots_par_fichier = []
    dico_score_idf = {}
    nb_documents_total = 0
    for fichier in os.listdir(directory):
        nb_documents_total += 1
        liste_mot = []
        with open("cleaned//" + fichier, 'r', encoding='utf-8') as F:
            for ligne in F:
                mots = ligne.split()
                for mot in mots:
                    if mot not in liste_mot:
                        liste_mot.append(mot)
        liste_mots_par_fichier.append(liste_mot)
    for liste in liste_mots_par_fichier:
        for mot in liste:
            if mot in dico_score_idf:
                dico_score_idf[mot] += 1
            else:
                dico_score_idf[mot] = 1
    for mot in dico_score_idf:
        dico_score_idf[mot] = log(nb_documents_total / dico_score_idf[mot])
    return dico_score_idf

def IDF_10(directory):
    liste_mots_par_fichier = []
    dico_score_idf = {}
    nb_documents_total = 0
    for fichier in os.listdir(directory):
        nb_documents_total += 1
        liste_mot = []
        with open("cleaned//" + fichier, 'r', encoding='utf-8') as F:
            for ligne in F:
                mots = ligne.split()
                for mot in mots:
                    if mot not in liste_mot:
                        liste_mot.append(mot)
        liste_mots_par_fichier.append(liste_mot)
    for liste in liste_mots_par_fichier:
        for mot in liste:
            if mot in dico_score_idf:
                dico_score_idf[mot] += 1
            else:
                dico_score_idf[mot] = 1
    for mot in dico_score_idf:
        dico_score_idf[mot] = log((nb_documents_total / dico_score_idf[mot]), 10)
    return dico_score_idf


# Écrire une fonction qui prend en paramètre le répertoire où se trouvent les fichiers à analyser et qui
# retourne au minimum la matrice TF-IDF.

def tfidf(directory="cleaned"):
    liste_des_mots = IDF_10(directory)
    matrice_tf_idf = []
    id = 0
    liste_txt = liste_texte()
    liste_tf = []
    for txt in liste_txt:
        liste_tf.append(TF(txt))

    for mot in liste_des_mots:
        L = []
        for tf in liste_tf:
            if mot in tf.keys():
                #matrice_tf_idf[id].append(round((dico_mot_fichier[mot] * liste_des_mots[mot]), 2))
                L.append((tf[mot] * liste_des_mots[mot]))
            else:
                L.append(0.0)
        matrice_tf_idf.append(L)
        id += 1
    return matrice_tf_idf


# Fonctionnalités à développer

# Fonctionnalité 1 : Afficher la liste des mots les moins importants dans le corpus de documents. Un mot est dit non important, si son TD-IDF = 0 dans tous les fichiers.

def fonctionnalite_1():
    matrice_TF_IDF = tfidf("cleaned")
    liste_mot_pas_important = []
    i = 0
    liste_mot = list(IDF("cleaned").keys())
    for ligne in matrice_TF_IDF:
        somme = 0
        for colonne in ligne:
            somme += colonne
        if somme == 0:
            liste_mot_pas_important.append(liste_mot[i])
        i += 1
    return liste_mot_pas_important


# Fonctionnalité 2 : Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé

def fonctionnalite_2():
    liste_mot_important = []
    matrice_tfidf = tfidf("cleaned")
    somme_max = 0
    liste_mot = list(IDF("cleaned").keys())

    for ligne in matrice_tfidf:
        somme = 0
        for colonne in ligne:
            somme += colonne
        if somme > somme_max:
            somme_max = somme

    cpt = 0
    for ligne in matrice_tfidf:
        somme = 0
        for colonne in ligne:
            somme += colonne
        if somme_max == somme:
            liste_mot_important.append(liste_mot[cpt])
        cpt += 1

    return liste_mot_important


# fonctionnalité 3: Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac

def fonctionnalite_3():
    liste_texte = liste_texte_president()
    txt_chirac = liste_texte[0]
    tf_chirac = TF(txt_chirac)
    max = 0
    for mot in tf_chirac:
        if tf_chirac[mot] > max:
            max = tf_chirac[mot]
    mot_plus_repetes = []
    for mot in tf_chirac:
        if tf_chirac[mot] == max:
            mot_plus_repetes.append(mot)
    return mot_plus_repetes, max


# fonctionnalité 4: Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois

def fonctionnalite_4():
    liste_texte = liste_texte_president()
    liste_repetition_nation = []
    president_nation = []
    nom_president = list_president()
    i = 0
    for texte in liste_texte:
        tf_texte = TF(texte)
        for mot in tf_texte:
            if mot == "nation":
                president_nation.append(nom_president[i])
                liste_repetition_nation.append(tf_texte[mot])
        i += 1
    repetition_max = 0
    indice = 0
    for nb in liste_repetition_nation:
        if nb > repetition_max:
            repetition_max = nb
            indice_president = indice
        indice += 1

    return president_nation, president_nation[indice_president], repetition_max


# fonctionnalité 5: Indiquer le premier président à parler du climat et/ou de l’écologie

def fonctionnalite_5():
    liste_texte = liste_texte_president()
    nom_president = list_president()
    i = 0
    president_climat = ""
    verif = False
    while verif == False and i < len(liste_texte):
        txt = liste_texte[i]
        tf_mot = TF(txt)
        for mot in tf_mot:
            if 'climat' in mot or 'écologie' in mot:
                president_climat = nom_president[i]
                verif = True
        i += 1
    return president_climat


# fonctionalité 6 : Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués.
def fonctionnalite_6():
    liste_texte = liste_texte_president()
    liste_mots = []
    i = 0
    dico_mot = {}
    for txt in liste_texte:
        TF_txt = TF(txt)
        for mot in TF_txt:
            if i == 0:
                dico_mot[mot] = 1
            else:
                if mot in dico_mot:
                    dico_mot[mot] += 1
        i += 1
    for mot in dico_mot:
        if dico_mot[mot] == 6:
            liste_mots.append(mot)
    liste_mots_pas_important = fonctionnalite_1()
    for mot in liste_mots:
        if mot in liste_mots_pas_important:
            liste_mots.remove(mot)
    return liste_mots


# ---------------------Partie 2-----------------------------

#1. Tokenisation de la Question :

def question(txt_question):
    txt_clean = ""
    for car in txt_question:
        if car in ['.', ',', '"', '!', '?', ';', ':']:
            car = ''
        elif car in ["-", "'"]:
            car = ' '
        else:
            car = minuscule(car)
        txt_clean += car
    return txt_clean.split()

# 2. Recherche des mots de la question dans le Corpus :


def mot_corpus_question(list_mot_question):
    liste_mot_corpus = list(IDF("cleaned").keys())
    intersection = []
    for mot in list_mot_question:
        if mot in liste_mot_corpus:
            intersection.append(mot)
    return intersection


# 3. Calcul du vecteur TF-IDF pour les termes de la question :
def vecteur_question(question):
    chaine = ""
    for car in question:                                        #enlever les caractères spéciaux
        if car in ['.', ',', '"', '!', '?', ';', ':']:
            car = ''
        elif car in ["-", "'"]:
            car = ' '
        chaine += car
    liste_mot = chaine.split()         #liste mot

    dico_tf = {}
    for i in liste_mot:
        if i in dico_tf:
            dico_tf[i] += 1
        else:
            dico_tf[i] = 1
    for mot in dico_tf:
        dico_tf[mot] #/= len(liste_mot)
    dico_idf = IDF("cleaned")

    vecteur_question = []
    for mot in dico_idf:
        if mot in dico_tf:
            vecteur_question.append(dico_idf[mot] * dico_tf[mot])
        else:
            vecteur_question.append(0.0)

    return vecteur_question

def matrice_transposed(matrice):
    new_matrice = []
    for i in range(len(matrice[0])):
        L = []
        for j in range(len(matrice)):
            L.append(matrice[j][i])
        new_matrice.append(L)
    return new_matrice

def produit_scalaire(a, b):
    produit_scalaire = 0
    for i in range(len(a)):
        produit_scalaire += a[i] + b[i]
    return produit_scalaire

def norme_vecteur(a) :
    somme = 0
    for val in a :
        somme += val**2
    return sqrt(somme)

def similarité(a, b):
    return (produit_scalaire(a, b)/(norme_vecteur(a) * norme_vecteur(b)))

def doc_pertinent(matrice, vecteur_question , liste_nom):
    max_sim = 0
    max_id = 0
    i = 0
    liste_mot = list(IDF("cleaned").keys())

    for vecteur in matrice:

        if similarité(vecteur_question, vecteur) > max_sim :
            max_sim = similarité(vecteur_question, vecteur)
            max_id = i
        i += 1

    return liste_nom[max_id]

def score_idf(vecteur_question):
    val_max = 0
    cpt = 0
    id = 0
    liste_mot = list(IDF("cleaned").keys())
    idf = IDF("cleaned")
    for val in vecteur_question:
        if val > val_max:
            val_max = val
            id = cpt
        cpt += 1
    return liste_mot[id]


def reponse(mot, texte):
    with open("speeches/" + texte, 'r', encoding= 'utf-8') as F:
        texte = F.read()
    texte = texte.split('.')
    for phrase in texte:
        if mot in phrase:
            return phrase + "."




    



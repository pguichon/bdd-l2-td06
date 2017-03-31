# -*- coding: Utf-8 -*-
import sqlite3
conn = sqlite3.connect('td.db')

cursor = conn.cursor()


def init():
    while True:
        print("q pour quiter")
        print("1 pour selectionner les individus")
        print("2 pour selectionner les individus et leurs adresses associées")
        saisi = raw_input('Que voulez vous faire : ')
        if saisi == "q":
            print("Bye")
            conn.close()
            break
        elif saisi == "1":
            afficher_individu()
        elif sassi == "2":
            afficher_individu_adresses()
        else:
            print("vous avez fait une mauvaise saisi")


def selectionner_individu():
    cursor.execute("SELECT nom, prenom FROM individu")
    for individu in cursor:
        print("nom: {} prenom: {}".format(individu[0], individu[1]))

def afficher_individu_adresses():
    print("à implementer")

def rechercher_un_individu(email):
    print("à implementer")
    individu = {}
    return individu

def saisir_une_adresse(individu):
    print("à implementer")
init()

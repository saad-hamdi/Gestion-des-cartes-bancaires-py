#les fonctions
import random
def ajouter_client():
    while True:
        if liste_comptes:
            liste_compte=liste_comptes.copy()
            liste_comptes.clear()
        else:
            #le dictionnaire compte
            n=random.randint(0,9)
            a=random.randint(0,100)
            nombre=int(str(n)+str(a))
            while True:
                s=float(input("entrer le solde : "))
                if s>=0:
                    break
                else:
                    print("le solde ne peut pas negative")
            solde=s
            compte={"nombre":nombre,"solde":solde}
            liste_comptes.append(compte)
            #le dictionnaire client
            client={}
            q=random.randint(0,9)
            w=random.randint(0,9)
            e=random.randint(0,9)
            code=int(str(q)+str(w)+str(e))
            while True:
                numero=int(input("entrer votre numero : "))
                if numero>0:
                    client={"nombre de client":numero,"code secret":code}
                    break
                else:
                    print("le numero n'etre pas negatif , entrer un nombre positif !")
            #le dictionnaire clientcompte
            clientcompte={"nombre de client":client["nombre de client"],"numero de compte":compte["nombre"]}
            liste_comptes.append(client)
            liste_comptes.append(clientcompte)
            print("on ajoute votre compte !")
            print("votre compte :")
            print("votre nombre de compte :",liste_comptes[0]["nombre"])
            print("votre numero :",liste_comptes[1]["nombre de client"])
            print("votre solde :",liste_comptes[0]["solde"])
            print("votre code secret :",liste_comptes[1]["code secret"])
            liste_compte=liste_comptes.copy()
            #if liste_comptes:
            print("-"*40)
            break
            #j'ai stocke les 3 dictionnaire dans une liste nomme liste_comptes , pour les réutiliser       
    listedescomptes.append(liste_compte)
def supprimer_client():
    while liste_comptes in listedescomptes:
        listedescomptes.remove(liste_comptes)
    print("votre compte est supprime !")
    print("-"*40)
def modifier_MPClient():
    index_client=1
    new_password=input("entrer le nouveau password (code secret) !")
    liste_comptes[index_client]["code secret"]=new_password
    print("votre code secret est change !")
    print("-"*40)
def afficher_solde():
    index_solde=0
    print("votre solde = ",liste_comptes[index_solde]["solde"])
    print("-"*40)
def deposer():
    argentdepose=float(input("entrer l'argent que tu peut deposer dans ton compte : "))
    solde=liste_comptes[0]["solde"]
    liste_comptes[0]["solde"]=solde + argentdepose
    print("votre solde est depose !")
    print("-"*40)
def retirer():
    solde=liste_comptes[0]["solde"]
    while True:
        argentretire=float(input("entrer l'argent que tu peut retirer dans ton compte: "))
        if argentretire<=solde:
            break
        else:
            print("tu n'avait pas ce solde dans votre compte !")
    liste_comptes[0]["solde"]=solde - argentretire
    print("votre argent est retirer !")
    print("-"*40)
def lambdagenererNumCompte():
    #j'ai utilise dans cette fonction le dictionnaire clientcompte
    index_clientcompte=2
    if not liste_comptes:
        print("il n'exist pas un compte !")
    else:
        index_clientcompte=2
        c=0
        for i in listedescomptes:
            c=c+1
        n=int(input("entrer le numero de client : "))
        for i in range(c):
            if listedescomptes[i][index_clientcompte]["nombre de client"]==n:
                print("le numero de compte de ce client : ",listedescomptes[i][index_clientcompte]["numero de compte"])
    print("-"*40)
def EcrireFichierCSV():
    if not liste_comptes:
        print("il n'exist pas un compte !")
    else:
        c=0
        for i in listedescomptes:
            c=c+1
        for i in range(c):
            CSV_info={}
            index_client=1
            CSV_info["nombre de client"]=listedescomptes[i][index_client]["nombre de client"]
            CSV_info["code secret"]=listedescomptes[i][index_client]["code secret"]
            print(CSV_info)
    print("-"*40)
def manipSTS():
    if not liste_comptes:
        print("il n'exist pas un compte !")
    else:
        c=0
        for i in listedescomptes:
            c=c+1
        for i in range(c):
            index_clientcompte=2
            liste_STS=[]
            liste_STS.append(listedescomptes[i][index_clientcompte])
            tupleSTS=tuple(liste_STS)
            setSTS=set(tupleSTS[0].items())
            print("le dictionnaire clientcompte sous form d'une liste : ",liste_STS)
            print("le dictionnaire clientcompte sous form d'une tuple : ",tupleSTS)
            print("le dictionnaire clientcompte sous form d'un set : ",setSTS)
    print("-"*40)
#le programme principux
liste_comptes=[]
listedescomptes=[]
while True:
    print("""choose one :
    1-agent
    2-client
    3-quit""")
    choix=input("entrer ton choix : ")
    if choix=="1":
        while True:
            print("""choose one:
            1-generer le numero de compte a partir du numero de client
            2-voir les numeros de clients et leurs codes secrets
            3-option manip STS
            4-quit""")
            b=input("entrer votre choix : ")
            if b=="1":                
                lambdagenererNumCompte()
            elif b=="2":
                EcrireFichierCSV()
            elif b=="3":
                manipSTS()
            elif b=="4":
                break
            else:
                print("choix invalide , please entrer un nombre entre 1 et 4 !")
    elif choix=="2":
        while True:
            print("""choose one:
            1-ajouter un compte
            2-quit""")
            x=input("entrer votre choix : ")
            if x=="1":
                ajouter_client()
                while True:
                    print("""choose one:
                    1-supprimer le compte
                    2-modifier le code secret
                    3-afficher le solde
                    4-deposer l'argent
                    5-retirer l'argent
                    6-quit""")
                    choix=input("entrer votre choix : ")
                    if choix=="1":
                        supprimer_client()
                        break
                    elif choix=="2":
                        modifier_MPClient()
                    elif choix=="3":
                        afficher_solde()
                    elif choix=="4":
                        deposer()
                    elif choix=="5":
                        retirer()
                    elif choix=="6":
                        break
                    else:
                        print("choix invalide , please entrer un nombre entre 1 et 6 !")
                break
            elif x=="2":
                break
            else:
                print("choix invalide , please entrer un nombre entre 1 et 2 !")           
    elif choix=="3":
        break
    else:
        print("choix invalide , please entrer un nombre entre 1 et 3 ")
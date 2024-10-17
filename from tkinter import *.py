from tkinter import * 
#création de la fenetre de jeu et attribution de nom
fenetre = Tk()
fenetre.title("fenetre joueur")
plateau_j1 = [[0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0]]

plateau_j1A = [[0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0]]

plateau_j2 = [[0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0]]


plateau_j2A = [[0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0]]




tous_les_boutons=[]
pacatta= False
listeplace = []

TJ= "J1"
plateau_des_joueurs = {"J1": plateau_j1, "J2" :plateau_j2}
liste_bateaux_restants = { "J1" : { "5C": 1, "4C":1, "3C":2, "2C":1},  "J2" : { "5C": 1, "4C":1, "3C":2,  "2C":1} }
liste_bateaux=[]

def bateau_couler(ligne,colonne):
    global liste_bateaux
    for bateaux in liste_bateaux:
        for coord in bateaux :
            print(liste_bateaux)
            print (bateaux)
            print (coord)


            if plateau_des_joueurs[TJ][coord[0]][coord[-1]]==2:

                ##verifier chaque coordonnés pour bateau pour que savoir si bateau coulé
                if TJ=="TJ1":
                    for i in range (5):
                        if plateau_des_joueurs[TJ][liste_bateaux[i][0]][liste_bateaux[i][0]]==2:
                            return True
                        else :
                            return "toucher"
                else:
                    for i in range (5):
                        if plateau_des_joueurs[TJ][liste_bateaux[5+i][0]][liste_bateaux[5+i][0]]==2:
                            return True
                        else :
                            return "toucher"
    return False




def cliquer_sur_bouton(case  , ligne ,colonne):
    global TJ
    global listeplace
    if pacatta==False:
        global plateau_des_joueurs
        if plateau_des_joueurs[TJ][ligne][colonne]==1:
            #afficher un truc met autre part
            pass
        else:
            listeplace+=[[ligne,colonne]]
            for ligne in plateau_des_joueurs[TJ]:
                print (ligne)
    
    if pacatta== True:
        if TJ=="J1":
            TJ="J2"
        else:
            TJ="J1"
        if plateau_des_joueurs[TJ][ligne][colonne]==1:
            plateau_des_joueurs[TJ][ligne][colonne]==2
            if bateau_couler(ligne ,colonne)==False:
                print ("louper")
            elif bateau_couler(ligne,couleur)=="toucher":
                print ("toucher")
            else :
                if TJ=="J1":
                    print("J2 a gagné")
                else:
                    print("J1 a gagné")
            if TJ=="J1":
                for ligne in plateau_j2A:
                 print (ligne)
                





def verifier ():
    global liste_bateaux_restants
    global listeplace
    global TJ
    if len(listeplace) not in [2, 3, 4, 5]:
        return False
###prends la ligne et la colonne de chaque elt in listeplace
    else :
        if len(listeplace)==2:
            if liste_bateaux_restants[TJ]["2C"]==0:
                return False
            liste_bateaux_restants[TJ]["2C"]-=1
        if len(listeplace)==3:
            if liste_bateaux_restants[TJ]["3C"]==0:
                return False
            liste_bateaux_restants[TJ]["3C"]-=1
        if len(listeplace)==4:
            if liste_bateaux_restants[TJ]["4C"]==0:
                return False
            liste_bateaux_restants[TJ]["4C"]-=1
        if len(listeplace)==5:
            if liste_bateaux_restants[TJ]["5C"]==0:
                return False
            liste_bateaux_restants[TJ]["5C"]-=1
    lignes = [pos[0] for pos in listeplace]
    colonnes = [pos[1] for pos in listeplace]

    

    if len(set(lignes)) == 1:  # Alignement horizontal
        # Vérifier la contiguïté
        if sorted(colonnes) == list(range(min(colonnes), max(colonnes) + 1)):
            
            return True

        else:
            return False

    elif len(set(colonnes)) == 1:  # Alignement vertical
        # Vérifier la contiguïté
        if sorted(lignes) == list(range(min(lignes), max(lignes) + 1)):
            
            return True
        else:
            
            return False
    
    
        
    



def ok_selection_bouton():
    global TJ
    global listeplace
    global plateau_des_joueurs
    global liste_bateaux
    if verifier():
        liste_bateaux+=[listeplace]#####5premier J1 5dernier J2
        for elt in listeplace:
            plateau_des_joueurs[TJ][elt[0]][elt[-1]]=1
        listeplace=[]
        if liste_bateaux_restants[TJ]["2C"]== 0 and liste_bateaux_restants[TJ]["3C"]==0 and liste_bateaux_restants[TJ]["4C"]==0 and liste_bateaux_restants[TJ]["5C"]==0 :
            if TJ=="J2":
                TJ="J1"
                global pacatta
                pacatta=True
                print("maintenant on attaque")
            TJ= "J2"
            for bouton in tous_les_boutons:
                bouton.config(fg="black")
    else :
        print("non")
    listeplace=[]
lignes=10
colonnes=10
nom_ligne=["A","B","C","D","E","F","G","H","I","J"]





#création des boutons et de la grille
for ligne in range (lignes):
    for colonne in range (colonnes):
        case = Button(text=(nom_ligne[ligne],colonne+1) )
        case.config(command=lambda btn=case, l=ligne ,c=colonne :cliquer_sur_bouton(btn ,l ,c) , width= 6 , height= 2 )  # config de la commande après car sinon la fonction appelle quelque chose qui n'existe pas encore
        tous_les_boutons.append(case)

        
        case.grid(row=ligne,column=colonne, padx=0 ,pady=0)


case = Button(text= "ok" )
case.config(command=lambda btn=case :ok_selection_bouton() , width= 6 , height= 2 )
case.grid(row=13,column=6, padx=0 ,pady=0)














#lancement de la boucle principale
fenetre.mainloop()


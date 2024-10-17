if TJ=="TJ1":
    for i in range (5):
        if plateau_des_joueurs[TJ][liste_bateaux[i][0]][liste[i][0]]==2:
            return True
        else :
            return False
else:
    for i in range (5):
        if plateau_des_joueurs[TJ][liste_bateaux[5+i][0]][liste[5+i][0]]==2:
            return True
        else :
            return False
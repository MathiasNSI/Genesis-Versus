# Créé par mstoeckl, le 22/01/2024 en Python 3.7
from tkinter import *

# ------------ On commence par définir toutes les fonctions qui seront utilisées ------------

def enfoncee(evt) :   # Crée une fonction pour exécuter des instructions quand on appuie sur une touche
    global V1X,V1Y,V2X,V2Y , pos  # Permet d'utiliser les variables créées ailleurs dans le programme (et pas dans une fonction)
    t = evt.keysym    # Permet de récupérer dans la variable t la valeur de la touche enfoncée
    if t == 'z' and 3 in ColisionPerso1Y:
        V1X, V1Y = 0, -5
    elif t == 's' :
        V1X, V1Y = 0, 5
    elif t == 'q' :
        V1X, V1Y = -5, 0
    elif t == 'd' :
        V1X, V1Y = 5, 0
    elif t == 'Right' :
        V2X, V2Y = 5, 0
    elif t == 'Left' :
        V2X, V2Y = -5, 0
    elif t == 'Up' and 3 in ColisionPerso2Y:
        V2X, V2Y = 0, -5
    elif t == 'Down' :
        V2X, V2Y = 0, 5

def relachee(evt) :    # Crée une fonction pour exécuter des instructions quand on relâche une touche
    global V1X, V1Y, V2X, V2Y
    t = evt.keysym
    if t == "q" or "s" or "d" or "z":
        V1Y,V1X = 0,0
    if t == "Right" or "Left" or "Down" or "Up":
        V2Y,V2X = 0,0

def physique():    # Crée une fonction pour exécuter des instructions à chaque fois qu'on "appelle" cette fonction
    global X1,Y1,X2,Y2,V1X,V1Y,V2X,V2Y,ColisionPerso1X,ColisionPerso1Y,ColisionPerso2X,ColisionPerso2Y

    ColisionPerso1X = canevas.find_overlapping(X1-100+V1X,Y1-100,X1+100+V1X,Y1+100)
    ColisionPerso1Y = canevas.find_overlapping(X1-100,Y1-110+V1Y,X1+100,Y1+110+V1Y)
    ColisionPerso2X = canevas.find_overlapping(X2-100+V2X,Y2-100,X2+100+V2X,Y2+100)
    ColisionPerso2Y = canevas.find_overlapping(X2-100,Y2-110+V2Y,X2+100,Y2+110+V2Y)

    if 3 not in ColisionPerso1Y:
        Y1 = Y1+2
    if 3 not in ColisionPerso2Y:
        Y2 = Y2+2

    if len(ColisionPerso1Y) == 1:
        Y1 = Y1+ V1Y
    if len(ColisionPerso2Y) == 1:
        Y2 = Y2+ V2Y
    ##print("Y :",ColisionPerso1Y)

    if len(ColisionPerso1X) == 1:
        X1 = X1+ V1X
    if len(ColisionPerso2X) == 1:
        X2 = X2+ V2X
    ##print("X :",ColisionPerso1X)


    canevas.coords(perso1,X1,Y1)
    canevas.coords(perso2,X2,Y2)
    fenetre.after(5,physique)  # Permet de relancer la fonction animation après 5 ms, donc elle tournera en boucle sans arrêt

def stop(evt):
    fenetre.destroy()   # Permet de détruire la fenêtre et de sortir du programme

def centre(evt):
    global X1,Y1,X2,Y2
    X1,Y1=400,500
    X2,Y2=600,500
# ------------ Le programme principal est ici ------------

fenetre=Tk()
fenetre.geometry('1300x600')
fenetre.title("Promenons-nous...")

canevas=Canvas(fenetre,bg='brown',height=600,width=1300)
canevas.place(x=0,y=0)
fenetre.focus_force() # Permet de mettre la fenêtre automatiquement en premier plan

X1 , Y1 , V1X , V1Y = 200 , 200 , 0 , 0
X2 , Y2 , V2X , V2Y = 1100 , 200 , 0 , 0  # Initialise la position et la vitesse des personnage

fichier1 = PhotoImage(master = fenetre,file="perso1.gif") # Permet de convertir une image png en une variable utilisable par TKinter
perso1 = canevas.create_image(X1,Y1,image=fichier1)  #Permet de placer une image convertie sur le canevas
fichier2 = PhotoImage(master = fenetre,file="perso2.gif") # Permet de convertir une image png en une variable utilisable par TKinter
perso2 = canevas.create_image(X2,Y2,image=fichier2)  #Permet de placer une image convertie sur le canevas
plateforme = canevas.create_rectangle(100,500,1200,400,fill='red')

fenetre.bind_all("<KeyPress>", enfoncee)  # Permet de définir la fonction qui sera lancée quand on appuie sur une touche
fenetre.bind_all("<KeyRelease>", relachee)  # Permet de définir la fonction qui sera lancée quand on relâche une touche
canevas.bind('<ButtonPress-3>', stop)  # Permet de définir la fonction qui sera lancée quand on clique sur le bouton droit de la souris
canevas.bind('<ButtonPress-1>', centre)

physique()  # Permet de lancer la fonction principale, qui après tournera toute seule "en boucle"

fenetre.mainloop()

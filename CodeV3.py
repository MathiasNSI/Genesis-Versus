# Créé par mstoeckl, le 22/01/2024 en Python 3.7
from tkinter import *
import time
# ------------ On commence par définir toutes les fonctions qui seront utilisées ------------

def InterractionObjet(X,Y,Force):
    global X1,Y1,X2,Y2,V1X,V1Y,V2X,V2Y

    dist_x1 = X - X1
    dist_y1 = Y - Y1
    dist_x2 = X - X2
    dist_y2 = Y - Y2
    if ((dist_x1 ** 2 + dist_y1 ** 2) ** 0.5) != 0:
        magnitude1 = Force / ((dist_x1 ** 2 + dist_y1 ** 2) ** 0.5)
    if ((dist_x2 ** 2 + dist_y2 ** 2) ** 0.5) != 0:
        magnitude2 = Force / ((dist_x2 ** 2 + dist_y2 ** 2) ** 0.5)

    force_x1 = magnitude1 * dist_x1
    force_y1 = magnitude1 * dist_y1 *10
    force_x2 = magnitude2 * dist_x2
    force_y2 = magnitude2 * dist_y2 *10

    V1X += force_x1
    V1Y += force_y1
    V2X += force_x2
    V2Y += force_y2


def DeplacementProjectile(Objet, X, Y, VX, VY, Force):
    global V1X, V1Y, V2X, V2Y

    X += VX
    Y += VY

    # Appel de la fonction d'interraction
    InterractionObjet(X, Y, Force)

    canevas.coords(Objet, X-20, Y-20, X+20, Y+20)  # Met à jour la position du projectile

    # Vérifie si le projectile est toujours dans les limites de la fenêtre
    if X < 0 or X > 1300 or Y < 0 or Y > 600:
        canevas.delete(Objet)  # Supprime le projectile s'il sort de la fenêtre
        V1X, V1Y, V2X, V2Y = 0, 0, 0, 0
        return

    # Réappel de la fonction DeplacementObjet après un délai de 5 ms
    fenetre.after(5, lambda: DeplacementProjectile(Objet, X, Y, VX, VY, Force))


def enfoncee(evt) :   # Crée une fonction pour exécuter des instructions quand on appuie sur une touche
    global V1X,V1Y,V2X,V2Y ,Orientation1 , Orientation2  # Permet d'utiliser les variables créées ailleurs dans le programme (et pas dans une fonction)
    t = evt.keysym    # Permet de récupérer dans la variable t la valeur de la touche enfoncée
    if t == 'z' and 3 in ColisionPerso1Y:
        V1Y = -15
        Orientation1 = "haut"
    if t == 's' :
        V1Y = 5
        Orientation1 = "bas"
    if t == 'q' :
        V1X = -5
        Orientation1 = "gauche"
    if t == 'd' :
        V1X = 5
        Orientation1 = "droite"
    if t == 'm' :
        V2X = 5
        Orientation2 = "droite"
    if t == 'k' :
        V2X = -5
        Orientation2 = "gauche"
    if t == 'o' and 3 in ColisionPerso2Y:
        V2Y = -15
        Orientation2 = "haut"
    if t == 'l' :
        V2Y = 5
        Orientation2 = "bas"

def relachee(evt) :    # Crée une fonction pour exécuter des instructions quand on relâche une touche
    global V1X, V1Y, V2X, V2Y
    t = evt.keysym
    #print(t)
    if t == "q":
        V1X = 0
    if t == "s":
        V1Y = 0
    if t == "d":
        V1X = 0
    if t == "z":
        V1Y = 0
    if t == "m":
        V2X = 0
    if t == "k":
        V2X = 0
    if t == "l":
        V2Y = 0
    if t == "o":
        V2Y = 0

def attaque1(evt):
    global X1, Y1, Orientation1, Xprojectile, Yprojectile, VXprojectile, VYprojectile, projectile
    Force = -0.1
    VYprojectile = 0
    VXprojectile = 0

    if Orientation1 == "gauche":
        VXprojectile = -5
    if Orientation1 == "droite":
        VXprojectile = 5
    if Orientation1 == "haut":
        VYprojectile = -5
    if Orientation1 == "bas":
        VYprojectile = 5



    Xprojectile = X1 + VXprojectile
    Yprojectile = Y1 + VYprojectile


    projectile = canevas.create_oval(Xprojectile-20, Yprojectile-20, Xprojectile+20, Yprojectile+20, fill='red')

    # Appel initial de la fonction DeplacementObjet pour commencer le mouvement
    DeplacementProjectile(projectile, Xprojectile, Yprojectile, VXprojectile, VYprojectile,Force)

def attaque2(evt):
    global X1, Y1, Orientation1, Xprojectile, Yprojectile, VXprojectile, VYprojectile, projectile
    Force = 0.1
    VYprojectile = 0
    VXprojectile = 0

    if Orientation1 == "gauche":
        VXprojectile = -5
    if Orientation1 == "droite":
        VXprojectile = 5
    if Orientation1 == "haut":
        VYprojectile = -5
    if Orientation1 == "bas":
        VYprojectile = 5



    Xprojectile = X1 + VXprojectile
    Yprojectile = Y1 + VYprojectile


    projectile = canevas.create_oval(Xprojectile-20, Yprojectile-20, Xprojectile+20, Yprojectile+20, fill='blue')

    # Appel initial de la fonction DeplacementObjet pour commencer le mouvement
    DeplacementProjectile(projectile, Xprojectile, Yprojectile, VXprojectile, VYprojectile,Force)
def physique():
    global X1,Y1,X2,Y2,V1X,V1Y,V2X,V2Y,ColisionPerso1X,ColisionPerso1Y,ColisionPerso2X,ColisionPerso2Y,Xprojectile,Yprojectile

# Calcul de la force d'attraction du projectile sur les joueurs

    ColisionPerso1X = canevas.find_overlapping(X1-50+V1X,Y1-50,X1+50+V1X,Y1+50)
    ColisionPerso1Y = canevas.find_overlapping(X1-50,Y1-50+V1Y,X1+50,Y1+50+V1Y)

    ColisionPerso2X = canevas.find_overlapping(X2-50+V2X,Y2-50,X2+50+V2X,Y2+50)
    ColisionPerso2Y = canevas.find_overlapping(X2-50,Y2-50+V2Y,X2+50,Y2+50+V2Y)

    if 2 not in ColisionPerso1Y and 3 not in ColisionPerso1Y:
        Y1 = Y1+ V1Y
        if V1Y < 10:                #Ici on définit la vitesse limite du personnage pour des questions de jouabilité et éviter des bugs avec des vitesses de chute trop haute
            V1Y = V1Y + 0.5         #Ici on ajoute la force de la gravité à notre variable de déplacement verticale
    if 1 not in ColisionPerso2Y and 3 not in ColisionPerso2Y:
        Y2 = Y2+ V2Y
        if V2Y < 10:
            V2Y = V2Y + 0.5
    #print("Y :",ColisionPerso1Y)

    if 2 not in ColisionPerso1X and 3 not in ColisionPerso1X:
        X1 = X1+ V1X
    if 1 not in ColisionPerso2X and 3 not in ColisionPerso2X:
        X2 = X2+ V2X
    #print("X :",ColisionPerso1X)

    canevas.coords(perso1,X1,Y1)
    canevas.coords(perso2,X2,Y2)
    fenetre.after(5,physique)  # Permet de relancer la fonction animation après 5 ms, donc elle tournera en boucle sans arrêt

def stop(evt):
    fenetre.destroy()   # Permet de détruire la fenêtre et de sortir du programme

def centre(evt):
    global X1,Y1,X2,Y2,V1X,V1Y,V2X,V2Y
    X1 , Y1 , V1X , V1Y = 200 , 200 , 0 , 0
    X2 , Y2 , V2X , V2Y = 1100 , 200 , 0 , 0

# ------------ Le programme principal est ici ------------

fenetre=Tk()
fenetre.geometry('1300x600')
fenetre.title("Genesis Versus")

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
canevas.bind_all('<e>', attaque1)
canevas.bind_all('<a>', attaque2)
canevas.bind_all('<i>', attaque1)
canevas.bind_all('<p>', attaque2)

physique()  # Permet de lancer la fonction principale, qui après tournera toute seule "en boucle"

fenetre.mainloop()

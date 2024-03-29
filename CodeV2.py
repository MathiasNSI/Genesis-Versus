from tkinter import *

# ------------ On commence par définir toutes les fonctions qui seront utilisées ------------

def enfoncee(evt) :   # Crée une fonction pour exécuter des instructions quand on appuie sur une touche
    global V1X,V1Y,V2X,V2Y , pos  # Permet d'utiliser les variables créées ailleurs dans le programme (et pas dans une fonction)
    t = evt.keysym    # Permet de récupérer dans la variable t la valeur de la touche enfoncée
    if t == 'z' :
        V1X, V1Y = 0, -5
    elif t == 's' :
        V1X, V1Y = 0, 5
    elif t == 'q' :
        V1X, V1Y = -5, 0
    elif t == 'd' :
        V1X, V1Y = 5, 0
    elif t == 'd' :
        V1X, V1Y = 5, 0
    elif t == 'Right' :
        V2X, V2Y = 5, 0
    elif t == 'Left' :
        V2X, V2Y = -5, 0
    elif t == 'Up' :
        V2X, V2Y = 0, -5
    elif t == 'Down' :
        V2X, V2Y = 0, 5

def relachee(evt) :    # Crée une fonction pour exécuter des instructions quand on relâche une touche
    global V1X, V1Y, V2X, V2Y
    V1X, V1Y, V2X, V2Y = 0, 0, 0, 0

def animation():    # Crée une fonction pour exécuter des instructions à chaque fois qu'on "appelle" cette fonction
    global X1,Y1,X2,Y2
    X1, Y1 = X1 + V1X, Y1+ V1Y
    X2, Y2 = X2 + V2X, Y2+ V2Y
    canevas.coords(perso1,X1,Y1)
    canevas.coords(perso2,X2,Y2)
    fenetre.after(5,animation)  # Permet de relancer la fonction animation après 5 ms, donc elle tournera en boucle sans arrêt

def stop(evt):
    fenetre.destroy()   # Permet de détruire la fenêtre et de sortir du programme

def centre(evt):
    global X1,Y1,X2,Y2
    X1,Y1=400,500
    X2,Y2=600,500
# ------------ Le programme principal est ici ------------

fenetre=Tk()
fenetre.geometry('1000x1000')
fenetre.title("Promenons-nous...")

canevas=Canvas(fenetre,bg='brown',height=1000,width=1000)
canevas.place(x=0,y=0)
fenetre.focus_force() # Permet de mettre la fenêtre automatiquement en premier plan

X1 , Y1 , V1X , V1Y = 400 , 500 , 0 , 0
X2 , Y2 , V2X , V2Y = 600 , 500 , 0 , 0  # Initialise la position et la vitesse des personnage

fichier = PhotoImage(file="perso1.gif") # Permet de convertir une image gif en une variable utilisable par TKinter
perso1 = canevas.create_image(X2,Y2,image=fichier)  #Permet de placer une image convertie sur le canevas
fichier = PhotoImage(file="perso2.gif") # Permet de convertir une image gif en une variable utilisable par TKinter
perso2 = canevas.create_image(X2,Y2,image=fichier)  #Permet de placer une image convertie sur le canevas

fenetre.bind_all("<KeyPress>", enfoncee)  # Permet de définir la fonction qui sera lancée quand on appuie sur une touche
fenetre.bind_all("<KeyRelease>", relachee)  # Permet de définir la fonction qui sera lancée quand on relâche une touche
canevas.bind('<ButtonPress-3>', stop)  # Permet de définir la fonction qui sera lancée quand on clique sur le bouton droit de la souris
canevas.bind('<ButtonPress-1>', centre)

animation()  # Permet de lancer la fonction principale, qui après tournera toute seule "en boucle"

fenetre.mainloop()
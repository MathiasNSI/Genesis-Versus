from tkinter import *

# ------------ On commence par définir toutes les fonctions qui seront utilisées ------------

def enfoncee(evt) :   # Crée une fonction pour exécuter des instructions quand on appuie sur une touche
    global VX, VY, pos  # Permet d'utiliser les variables créées ailleurs dans le programme (et pas dans une fonction)
    t = evt.keysym    # Permet de récupérer dans la variable t la valeur de la touche enfoncée
    if t == 'z' :
        VX, VY = 0, -5
    elif t == 's' :
        VX, VY = 0, 5
    elif t == 'q' :
        VX, VY = -5, 0
    elif t == 'd' :
        VX, VY = 5, 0

def relachee(evt) :    # Crée une fonction pour exécuter des instructions quand on relâche une touche
    global VX, VY
    VX, VY = 0, 0

def animation():    # Crée une fonction pour exécuter des instructions à chaque fois qu'on "appelle" cette fonction
    global X,Y
    X, Y = X + VX, Y+ VY
    canevas.coords(perso,X,Y)
    fenetre.after(5,animation)  # Permet de relancer la fonction animation après 5 ms, donc elle tournera en boucle sans arrêt

def stop(evt):
    fenetre.destroy()   # Permet de détruire la fenêtre et de sortir du programme

def centre(evt):
    global X,Y
    X,Y=350,300

# ------------ Le programme principal est ici ------------

fenetre=Tk()
fenetre.geometry('700x600')
fenetre.title("Promenons-nous...")

canevas=Canvas(fenetre,bg='brown',height=600,width=700)
canevas.place(x=0,y=0)
fenetre.focus_force() # Permet de mettre la fenêtre automatiquement en premier plan

X, Y, VX, VY = 260, 260, 0, 0  # Initialise la position et la vitesse du personnage

fichier = PhotoImage(file="perso.gif") # Permet de convertir une image gif en une variable utilisable par TKinter
perso = canevas.create_image(X,Y,image=fichier)  #Permet de placer une image convertie sur le canevas

fenetre.bind_all("<KeyPress>", enfoncee)  # Permet de définir la fonction qui sera lancée quand on appuie sur une touche
fenetre.bind_all("<KeyRelease>", relachee)  # Permet de définir la fonction qui sera lancée quand on relâche une touche
canevas.bind('<ButtonPress-3>', stop)  # Permet de définir la fonction qui sera lancée quand on clique sur le bouton droit de la souris
canevas.bind('<ButtonPress-1>', centre)

animation()  # Permet de lancer la fonction principale, qui après tournera toute seule "en boucle"

fenetre.mainloop()
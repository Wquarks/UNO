# importation de fichier utile par la suite ...
from random import *
import webbrowser
from tkinter import *
from tkinter.messagebox import *
fenetre = Tk()
fenetre.title("Le jeu du Uno")

while true :
    
        
    # Liste de cartes par couleur
    cb = ["0 bleu","1 bleu","2 bleu","3 bleu","4 bleu","5 bleu","6 bleu","7 bleu","8 bleu","9 bleu","1 bleu","2 bleu","3 bleu","4 bleu","5 bleu","6 bleu","7 bleu","8 bleu","9 bleu","+2 bleu","+2 bleu","carte +4","carte +4","passe ton tour bleu","passe ton tour bleu"]
    cr = ["0 rouge","1 rouge","2 rouge","3 rouge","4 rouge","5 rouge","6 rouge","7 rouge","8 rouge","9 rouge","1 rouge","2 rouge","3 rouge","4 rouge","5 rouge","6 rouge","7 rouge","8 rouge","9 rouge","+2 rouge","+2 rouge","carte +4","carte +4","passe ton tour rouge","passe ton tour rouge"]
    cj = ["0 jaune","1 jaune","2 jaune","3 jaune","4 jaune","5 jaune","6 jaune","7 jaune","8 jaune","9 jaune","1 jaune","2 jaune","3 jaune","4 jaune","5 jaune","6 jaune","7 jaune","8 jaune","9 jaune","+2 jaune","+2 jaune","carte +4","carte +4","passe ton tour jaune","passe ton tour jaune"]
    cv = ["0 vert","1 vert","2 vert","3 vert","4 vert","5 vert","6 vert","7 vert","8 vert","9 vert","1 vert","2 vert","3 vert","4 vert","5 vert","6 vert","7 vert","8 vert","9 vert","+2 vert","+2 vert","carte +4","carte +4","passe ton tour vert","passe ton tour vert"]
    cc = ["carte couleur","carte couleur","carte couleur","carte couleur"]
    # Liste de cartes par style
    cp = ["passe ton tour vert","passe ton tour vert","passe ton tour jaune","passe ton tour jaune","passe ton tour rouge","passe ton tour rouge","passe ton tour vert","passe ton tour vert"]
    c2= ["+2 bleu","+2 bleu","+2 rouge","+2 rouge","+2 jaune","+2 jaune","+2 vert","+2 vert"]
    c4= ["carte +4","carte +4","carte +4","carte +4","carte +4","carte +4","carte +4","carte +4"]
    zero =["0 bleu","0 rouge","0 jaune","0 vert"]
    un =["1 bleu","1 rouge","1 jaune","1 vert"]
    deux =["2 bleu","2 rouge","2 jaune","2 vert"]
    trois =["3 bleu","3 rouge","3 jaune","3 vert"]
    quatre =["4 bleu","4 rouge","4 jaune","5 vert"]
    cinq =["5 bleu","5 rouge","5 jaune","5 vert"]
    six =["6 bleu","6 rouge","6 jaune","6 vert"]
    sept =["7 bleu","7 rouge","7 jaune","7 vert"]
    huit =["8 bleu","8 rouge","8 jaune","8 vert"]
    neuf =["9 bleu","9 rouge","9 jaune","9 vert"]
    
    # Autre liste
    pioche = cb + cr + cj + cv + cc
    couleur =[cb,cr,cj,cv,cc]
    style =[zero,un,deux,trois,quatre,cinq,six,sept,huit,neuf,c2,c4,cp,cc]
    tas = []
    ordi = []
    moi = []
    a=[]
    suiv_ordi=[]
    suiv_moi=[]
    lis2=[]
    vaarr=[]
    nbr=cr
    imlist=[]
    colbg=["orange"]
    mode_nuit=["Mode nuit"]
    mode_jour=["Mode jour ✓"]
    mode_pers=["Personnaliser"]
    mode_rouge=["Rouge"]
    mode_vert=["Vert"]
    mode_bleu=["Bleu"]
    mode_cyan=["Cyan"]
    mode_jaune=["Jaune"]
    mode_magenta=["Magenta"]
    barre=["0"]
    but=["0"]
    fr=["true"]
    ecrtxt=["Reduire la fenêtre"]
    tailler=["écran réduit "]
    taillep=["Plein écran ✓"]
    erre=["0"]
    txtcharg=["Préparation du jeu ..."]
    
    #qq var
    b=0
    c=0
    n=0
    vitesse= 4
    dx=2
    dy=0
    dc=500
    selection1=0
    co="rouge"
   
    
    def aae():
        fenetre.destroy()

    def battage() :
        if len(tas) <= 2 :
            nel = len(tas) -1
            for ra in range (nel) :
                ne = tas[ra]
                tas.remove(ne)
                pioche.append(ne)
        elif len(tas) == 0 :
            showinfo("pioche", "Il n'y a plus rien dans la pioche")
            
    def cls() :
        for c in fenetre.winfo_children():
            c.destroy()
        fenetre.quit()
        try:
            for c in root.winfo_children():
                c.destroy()
            root.quit()
        except:
            None
            
    def control_carte() :
        for h in style:
             if g in h :
                 if b in h :
                     m.append(g)

        for j in couleur:
            if g in j :
                if b in j :
                    m.append(g)

    def alert():
        webbrowser.open("Regle-uno.html")

    def colpar() :
        mode_nuit.append("Mode nuit ")
        mode_jour.append("Mode jour ")
        mode_rouge.append("Rouge")
        mode_vert.append("Vert")
        mode_bleu.append("Bleu")
        mode_cyan.append("Cyan")
        mode_jaune.append("Jaune")
        mode_magenta.append("Magenta")
        mode_pers.append("Personnaliser")

    def mnuit():
        colbg.append("grey")
        colpar()
        mode_nuit.append("Mode nuit ✓")
        mbar()

    def mjour():
        colbg.append("orange")
        colpar()
        mode_jour.append("Mode jour ✓")
        mbar()
        
    def mrouge():
        colbg.append("red")
        colpar()
        mode_rouge.append("Rouge✓")
        mode_pers.append("Personnaliser ✓")
        mbar()
        
    def mvert():
        colbg.append("green")
        colpar()
        mode_vert.append("Vert ✓")
        mode_pers.append("Personnaliser ✓")
        mbar()

    def mbleu():
        colbg.append("blue")
        colpar()
        mode_bleu.append("Bleu ✓")
        mode_pers.append("Personnaliser ✓")
        mbar()

    def mcyan():
        colbg.append("cyan")
        colpar()
        mode_cyan.append("Cyan ✓")
        mode_pers.append("Personnaliser ✓")
        mbar()

    def mjaune():
        colbg.append("yellow")
        colpar()
        mode_jaune.append("Jaune ✓")
        mode_pers.append("Personnaliser ✓")
        mbar()

    def mmagenta():
        colbg.append("magenta")
        colpar()
        mode_magenta.append("Magenta ✓")
        mode_pers.append("Personnaliser ✓")
        mbar()

    def aad():
        cls()
        n=0
        
    def aac():
        if len(pioche) >= 1 :
            b = choice(pioche)
            moi.append(b)
            pioche.remove(b)
            print("une nouvelle carte : ",b)
        battage()    
        ii=i+1
        try :
            if moi[ii] in cb :
                couleurbg = "blue"
                couleurfg = "cyan"
            elif moi[ii] in cr :
                couleurbg = "red"
                couleurfg= "black"
            elif moi[ii] in cj :
                couleurbg = "yellow"
                couleurfg= "black"
            elif moi[ii] in cv :
                couleurbg = "green"
                couleurfg= "cyan"
            if moi[ii] in c4 or moi[ii] in cc:
                couleurbg = "cyan"
                couleurfg= "black"
        except:
            None
            
        if ii <=8 :
            iii=ii
            ro= 5
        if ii > 8 :
            iii= ii-9
            ro= 7
        if ii > 17 :
            iii=ii-18
            ro= 9
        if ii > 26 :
            iii=ii-27
            ro= 11
        if ii > 35 :
            iii=ii-36
            ro= 13
        if ii > 44 :
            iii=ii - 45
            ro = 15

        try:
            lis=str(b)+".png"
            print(lis)
        except:
            None
        
        try:
            photo=PhotoImage(file=lis)
            imlist.append(photo)
            #print(imlist)
            dessin=Canvas(fenetre,width=50,height=80,bg='black',bd=10)
            dessin.create_image(37,50,image=imlist[-1])
        except:
            dessin=Canvas(fenetre,width=50,height=80,bg=couleurbg,bd=10)
            
        dessin.grid(row = (ro-1) , column = iii, padx=4, pady=5 )
        
        boutton = Radiobutton(fenetre, text= b, width= 15 , bg=couleurbg, fg=couleurfg, variable=var, value=ii, indicatoron= 1)
        boutton.grid(row = ro , column = iii , sticky = S , padx=4, pady=5 )
       
                   

        for g in moi :
            for h in style:
                if g in h :
                    if b in h :
                        m.append(g)

        for j in couleur:
            if g in j :
                if b in j :
                    m.append(g)
                                            
        nb_pioche=1
        if nb_pioche==1 :
            b_pioche = Button(fenetre, text="Passer son tour ", width=20, command = aad ).grid(row= 21 , column=0, columnspan=20 )
     
    def ok():
        selection = var.get()
        print (moi[selection])
        if moi[selection] not in m :
            msg="La carte "+moi[selection]+" ne peut être jouée, veuillez choisir une autre carte."
            showwarning( "Vous vous êtes trompé." ,msg)  

        if (moi[selection]) == "carte couleur" or  (moi[selection]) == "carte +4" :

            try:
                root.destroy()
            except:
                None
                
            root = Tk()
            root.title("Choix des couleurs")  
            root.grid()
            root.configure(background=colbg[-1])
            
            label = Label(root, text= "", bg=colbg[-1]).grid(row=0,column=0)
            label = Label(root, text= "Veuillez choisir une couleur : ",bg=colbg[-1]).grid(row=1,column=0, columnspan=4)
            label = Label(root, text= "" , bg=colbg[-1]).grid(row=2,column=0)
                        
            varGr = IntVar()
            bouton0 = Radiobutton(root, text="Rouge", width=10, bg="red", fg="black", variable=varGr, value=0, command=redc, indicatoron= 1).grid(row=3,column=0, padx=1, pady=5 )
            bouton1 = Radiobutton(root, text="Vert", width=10, bg="green", fg="cyan", variable=varGr, value=1, command=greenc, indicatoron= 1).grid(row=3,column=1, padx=1, pady=5 )
            bouton2 = Radiobutton(root, text="Bleu", width=10, bg="blue", fg="cyan", variable=varGr, value=2, command=bluec, indicatoron= 1).grid(row=3,column=2, padx=1, pady=5 )
            bouton3 = Radiobutton(root, text="Jaune", width=10, bg="yellow", fg="black", variable=varGr, value=3,command=yellowc, indicatoron= 1).grid(row=3,column=3, padx=1, pady=5 )
            boutonok = Button(root, text="Valider", width=10, command= ook).grid(row=10,column=0, columnspan=4, pady=5 )
            root.mainloop()
            root.destroy()
        if moi[selection] in m :
            tas.append(moi[selection])
            moi.remove(moi[selection])
            cls()

      

    def redc():
        suiv_ordi=cr+cc+c4
        print ("la couleur choisie est le rouge")
        vaarr.append(suiv_ordi)
    def greenc():
        suiv_ordi=cv+cc+c4
        print ("la couleur choisie est le vert")
        vaarr.append(suiv_ordi)
    def bluec():
        suiv_ordi=cb+cc+c4
        print ("la couleur choisie est le bleu")
        vaarr.append(suiv_ordi)
    def yellowc():
        suiv_ordi=cj+cc+c4
        print ("la couleur choisie est le jaune")
        vaarr.append(suiv_ordi)

    def  ook() :
        
        varGr = IntVar()
        varr= varGr.get()
        selection1 = varGr.get()
        cls()

    def mbar() :
        menubar = Menu(fenetre)
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label=tailler[-1], command=plein)
        menu1.add_command(label=taillep[-1], command=plein)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=fenetre.destroy)
        menubar.add_cascade(label="Fenêtre", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label=mode_jour[-1], command=mjour)
        menu2.add_command(label= mode_nuit[-1], command=mnuit)
        menubar.add_cascade(label="Paramètres", menu=menu2)

        menu3 = Menu(menu2, tearoff=0)
        menu3.add_command(label=mode_rouge[-1], command=mrouge)
        menu3.add_command(label=mode_vert[-1], command=mvert)
        menu3.add_command(label=mode_bleu[-1], command=mbleu)
        menu3.add_command(label=mode_cyan[-1], command=mcyan)
        menu3.add_command(label=mode_jaune[-1], command=mjaune)
        menu3.add_command(label=mode_magenta[-1], command=mmagenta)
        
        menu2.add_cascade(label=mode_pers[-1], menu=menu3)

        menu4 = Menu(menubar, tearoff=0)
        menu4.add_command(label="Les règles du jeu", command=alert)
        menubar.add_cascade(label="Aide", menu=menu4)

        fenetre.config(menu=menubar)
        fenetre.configure(background=colbg[-1])
        
    def deplacement():
        global dx
        try:
            if (canvas.coords(balle1)[0]<0) or (canvas.coords(balle1)[2]>dc):
                dx=-1*dx
                z=str(barre[-1])
                barre.append(str(z))
                print((len(barre)-1))
            
            canvas.move(1,dx,dy)
            fenetre.after(vitesse,deplacement)
            
            if len(barre) > 2 :            
                txtcharg.append("Battage des cartes...")
                textdeb=Label(fenetre, text=txtcharg[-1],bg=colbg[-1]).grid(row=15, column=0, columnspan=20)

            if len(barre) > 4 :            
                txtcharg.append("Distribution des cartes...")
                textdeb=Label(fenetre, text=txtcharg[-1],bg=colbg[-1]).grid(row=15, column=0, columnspan=20)

            if len(barre) > 6 :            
                txtcharg.append("            C'est parti !            ")
                textdeb=Label(fenetre, text=txtcharg[-1],bg=colbg[-1]).grid(row=15, column=0, columnspan=20)
            
            if len(barre) > 7 :
                cls()
        except:
            None
            
    def plein():
        if fr[-1]=="False" :
            fr.append("True")
            ecrtxt.append("Réduire la fenêtre")
            tailler.append("Ecran réduit ")
            taillep.append("Plein écran ✓")
        else:
            fr.append("False")
            ecrtxt.append("Agrandir la fenêtre")
            tailler.append("Ecran réduit ✓")
            taillep.append("Plein écran ")
            
        if but[-1]=="0":    
            Button(fenetre, text=ecrtxt[-1], width=20, command = plein ).grid(row= 24 , column=0, columnspan=20 )
            
        fenetre.attributes('-fullscreen',fr[-1])
        mbar()

    def men ():
        if askyesno('', 'Etes vous sûr de vouloir retourner au menu ? \nCeci sera considéré comme un abandon de la partie...'):
            ordi.clear()
            moi.clear()
            erre.append("1")
            cls()
        else:
            None
#*********************************************************************************************************************************************************************************************************************************************************************************
    
    fenetre.grid()
    fenetre.geometry("1366x768")
    fenetre.configure(background=colbg[-1])
    fenetre.attributes('-fullscreen',fr[-1])
    
    for u in range(4):
        Label(fenetre, text="", bg=colbg[-1],width=180).grid(row=u, column=0,sticky = N)
        Label(fenetre, text="", bg=colbg[-1],width=180).grid(row=(10+u), column=0,sticky = N)
     
    Label(fenetre, text="      __                               _____                                                                      __   __                              ", bg=colbg[-1]).grid(row=5, column=0)
    Label(fenetre, text="    |   |       _____              /__  __\  _____   __   __            __        __   __          |   |  |   |   __   __     __      ", bg=colbg[-1]).grid(row=6, column=0)
    Label(fenetre, text="  |   |       |  ____\              |   |     |  ____\  |   |  |   |        |     \   |   |  |   |        |   |  |   |  |    \  |  |  /     \ ", bg=colbg[-1]).grid(row=7, column=0)#####
    Label(fenetre, text="  |   |__   |  __|__           __|   |     |  __|__   |   |_|   |         |   |   |  |   |_|   |        |   |_|   |  |  |\  \|  |  |   |   | ", bg=colbg[-1]).grid(row=8, column=0)
    Label(fenetre, text="  \____|  |_____/          \____|     |_____/   \ ___ /          |__ /    \ ___ /         \ ___ /   |_|  \__|    \__/  ", bg=colbg[-1]).grid(row=9, column=0)

    Button(fenetre, text="Commencer à jouer ", width=20, command = cls ).grid(row= 21 , column=0, columnspan=20 )
    Label(fenetre, text="", bg=colbg[-1],width=180).grid(row=22, column=0,sticky = N)

    Button(fenetre, text=ecrtxt[-1], width=20, command = plein ).grid(row= 24 , column=0, columnspan=20 )
    Button(fenetre, text="Les règles du jeu", width=20, command = alert ).grid(row= 23 , column=0, columnspan=20 )
    Button(fenetre, text="Quitter", width=20, command = aae ).grid(row=25, column=0, columnspan=20 )

   
    mbar()
    fenetre.mainloop()



###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###   ###
    but.append("1")
    for i in range (14) :
         Label(fenetre, text="",bg=colbg[-1]).grid(row=i)

    canvas = Canvas(fenetre,width = dc, height = 20 , bd=0, bg="white")
    canvas.grid(padx=(1366/2-300),pady=8)

    balle1 = canvas.create_rectangle(200,20,40,0,fill='green')
    Label(fenetre, text=txtcharg[-1],bg=colbg[-1]).grid(row=15, column=0, columnspan=20)

    deplacement()
    mbar()
    fenetre.mainloop()
    
    print("ok")
    #definir le jeux de l'ordi
    for i in range (7) :
        a = choice(pioche)
        pioche.remove(a)
        ordi.append(a)
    print("le jeu de l'ordi : ",ordi)
    
    #definir mon jeux
    for i in range (7) :
        a = choice(pioche)
        pioche.remove(a)
        moi.append(a)
    print("mon jeu : ",moi)


    # choisir la première carte du tas
    while b in cp or b in cc or b in c4 or b in c2 or b==0 :
        b = choice(pioche) # b est la carte sur le tas
    tas.append(b)
    pioche.remove(b)
    print("le tas :",tas)
    
                    
    while (len(moi) !=0) and ( len(ordi) !=0) :
        
    # c'est l ordi qui commence---------------------------------------------------------------------------------------------
        m=[]
        p=0
        b=tas[-1]

        print("le jeu de l'ordi : ",ordi)
        
        while p<3 :
            
            if b in cc or b in c4 :
                for g in ordi :
                    print(g, suiv_ordi)
                    if g in suiv_ordi:
                        print
                        m.append(g)
            else :
                print("==========================================================")
                for g in ordi :
                    control_carte()
            print("")
            if b in cp :
                if b==n :
                    ta= tas[-1]
                    m=[ta]
            print ("toutes les cartes que l'ordi peut jouer : ",m)

              
            
            p+=1
                       
            if m==[] :
                #remettre une nouvelle carte dans le jeu de l'ordi
                if len(pioche) >=1 :
                    n = choice(pioche)
                    ordi.append(n)
                    pioche.remove(n)
                    print("le tas :",tas)
                    print("le jeu de l'ordi : ",ordi)
                    print ("l'ordi pioche une nouvelle carte")
                battage()
                
                if b in cc or b in c4 :
                     for g in ordi :
                        for j in vaarr :
                            if g in j :
                                if b in j :
                                    m.append(g)
                        print("MMMMMMMMMMM",m,vaarr)
                else :
                    print("==========================================================")
                    for g in ordi :
                        control_carte()


                if b in cp :
                    ta= tas[-1]
                    m=[ta]
                    
                print ("toutes les cartes que l'ordi peut jouer 0000000: ",m)
                
                p+=1

            if m!=[] :
                n = choice(m)
                p+=5
                
            elif p<3:
                break

        if m==[] :
            print(" l'ordi passe son tour ")
            n=0
        elif m !=[]:
            print ("l'ordi joue : ",n)
            if b not in cp:
                ordi.remove(n)
                tas.append(n)
                txt3="l'ordi a joué : "+n
            #showinfo("",txt3)

        if b in cc or b in c4 :
            if b == n :
                nb = randrange(0,4)
                if nb == 0 :
                    nbr = cb
                    co="bleu"
                if nb == 1:
                    nbr = cr
                    co="rouge"
                if nb == 2 :
                    nbr = cj
                    co="jaune"
                if nb == 3 :
                    nbr = cv
                    co="vert"

                
            suiv_moi = nbr,cc,c4
            print(suiv_moi)
    # a l'humain de joué----------------------------------------------------------------------------------------------------------------------------

        if  len(ordi) !=0 :
            b=tas[-1]
            m=[]
            suiv_ordi=[]
            vaarr= []
            try:
                mbar()
            except:
                None
                
            if b in c2 :
                if b == n :
                    for i in range (2) :
                        if len(pioche) >= 1 :
                            a = choice(pioche)
                            pioche.remove(a)
                            moi.append(a)
                            battage()
                        
            if b in c4 :
                if b == n :
                    for i in range (4) :
                        if len(pioche) >= 1 :
                            a = choice(pioche)
                            pioche.remove(a)
                            moi.append(a)
                            battage()
                        
            for g in moi :
                control_carte() 

                if b in cc or b in c4 :
                    for g in ordi :
                        for j in suiv_moi :
                            if g in j :
                                if b in j :
                                   m.append(g)
                
            if "carte couleur" in moi :
                m.append("carte couleur")
            if "carte +4" in moi:
                m.append("carte +4" )
            print("")
            
            print ("toutes les cartes que je peux jouer : ",m)

            p+=1
                

                    # tkinter
            if b in cc or b in c4 :
                txt1="La dernière carte est : " + b
                txt1= txt1 + ", et la couleur choisie par l'ordinateur est le "
                txt1= txt1 + co
            else :
                txt1="La dernière carte est : " + b  

            photo1carte=b
                        
         
            var=IntVar()
            var1=IntVar()
            aa=len(moi)
            nb_pioche=0
            for i in range(aa):
                        
                if moi[i] in cb :       
                    couleurbg = "blue"
                    couleurfg = "cyan"
                elif moi[i] in cr :       
                    couleurbg = "red"
                    couleurfg= "black"
                elif moi[i] in cj :       
                    couleurbg = "yellow"
                    couleurfg= "black"
                elif moi[i] in cv :       
                    couleurbg = "green"
                    couleurfg= "cyan"
                if moi[i] in c4 or moi[i] in cc:
                    couleurbg = "cyan"
                    couleurfg= "black"
        ##################################
                if i <=8 :
                    iii=i
                    ro= 5
                if i > 8 :
                    iii= i-9
                    ro= 7
                if i > 17 :
                    iii= i-18
                    ro= 9
                if i > 26 :
                    iii= i-27
                    ro= 11
                if i > 35 :
                    iii= i-36
                    ro= 13
                if i > 44 :
                    iii= i-45
                    ro= 15
                
                lis=str(moi[i])+".png"
                print(lis)
                
                try :
                    photo=PhotoImage(file=lis)
                    imlist.append(photo)
                    #print(imlist)
                    dessin=Canvas(fenetre,width=50,height=80,bg='black',bd=10)
                    dessin.create_image(37,50,image=imlist[-1])
                   
                except:
                    dessin=Canvas(fenetre,width=50,height=80,bg=couleurbg ,bd=10)
                    
                dessin.grid(row = (ro-1) , column = iii , sticky = N , padx=4, pady=5 )
                boutton = Radiobutton(fenetre, text=moi[i], bg=couleurbg, fg=couleurfg, variable=var, value=i, indicatoron= 1 ,width= 15)
                boutton.grid(row = ro , column = iii , sticky = N, padx=4, pady=5 )
                
        ##################################
                
            if len(moi)<=9:
                col=i
                u=i+1
                while col < 8 :
                    col+=1
                    Label(fenetre, text="",width= 20,bg=colbg[-1] ).grid(row=3, column=col, padx=4, pady=5 )
                col1= col +1
           
            ii= i+1
            txtord="Il reste "+str(len(ordi))+" carte(s) à l'ordinateur."
            Label(fenetre, text=txtord,bg=colbg[-1]).grid(row=3, column=0, columnspan=20)  
            Label(fenetre, text=txt1,bg=colbg[-1]).grid(row=0, column=0, columnspan=20)

            lis1=photo1carte+".png"
            print(lis1)
            lis2.append(lis1)
            print(lis2)
            
            try:
                dessin1 = Canvas(fenetre,width=50,height=80,bg='black',bd=10)
                photo1=PhotoImage(file=lis1)
                dessin1.create_image(37,50,image=photo1)
             
            except:
                dessin1 = Canvas(fenetre,width=50,height=80,bg='black',bd=10)
            
            dessin1.grid(row = 2 ,column=0, columnspan=20 , sticky = N , padx=4, pady=5 )        
            textdeb=Label(fenetre, text=txt1, bg=colbg[-1]).grid(row=0, column=0, columnspan=20)

            if ro == 5 :
                dessin1 = Canvas(fenetre,width=50,height=80,bg=colbg[-1],bd=10).grid(row = 6 ,column=25, sticky = N , padx=4, pady=5 )
                Label(fenetre, text=" ", bg=colbg[-1]).grid(row=7, column=25, padx=4, pady=5 )

            b_pioche= Button(fenetre, text="Piocher une nouvelle carte ", width=20, command = aac ).grid(row=21, column=0, columnspan=20 )
            Button(fenetre, text = "Valider", width=20, command = ok ).grid(row = 20,  column=0, columnspan=20 )
            Button(fenetre, text="Retourner au menu", width=20, command = men ).grid(row=22, column=0, columnspan=20 )
            

            fenetre.mainloop()
           
            print("le jeu de l'ordi : ",ordi)
            if b in c2 :
                if b == n :
                    for i in range (2) :
                        a = choice(pioche)
                        pioche.remove(a)
                        ordi.append(a)

                    
            if b in c4 :
                if b == n :
                    for i in range (4) :
                        a = choice(pioche)
                        pioche.remove(a)
                        ordi.append(a)
            
    #faire joué l ordi...---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    print("_______________________________________________________________")

    if erre[-1]=="0":
        if len(moi)==0 :
            txtfin="Gagné"
        elif len(ordi)==0:
            txtfin="Perdu"

        showwarning( "Résultat : " ,txtfin)

        if askyesno('', 'Souhaitez-vous rejouer ?'):
            cls()
            
        else:
            showinfo('', 'Êtes-vous sûr de vouloir faire ça ?')
            showinfo("", "Tant pis...")
            fenetre.destroy()
     

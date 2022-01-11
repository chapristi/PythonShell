import time 


class Terminal:
    def __init__(self) -> None:
        self.nameConsole = "[default]"
        pass
    def callGoodFunction(self):
          s = input(self.nameConsole + ">>>")
          commandes= dict({
          "run":self.run,
          "name":self.name,
          "help":self.help
          })
          for key,value in commandes.items(): 
            if s == key:
              return value()
            elif s == "quit":
                return "break"
            
      
    def run(self) -> str:
       for i in range(0,5):
        print(".")
        time.sleep(1)
    def name(self) -> str:
        self.nameConsole = input("Entrez un nouveau nom pour le terminal ")
        print(f" le terminal se nomme maintenant {self.nameConsole}")
    def help(self) -> str:
        print("""\
         commandes:
                run =>  ("permet d'afficher 5 points avec delait "),
                name =>  ("permet de changer le nom de son terminal"),
                help =>  ("permet d'afficher les commandes"),
                quit => ("permet de fermer le terminal")
        """)
terminal = Terminal()
while True:     
  Call = terminal.callGoodFunction()
  if Call == "break":
    break
 



















import csv;
"""
la fonction WriteNewTab nous permet de recuperer les donnees du fichier csv entré
et creer un tableau de celui ci.
"""
def WriteNewTab(file):
    tab = []
    #on ouvre le fichier
    with open(file) as file:
        array = []
        for files in file:
            #on enleve le retour a la ligne mis par default dans le tableau
            files = files[:-1]
            #on ajoute la valeure au tableau
            array.append([files])
        return array
"""
la fonction PostNewFormat nous permet d'afficher les données recuperes de la fonction precedente 
et de l'affciher sous forme de tableau dans la console.
"""
def PostNewFormat():
    #appel de la fonction presedente pour recuperer les données
    tableau = WriteNewTab("samere.csv")
    #definir la ligne du tableau
    ligne = "+-----+-----+-----+-----+-----+-----+"

    ligne1 = tableau[0][0].replace(",", "")
    ligne2 = tableau[1][0].replace(",", "")
    ligne3 = tableau[2][0].replace(",", "")
    ligne4 = tableau[3][0].replace(",", "")
    ligne5 = tableau[4][0].replace(",", "")
    print(ligne)
    #affiche la ligne du tableau grace a la boucle
    for i in ligne1:
        #condition qui verifie que nous sommes a la premiere ligne pour y ajouter |
        if i == "A":
            print("| ", end="")
        #afficher la ligne en question
        print(f"{i}",end="")
        #condition qui verifie que nous sommes apres la premiere ligne pour y ajouter |
        if i == "1":
            print("  | ", end="")
    print("\n" + ligne)
    for i in ligne2:
        if i == "A":
            print("| ", end="")
        print(f"{i}",end="")
        if i == "2":
            print("  | ", end="")
    print("\n" + ligne)
    for i in ligne3:
        if i == "A":
            print("| ", end="")
        print(f"{i}",end="")
        if i == "3":
            print("  | ", end="")
    print("\n" + ligne)
    for i in ligne4:
        if i == "A":
            print("| ", end="")
        print(f"{i}",end="")
        if i == "4":
            print("  | ", end="")
    print("\n" + ligne)
    for i in ligne5:
        if i == "A":
            print("| ", end="")
        print(f"{i}",end="")
        if i == "5":
            print("  | ", end="")
    print("\n" + ligne)
PostNewFormat()

"""
def WriteNewTab(file):
    f= open (file)
    myReader = csv.reader(f)
    tableau = []
    for row in myReader:
        tableau.append(row)
    return tableau

csv = WriteNewTab("file.csv")

sort  = sorted(csv, key = lambda x: x[1])
print(sort)

"""



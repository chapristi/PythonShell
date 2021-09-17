import time 


class Terminal:
    def __init__(self) -> None:
        self.nameConsole = "[default]"
        pass
    def callGoodFunction(self):
        while True:
          s = input(self.nameConsole + ">>>")
          commandes= dict({"run":self.run,"name":self.name,"help":self.help})
          for key,value in commandes.items(): 
            if s == key:
              return value()
            elif s == "quit":
              print("a bientot")
              break
      
    def run(self):
       for i in range(0,5):
        print(".")
        time.sleep(1)
    def name(self):
        self.nameConsole = input("Entrez un nouveau nom pour le terminal ")
        print(f" le terminal se nomme maintenant {self.nameConsole}")
    def help(self):
        print("""\
         commandes:
                run =>  ("permet d'afficher 5 points avec delait "),
                name =>  ("permet de changer le nom de son terminal"),
                help =>  ("permet d'afficher les commandes"),
                quit => ("permet de fermer le terminal")
        """)
    
terminal = Terminal()
Call = terminal.callGoodFunction()

 

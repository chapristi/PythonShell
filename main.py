import time 


class Terminal:
    def __init__(self,command) -> None:
        self.command = command
        self.name = "[default]>"
        pass
    def callGoodFunction(self):
            commandes=dict({"run":self.run(),"name":self.name(),"help":self.help(),"quit":self.quit()})
            for key,value in commandes.items(): 
              if self.command == key:
                  return globals(value)
              elif self.command == "quit":
                  return False
    def run(self):
       for i in range(0,5):
        print(".")
        time.sleep(1)
    def name(self):
        self.name = input(f"{self.name} entrez le nouveau nom nouveau nom du terminal")
    def help(self):
        fiche =  """
            commandes:
                run =>  ("permet d'afficher 5 points avec delait "),
                name =>  ("permet de changer le nom de son terminal"),
                help =>  ("permet d'afficher les commandes"),
                quit => ("permet de fermer le terminal")
        """
        print(fiche)
    
       

while True:
    s = input("[default]>")
    Terminal = Terminal(s)
    Call = Terminal.callGoodFunction()
    if(Call == False):
        break
 
    

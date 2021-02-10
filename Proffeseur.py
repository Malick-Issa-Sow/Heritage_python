from Personne import Personne 

class Proffesseur(Personne):
    # Définition de notre classe Proffesseur
    """Classe définissant une Proffesseur caractérisée par :
    - son module
    """
      

    def __init__(self,nom,age,module): 
            """initialisation des attribut de la classe mere"""
            Personne.__init__(self,nom,age)
            """Pour l'instant, on ne va définir qu'un seul attribut"""
            self._module = module
    #getter----------------------------
    def _get_module(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture à l'attribut '_module'"""
        print("On accède à l'attribut _module!")
        return self._module
    #fin getter------------------------
    #setter---------------------------------------
    def _set_module(self, nouvelle_module):
        allModules = {
        'dwm' : ["python","Java","php"],
        'sr' : ['cablage','telephonie','php'],
        } 
        """Méthode appelée quand on souhaite modifier la filiere de l'apprenant"""
        nouvelle_module= input("Donner le nouveau module : ")
        if (dwm == allModules):
            print("Attention, il semble que le prof {}  à chager de module {}.".format( self._nom, nouvelle_module))
            self._module = nouvelle_module
        else:
            print("desoler la nouvelle module doit etre obligatoirement dans allModules")

    #fin setter-----------------------------------

    # On va dire à Python que notre attribut _module pointe vers une

    # propriété
    module = property(_get_module,_set_module)

    #la methode presenter
    def presenter(self):
            """Cette méthode se charge de presenter une personne"""
            print("Bonjour je suis une Proffesseur qui s'appele {} et age de {}  et ma module est {}".format(self._nom,self._age,self._module))


print("---------------------------------------------je vais tester la classe Professeur (test unitaire)---------------------------------------------------------")
pr=Proffesseur("Coumba",26,"java")
print(pr.presenter())
print("---------------------------------------------changer de module------------------------------------------------------")
print(pr._set_module("js"))
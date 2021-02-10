from Personne import Personne 


class Apprenant(Personne):
    # Définition de notre classe Apprenant

    """Classe définissant une personne caractérisée par :- son filiere"""
    """Constructeur de notre classe"""
    def __init__(self,nom,age,filiere): 
        """initialisation des attribut de la classe mere"""
        Personne.__init__(self,nom,age)
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self._filiere = filiere
        
    #getter---------------------------------------
    def _getFiliere(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture à l'attribut '_filiere'"""
        print("On accède à l'attribut _filiere!")
        return self._filiere
    #fin getter-----------------------------------

    #setter---------------------------------------
    def _set_filiere(self, nouvelle_filiere):
        filiers=["dev","sr"]
        nouvelle_filiere= input("Donner le nouveau filiere : ")
        """Méthode appelée quand on souhaite modifier la filiere de l'apprenant"""
        if nouvelle_filiere in filiers:
            print("Attention, il semble que l'apprenant {}  à chager de filiere  et son{}.".format( self._nom, nouvelle_filiere))
            self._filiere = nouvelle_filiere
        else:
            print("desoler la nouvelle filiere doit etre obligatoirement dans notre la notre bd(filieres)")

    #fin setter-----------------------------------

    # On va dire à Python que notre attribut _filiere pointe vers une

    # propriété
    filiere = property(_getFiliere,_set_filiere)

    #la methode presenter
    def presenter(self):
        """Cette méthode se charge de presenter une personne"""
        print("Bonjour je suis une apprenant qui s'appele {} et age de {}  et ma filiere est {}".format(self._nom,self._age,self._filiere))


print("---------------------------------------------je vais tester la classe Apprenant (test unitaire)--------------------------------------------------------")
a=Apprenant("ali",26,"dev")
print(a.presenter())
print("---------------------------------------------changer de filiere------------------------------------------------------")
print(a._set_filiere("js"))
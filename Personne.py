class Personne(object):# Définition de notre classe Personne
    """Classe définissant une personne caractérisée par :
    - son nom
    - son âge
    """
    def __init__(self,nom,age): # Notre méthode constructeur
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self._nom = nom
        self._age = age
    # getter--------------------------------
    def _getAge(self):
        """Méthode qui sera appelée quand on souhaitera accéder en
        lecture
        à l'attribut '_age'"""
        print("On accède à l'attribut _age!")
        return self._age
    
    def _getNom(self):
        """Méthode qui sera appelée quand on souhaitera accéder en
        lecture
        à l'attribut '_nom'"""
        print("On accède à l'attribut _nom!")
        return self._nom
    #fin getter---------------------------------
    #setter-------------------------------------
    def _set_nom(self, nouvelle_nom):
        """Méthode appelée quand on souhaite modifier la filiere de
        l'apprenant"""
        nouvelle_nom=input("Donner un nouveau nom :")
        if 	(len(nouvelle_nom) >	6) :
            print("Attention, il semble que la personne dont le nom est {}  à chager de nom et son nouveau nom est {}.".format(self._nom, nouvelle_nom))
            self._module = nouvelle_nom
        else:
            print("reaseryer la longueur du nom doit etre superieur ou egale a 6 ")
            nouvelle_nom=input("Donner un nouveau nom :")
            
    def _set_age(self, nouvelle_age):
        """ Méthode appelée quand on souhaite modifier la filiere de l'apprenant """
        nouvelle_age=int(input(" Donner un nouveau age : "))
        if 	(nouvelle_age >	16):
            print("Attention, il semble que la personne  dont le nom est {} et dont l'age est {} veux changer d'age et son nouveau age est {}.".format(self._nom,self._age, nouvelle_age))
            self._age = nouvelle_age
        else:
            print("reaseryer la longueur du nom doit etre superieur ou egale a 6 ")
            nouvelle_age=int(input(" Donner un nouveau age : "))
            

#fin setter-----------------------------------

    #la methode presenter

    def presenter(self):
        """Cette méthode se charge de presenter une personne"""
        print("Bonjour je suis une personne qui s'appele {} et age de {} ".format(self._nom,self._age))

"""je vais tester la classe personne (test unitaire)"""
print("---------------------------------------------je fais tester la classe personne (test unitaire)---------------------------------------------------------")
"""je fais instancier un objet de la classe personne """
personne1=Personne("Daouda",25)
"""je vais appeller la methode presenter de la classe personne """
print(personne1.presenter())
print("---------------------------------------------changer de nom------------------------------------------------------")
"""je vais appeller la methode(_set_nom) sur l'objet (personne1) pour changer le nom de  personne1 """
print(personne1._set_nom("lili"))
print("---------------------------------------------changer d'age--------------------------------------------------------")
"""je vais appeller la methode(_set_age) sur l'objet (personne1) pour changer le nom de  personne1 """
print(personne1._set_age(12))





"""Bonsoir Monsieur Ndieng , Veillier recevoir mon devoir d'integration de python 

Bonne fin de soiree
cordialement
 
Malick Issa SOW
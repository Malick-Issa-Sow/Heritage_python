from Personne import Personne 
from Proffeseur import Proffesseur
from Apprenant import Apprenant  


print("*****************************test-heritage-professeur***********************************")
prof1= Proffesseur("aly",25,"python")
print(prof1.presenter())
print("************************test-heritage-apprenant*****************************************")
app1= Apprenant("malick",45,"dev")
print(app1.presenter())
print("***************************test-heritage-personne***************************************")
per1= Personne("Samba",75)
print(per1.presenter())

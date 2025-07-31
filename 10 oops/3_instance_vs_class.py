#instance is also known as objects

#instance attributes has preference over the class attribute
 #here is an example 

class Shop:
    place = "jigani"
    landmark="near navodaya techno school"
    city= "anekal taluk"
    owner="kumar ji"

KumarPanStore= Shop()
#making an object from using shop and inbuiilt python functions

KumarPanStore.owner="Bijendar Kumar"
#here we updated an attribute in instance(objects)

#lets prints it now and see which owner name geets printed from the ,main class or the object we made

print(KumarPanStore.owner)# object with owner name 
print(Shop.owner)# class with owner name 

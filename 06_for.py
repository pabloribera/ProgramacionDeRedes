print("Practica 06_for.py")

clase=["Pablo" , "Pedro" , "Sara" , "Ariana" , "Diego"]
select=[]

for item in clase:
    print(item)
    if "a" in item:
        select.append(item)
        
print("Lista Select: " +str(select))


    

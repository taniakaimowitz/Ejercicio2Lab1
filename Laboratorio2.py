
def sum_items(lista):
    suma = 0
    for x in lista:
        if type(x) is int:
            suma = suma + x
    if suma == 0:
        print ("Ningun ítem es numérico")
    else:
        print ('La suma de todos los ítems es ' + str(suma))  
sum_items([“box”, “car”, “cat”, “tree”])


        
       


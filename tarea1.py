def operator_selector(operationType):
    operationOk=False
    while(operationOk==False):
        if(operationType=="1" or operationType=="2" or operationType=="3" or operationType=="4"):
            operationOk=True
        else:
                print("Opcion incorrecta, favor de intentar nuevamente")    
                operationType=input("Seleccione el tipo de operación que desea realizar\n 1:Suma \n 2:Resta\n 3:Multiplicacion\n 4:Division \n")

def operations(x,y,operationType):
    if(operationType=="1"):
        return(print("la suma de "+str(x)+" y "+str(y)+" es: "+str(x+y)))
    elif(operationType=="2"):
        return(print("la resta de "+str(x)+" y "+str(y)+" es: "+str(x-y)))
    elif(operationType=="3"):
            
        return(print("el producto de "+str(x)+" y "+str(y)+" es: "+str(x*y)))
    elif(operationType=="4"):
            return(print("el cociente de "+str(x)+" y "+str(y)+" es: "+str(x/y)))        
      
onApp=True
print("Bienvenido a la aplicación de calculadora")
numbersok=False
while(onApp==True):    
    operationType=input("Seleccione el tipo de operación que desea realizar\n 1:Suma \n 2:Resta\n 3:Multiplicacion\n 4:Division \n")
    operator_selector(operationType)
    while (numbersok==False):
        try:
            x1=(input("Ingrese el primer valor:\n"))
            x=float(x1)
            try:
                y1=input("Ingrese el segundo valor:\n")
                y=float(y1)
                if(operationType=="4" and y==0):
                    print("¡Error! no se puede dividir un número entre cero. \nIngrese nuevamente los valores de su división.")                
                else:
                    numbersok==True
                    break
            except ValueError:
                print("Valor incorrecto")
        except ValueError:
            print("Valor incorrecto")
    operations(x,y,operationType)
    salir=input(print("Presione 1 si desea continuar,presione cualquier tecla para salir:\n"))
    if(salir!="1"):
        onApp=False
        print("Saliendo de aplicación")
    else:
        numbersok=False

   

 


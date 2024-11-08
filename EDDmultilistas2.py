#SANTIAGO ELJACH E ISABELLA MORENO EDD :)

#EJERCICIO 2 DE MULTILISTAS

#listaempleados.append(["Juanito", 1500, 2000, 7000])
#listaempleados.append(["Emanuel", 200, 570, 790])
#listaempleados.append(["Isabella", 10000, 205800, 756000])
#listaempleados.append(["Margarita", 1250, 3000, 100])
#listaempleados.append(["Alejandro", 2000, 1000, 50])


listaempleados=[]
for i in range(5):
    print("  ")
    empleado = input("Ingrese el nombre del empleado: ")
   
    #while de validacion con try y catch para poder validar que el sueldo sea positivo: hacerlo para cada sueldo
    sw=1
    while sw==1:
        try:
            sueldo1 = float(input("Ingrese sueldo del primer mes:"))
            if sueldo1> 0:
                sw=0
                break
            else:
                 print("El sueldo debe ser un número positivo.")
                 
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
            

#para el sueldo del segundo mes
    sw=1
    while sw==1:
           
            try:
                sueldo2 = float(input("Ingrese sueldo del segundo mes:"))
                if sueldo2> 0:
                   sw=0
                   break
                else:
                    print("El sueldo debe ser un número positivo.")
                 
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
              
#vlaidacion y pedir el sueldo del tercer mes
    sw=1
    
    while sw==1:
            try:
                sueldo3 = float(input("Ingrese sueldo del tercer mes:"))
                if sueldo3> 0:
                    sw=0
                    break
                else:
                    print("El sueldo debe ser un número positivo.")
                   
            except ValueError:
                print("Entrada inválida. Ingrese un número.")


    listaempleados.append([empleado, sueldo1, sueldo2, sueldo3])
    
for i in range (5):
    sueldototal= 0
    
    for j in range (1,4):   
        sueldototal +=listaempleados[i][j]
    print("Empleado: " ,listaempleados[i][0], ". Sueldo total del empleado: $",sueldototal)   

            

        
def puede_votar(edad):
    if edad >=18:
        return"puedes votar"
    else:
         return "no puedes votar aun"
    
    #pedimos la edad al usuario
try:
    edad_usuario = int(input("cual es  tu edad?"))
    print(puede_votar(edad_usuario))
except ValueError:
    print("porfavor ingrese un numero")

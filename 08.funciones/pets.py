#Argumentos posicionales
def describe_pet(animal_type,pet_name):
    #Muestra informacion sobre una mascota
    print(f"\nYo tengo un {animal_type}.")
    print(f"El nombre de mi {animal_type} es {pet_name.title()}")

#Argumentos posicionales
print("-"*80)
print("Resultados de argumentos posicionales")
describe_pet('perro','alacran')
print("-"*80)

#Multiples llamadas a una funcion. puedes llamar varias vaces a la funcion 
print("Resultados de multiples llamadas a una funcion")
describe_pet('gallo','claudio')
describe_pet('perro','boby')

#Argumentos de palabra clave
print("-"*80)
print("Resultados de Argumentos de palabra clave")
describe_pet(animal_type='gato',pet_name='anubis')
print("-"*80)

#valroes predeterminados
def describe_pet(pet_name, animal_type='perro'):
    print(f"\nYo tengo un {animal_type}.")
    print(f"El nombre de mi {animal_type} es {pet_name.title()}")
describe_pet(pet_name='willie')
#la sigueitne linea entrega el mismo resultado 
describe_pet('willie')

#los valores predeterminados ignoran el orden de los argumentos y respeta el orden de los parametros que tiene la funcion
print("-"*80)
print("Resultados que los valores predeterminados a pesar de estar desornados respetan el orden d elos parametros")
describe_pet(pet_name='harry', animal_type='hamster')


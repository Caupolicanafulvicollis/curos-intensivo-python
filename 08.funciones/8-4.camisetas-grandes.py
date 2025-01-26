def hacer_camiseta(size="L",text='Me encanta Python'):
    if size == 'S' or size == 'M':
        text="Me encanta C++"
        print(f"La talla de la camiseta es {size}")
        print(f"La camiseta con talla {size} tiene un texto como '{text.title()}'")
    else:
        print(f"La talla de la camiseta es {size}")
        print(f"La camiseta con talla {size} tiene un texto como '{text.title()}'")        
    
#Argumento predeterminado
print("Resultado del argumento predeterminado")
hacer_camiseta()
print("-"*30)
#Argumentos posicional 
print('Resultado del argumento posicional')
hacer_camiseta('S','Yellowstone')
print("-"*30)
#Argumeto por palabra clave
print('Resultado por palabra clave')
hacer_camiseta(size='S')
hacer_camiseta(size='M')
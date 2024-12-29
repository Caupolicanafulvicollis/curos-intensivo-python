def hacer_camiseta(size,text):
    print(f"La talla de la camiseta es {size}")
    print(f"La camiseta con talla {size} tiene un texto como '{text.title()}'")

#Argumentos posicional 
print('Resultado del argumento posicional')
hacer_camiseta('S','Yellowstone')

#Argumeto por palabra clave
print('Resultado por palabra clave')
hacer_camiseta(size='L',text='Torres del Paine')
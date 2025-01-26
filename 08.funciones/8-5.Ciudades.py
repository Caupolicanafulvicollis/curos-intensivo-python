def describir_ciudad(ciudad="Reykjavík",pais='Islandia'):
    ciudades_islandia = [
    "Reykjavík",        # Capital y ciudad más grande
    "Kópavogur",        # Segunda ciudad más grande
    "Hafnarfjörður",    # Importante puerto pesquero
    "Akureyri",         # Conocida como la capital del norte
    "Reykjanesbær",     # Ubicada cerca del aeropuerto internacional de Keflavík
    "Garðabær",         # Ciudad residencial cerca de Reykjavík
    "Mosfellsbær",      # Famosa por sus áreas verdes
    "Árborg",           # Municipio que incluye Selfoss
    "Egilsstaðir",      # Principal centro en el este de Islandia
    "Ísafjörður",       # Centro urbano en los fiordos occidentales
    "Vestmannaeyjar",   # Archipiélago en el sur de Islandia
    "Húsavík",          # Popular por la observación de ballenas
    "Borgarnes",        # Ciudad histórica en el oeste
    "Seyðisfjörður",    # Ciudad pintoresca con arquitectura nórdica
    "Grindavík",        # Conocida por su proximidad a la Laguna Azul
]
    for ciudad in ciudades_islandia:
        if ciudad in ciudades_islandia:
            print(f"La ciudad de {ciudad.title()} se encuentra en {pais.title()}")
        else:
            print(f"La ciudad de {ciudad.title()} no se encuentra en {pais.title()}")

#Argumento predeterminado
print("Resultado del argumento predeterminado")
describir_ciudad()
print("-"*30)
#Argumentos posicional 
print('Resultado del argumento posicional')
describir_ciudad('Egilsstaðir')
print("-"*30)
#Argumeto por palabra clave
print('Resultado por palabra clave')
describir_ciudad(ciudad='Seyðisfjörður')

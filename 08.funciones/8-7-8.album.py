def hacer_album(name_album, name_artist, last_name_artist='', n_songs=None):
    album={'name': name_artist.title(), 'last': last_name_artist.title(), 'album':name_album.title()}
    if n_songs:
        album['songs']=n_songs
    return album

album1=hacer_album('woodstock','jimi','hendrix',12)
print(album1)
album2=hacer_album('pearl','janis','joplin',10)
print(album2)
album3=hacer_album('the doors','the doors',n_songs=11)
print(album3)

#ejercicio 8-8. Album de usuario
while True: 
    print('Ingrese el nombre de su album: ')
    print("Presione 'q' en cualqueir momento para salir del programa")
    f_name=input("Introduzca su nombre: ")
    if 'q'==f_name:
        break
    l_name=input("")
    f_name=input("Introduzca su apellido: ")
    if 'q'==f_name:
        break
    a_name=input("")
    f_name=input("Introduzca el nombre de su album: ")
    if 'q'==f_name:
        break
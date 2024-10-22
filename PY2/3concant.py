abc= 'a'
xyz= 'b'
star= ''' *
           * 
           * '''
a123= 12
print(abc+xyz)
print(abc,xyz)

print(abc*12)

print(abc+str(a123),star)

#print(len(abc+str(a123),star))



# Definición de variables
titulo_libro = 'Cien años de soledad'
autor_libro = 'Gabriel García Márquez'
descripcion = '''Este libro narra la historia de la familia Buendía 
en el pueblo ficticio de Macondo, explorando temas de soledad, 
poder y el ciclo de la vida.'''
anio_publicacion = 1967
cantidad_paginas = 417

# Mostrar información básica
print("Título:", titulo_libro)
print("Autor:", autor_libro)
print("Descripción:", descripcion)

# Mostrar información adicional
print("Año de publicación:", anio_publicacion)
print("Cantidad de páginas:", cantidad_paginas)

# Concatenación y repetición de cadenas
info_resumida = titulo_libro + " de " + autor_libro
print("\nInformación resumida:", info_resumida)

# Repetir una cadena
estrella = '*'
print("\nEstrellas: ", estrella * 10)

# Mostrar información con un formato
print("\nDetalles del libro:")
print(f"{titulo_libro} ({anio_publicacion}) - {cantidad_paginas} páginas")
print("Descripción breve:", descripcion[:50] + "...")  # Muestra solo los primeros 50 caracteres

# Calcular longitud de la descripción
print("Longitud de la descripción:", len(descripcion))

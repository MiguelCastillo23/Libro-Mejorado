import datetime


class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if not libro.titulo or not libro.autor:
            raise ValueError("El libro debe tener un título y un autor.")
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_libro(self, opcion_busqueda):
        if opcion_busqueda == "1":
            titulo = input("Ingrese el título del libro a buscar: ")
            for libro in self.libros:
                if libro.titulo.lower() == titulo.lower():
                    return libro
            raise ValueError(f"No se encontró ningún libro con el título '{titulo}'.")
        elif opcion_busqueda == "2":
            autor = input("Ingrese el autor del libro a buscar: ")
            for libro in self.libros:
                if libro.autor.lower() == autor.lower():
                    return libro
            raise ValueError(f"No se encontró ningún libro del autor '{autor}'.")
        elif opcion_busqueda == "3":
            año = input("Ingrese el año de publicación del libro a buscar: ")
            for libro in self.libros:
                if str(libro.año_publicacion) == año:
                    return libro
            raise ValueError(f"No se encontró ningún libro publicado en el año '{año}'.")
        elif opcion_busqueda == "4":
            return None
        else:
            raise ValueError("Opción no válida.")

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
            return

        while True:
            print("\nMostrar libros por:")
            print("1. Orden de registro")
            print("2. Alfabéticamente (título)")
            print("3. Año de publicación")
            print("4. Volver al menú principal")

            opcion_mostrar = input("Seleccione una opción: ")
            if opcion_mostrar == "1":
                print("\nLibros en la biblioteca (Orden de registro):")
                for i, libro in enumerate(self.libros, start=1):
                    print(f"{i}. {libro.titulo} (Autor: {libro.autor}, Año: {libro.año_publicacion})")
                break
            elif opcion_mostrar == "2":
                print("\nLibros en la biblioteca (Alfabéticamente por título):")
                libros_ordenados = sorted(self.libros, key=lambda x: x.titulo)
                for i, libro in enumerate(libros_ordenados, start=1):
                    print(f"{i}. {libro.titulo} (Autor: {libro.autor}, Año: {libro.año_publicacion})")
                break
            elif opcion_mostrar == "3":
                print("\nLibros en la biblioteca (Ordenados por año de publicación):")
                libros_ordenados = sorted(self.libros, key=lambda x: x.año_publicacion)
                for i, libro in enumerate(libros_ordenados, start=1):
                    print(f"{i}. {libro.titulo} (Autor: {libro.autor}, Año: {libro.año_publicacion})")
                break
            elif opcion_mostrar == "4":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")


class ErrorLibroSinTitulo(Exception):
    def __init__(self, mensaje="El libro debe tener un título."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ErrorLibroSinAutor(Exception):
    def __init__(self, mensaje="El libro debe tener un autor."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ErrorAñoPublicacionInvalido(Exception):
    def __init__(self, mensaje="El año de publicación debe ser un número entero."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def validar_año(año):
    try:
        año = int(año)
        if año <= 0:
            return False
        now = datetime.datetime.now()
        if año > now.year:
            return False
        return True
    except ValueError:
        return False


def main():
    biblioteca = Biblioteca()

    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Mostrar libros")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")

                while True:
                    año_publicacion = input("Ingrese el año de publicación del libro: ")
                    if validar_año(año_publicacion):
                        break
                    else:
                        print("El año de publicación debe ser un número entero positivo y menor o igual al año actual.")

                libro = Libro(titulo, autor, int(año_publicacion))
                biblioteca.agregar_libro(libro)
            except (ErrorLibroSinTitulo, ErrorLibroSinAutor, ErrorAñoPublicacionInvalido) as e:
                print(e)

        elif opcion == "2":
            print("\nBuscar libro por:")
            print("1. Título del libro")
            print("2. Autor del libro")
            print("3. Año de publicación")
            print("4. Volver al menú principal")

            sub_opcion = input("Seleccione una opción: ")
            try:
                libro_encontrado = biblioteca.buscar_libro(sub_opcion)
                if libro_encontrado:
                    print(
                        f"\nLibro encontrado: {libro_encontrado.titulo} (Autor: {libro_encontrado.autor}, Año: {libro_encontrado.año_publicacion})")
            except ValueError as e:
                print(e)

        elif opcion == "3":
            biblioteca.mostrar_libros()

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()

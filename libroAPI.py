"""
Esta API tiene como objetivo definir la interacción entre lbros almacenados y personas que requieren solicitarlos
por alg'un tiempo en específico
"""

class Libro:
    """Clase que instancia libros
    """
    
    def __init__(self, titulo, autor, ano_publicacion, esta_prestado = False) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.esta_prestado = esta_prestado
        

    def __str__(self) -> str:
        return f"{self.titulo} por {self.autor}, en {self.ano_publicacion}"


class Biblioteca:

    def __init__(self) -> None:
        self.libros = []

    def agregar_libro(self,libro: Libro):
        """ Método que agrega los libros a la biblioteca


        Args:
            libro (Libro): libro agregado
        """
        self.libros.append(libro)
        print(f"Agregado: {libro}")

    def listar_libros(self, disponibles=False):
        for libro in self.libros:
            if disponibles and libro.esta_prestado:
                continue
            print(libro)

    def prestar_libros(self,titulo):
        for libro in self.libros:
            if libro.titulo == titulo and not libro.esta_prestado:
                libro.esta_prestado = True
                print(f"libro prestado: {libro}")

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.esta_prestado = False
                print(f"Libro queda disponible: {libro}")


el_olvido = Libro("El olvido que seremos", "Hector Abad", 1999)
la_cuadra = Libro("La cuadra", "Gilmer Mesa", 2016)

biblioteca = Biblioteca()
biblioteca.agregar_libro(el_olvido)
biblioteca.agregar_libro(la_cuadra)

biblioteca.listar_libros()
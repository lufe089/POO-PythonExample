from src.model.Programa import Programa


class GUIConsola:

    def __init__(self) -> None:
        self.programaObj = Programa();



    def agregar_figura(self):
        opcion = -1
        print(" Figuras disponibles\n")
        print("1. Cuadrado\n")
        print("2. Círculo\n")
        print("0.  Salir \n")
        opcion = int(input(""))
        if opcion == 1:
            print("Ingrese la longitud de un lado del cuadrado \n")
            lado = int(input(""))
            self.programaObj.agregarFigura(lado = lado)
        elif opcion == 2:
            print("Ingrese el radio del círculo \n")
            radio = float(input(""))
            self.programaObj.agregarFigura(radio=radio)

    def dibujar_menu(self):
        opcion = -1
        while (opcion != 0):
            print(" Bienvenido\n")
            print("1. Ver el perimetro de las figuras existentes\n")
            print("2. Suma total de todas las areas de las figuras registradas\n")
            print("3. Dibujar figuras existentes\n")
            print("0.  Salir \n")

            opcion = int(input(""))

            if opcion == 1:
                self.programaObj.mostrar_perimetro_figura()
            elif opcion == 2:
                self.programaObj.mostrar_area_figura()
            elif opcion == 3:
                print("Pendiente")

import os
import sys
import logging
#Class pila
class Pila:
    """
    Clase Pila que contiene los datos de la pila como tal, atributos y métodos.

    """
    def __init__(self):
        """
        Inicializa Pila.
            textos: Lista que contiene los datos de la pila.
            tamano: int que indica la cantidad de elementos que posee la pila.
            indice_mas_largo: int que indica el indice del texto mas largo de la pila.
            largo_mas_largo: int que indica el largo del texto más largo de la pila.
            indice_mas_corto: int que indica el indice del texto más corte de la pila.
            largo_mas_corto: int que indica el largo del texto más corto de la pila
        """
        try:
            self.textos = []
            self.tamano = 0
            self.indice_mas_largo = -1
            self.largo_mas_largo = -1
            self.indice_mas_corto = -1
            self.largo_mas_corto = 999999
        except:
            logging.error("Error al inciar pila. %s. %s.", sys.exc_info()[0].  sys.exc_info()[1])
            logging.info("Ejecución terminada.")
            sys.exit(1)

    def push(self, x):
        """
        Recibe un elemento x y lo inserta el final de la lista (pila).
        Actualiza si es necesario las variables: largo_mas_largo, indice_mas_largo, indice_mas_corto, largo_mas_corto.

        """
        try:
            self.textos.append(x)
            logging.info("Texto: \"%s\" agregado a la pila.", x)
            self.tamano += 1
            logging.debug("Tamaño de pila aumentado a %2d.", self.tamano)
            logging.debug("Elementos de la pila [{}] ".format(','.join(self.textos)))
            largo = len(x)
            if (self.largo_mas_largo < largo):
                self.indice_mas_largo = self.tamano - 1
                self.largo_mas_largo = largo
                logging.debug("Texto mas largo actualizado al de indice %2d", self.indice_mas_largo)
            if (self.largo_mas_corto > largo):
                self.indice_mas_corto = self.tamano - 1
                self.largo_mas_corto = largo
                logging.debug("Texto mas corto actualizado al de indice %2d", self.indice_mas_corto)
        except:
            logging.error("Error al agregar texto a la pila. %s. %s", sys.exc_info()[0],  sys.exc_info()[1])
            logging.info("Ejecución terminada.")
            sys.exit(1)



    def puchnt(self):
        """
        Elimina el último elemento de la lista (pila).
        Si es necesario actualiza variables.
        Retorna el texto eliminado si existe.
        """
        try:
            if(self.tamano > 0):
                texto_popeado = self.textos.pop()
                logging.info("Texto: \"%s\" desapilado.", texto_popeado)
                logging.debug("Elementos de la pila [{}] ".format(','.join(self.textos)))
                self.tamano -= 1
                if(self.indice_mas_largo == self.tamano): #el texto popeado era el mas largo -> actualizar mas largo
                    self.indice_mas_largo = -1
                    self.largo_mas_largo = -1
                    if (self.tamano > 0): #para asegurarse que existen elementos en la pila
                        for i, texto in enumerate(self.textos):
                            largo = len(texto)
                            if(self.largo_mas_largo < largo):
                                self.largo_mas_largo = largo
                                self.indice_mas_largo = i
                        logging.debug("Texto más largo actualizado al de indice %2d", self.indice_mas_largo)
                if(self.indice_mas_corto == self.tamano): #texto popeado era el mas corto
                    self.indice_mas_corto = -1
                    self.largo_mas_corto = 999999
                    if(self.tamano > 0):
                        for i, texto in enumerate(self.textos):
                            largo = len(texto)
                            if(self.largo_mas_corto > largo):
                                self.largo_mas_corto = largo
                                self.indice_mas_corto = i
                        logging.debug("Texto más corto actualizado al de indice %2d", self.indice_mas_corto)
                return texto_popeado

            else:
                return "Pila está vacía."
        except:
            logging.error("Error al desapilar texto a la pila. %s. %s", sys.exc_info()[0],  sys.exc_info()[1])
            logging.info("Ejecución terminada.")
            sys.exit(1)

    def get_size(self):
        """
        Retorna la cantidad de elementos de la pila.
        """
        try:
            return self.tamano
        except:
            logging.error("Error al obtener tamaño de la pila. %s. %s", sys.exc_info()[0],  sys.exc_info()[1])
            logging.info("Ejecución terminada.")
            sys.exit(1)

    def get_mas_largo(self):
        """
        Retorna el texto más largo de la pila.
        """
        try:
            if(self.tamano>0):
                logging.info("Texto mas largo retornado. Indice: %2d", self.indice_mas_largo)
                return self.textos[self.indice_mas_largo]
            else:
                logging.debug("Texto más largo no existente")
                return None
        except:
            logging.error("Error al obtener el texto más largo. %s. %s", sys.exc_info()[0],  sys.exc_info()[1])
            logging.info("Ejecución terminada.")
            sys.exit(1)
    
    def get_mas_corto(self):
        """
        Retorna el texto más corto de la pila.
        """
        try:
            if(self.tamano>0):
                logging.info("Texto mas corto retornado. Indice: %2d", self.indice_mas_corto)
                return self.textos[self.indice_mas_corto]
            else:
                logging.debug("Texto más corto no existente")
                return None
        except:
            logging.error("Error al obtener el texto más corto. %s. %s", sys.exc_info()[0],  sys.exc_info()[1])
            logging.info("Ejecución terminada.")
            sys.exit(1)
    
    def get_any_texto(self, i):
        """
        Retorna el texto del indice i
        """
        try:
            i -= 1 #el elemento n está en la posición n-1.
            if(self.tamano > i and i > -1):
                logging.info("Texto número %2d, de indice %2d retornado", i+1, i)
                return self.textos[i]
            else:
                logging.debug("Texto número %2d de indice %2d no existente", i+1, i)
                return None
        except:
            logging.error("Error al obtener cualquier texto. %s. %s", sys.exc_info()[0],  sys.exc_info()[1])
            logging.info("Ejecución terminada.")
            sys.exit(1)


logging.basicConfig(filename="logging.log", format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', level = logging.DEBUG)
logging.info('Programa iniciado.')
pila_textos = Pila()
logging.debug('Pila iniciada.')

input_menu = -1

while (input_menu != 9):
    print("\t¡Menú principal de pila para Textos!\n")
    print("\tIngresa el número de la opción correspondiente\n")
    print("\t1. Apilar texto")
    print("\t2. Desapilar texto")
    print("\t3. Obtener texto más largo y más corto")
    print("\t4. Obtener cualquier texto")
    print("\t5. Comparar tamaños")
    print("\t9. Salir\n")
    try:
        input_menu = int(input("\tOpcion: "))
        logging.debug("Valor ingresado es del tipo correcto (int).")
    except:
        logging.debug("Valor ingresado es del tipo incorrecto. %s. %s",  sys.exc_info()[0],  sys.exc_info()[1])
        input_menu = -1

    #opcion 1. Apilar Texto
    if(input_menu == 1):
        logging.info("Se ingresó la opción número %2d. Apilar texto.", input_menu)
        os.system('cls')
        print("\tIngresa texto para apilar:\n")
        texto = input("\t")
        if(texto == ""):
            logging.debug("Se ingresó texto vacío como input. No permitido.")
            print("\tTexto vacío no permitido.")
        else:
            pila_textos.push(texto)
            os.system('cls')
            print("\tTexto apilado exitosamente.\n")
    
    #opcion 2. Desapilar texto
    elif(input_menu == 2):
        os.system('cls')
        logging.info("Se ingresó la opción número %2d. Desapilar texto.", input_menu)
        print(pila_textos.puchnt())

    #opcion 3. Obtener texto mas largo y mas corto
    elif(input_menu == 3):
        logging.info("Se ingresó la opción número %2d. Obtener texto más largo y más corto.", input_menu)
        os.system('cls')
        if(pila_textos.get_size() > 0):
            texto_mas_largo = pila_textos.get_mas_largo()
            texto_mas_corto = pila_textos.get_mas_corto()
            print("\tTexto más largo, de tamaño ", len(texto_mas_largo), ":")
            print(texto_mas_largo)
            print("\n\tTexto más corto, de tamaño ", len(texto_mas_corto), ":")
            print(texto_mas_corto)
            logging.info("Se retornaron los textos más largo y más corto.")
        else:
            logging.info("No se retornó ningún texto. Pila vacía.")
            print("\tLa Pila está vacía.\n")
        print("\tAprete ENTER para continuar.")
        input_aux = input()
        os.system('cls')

    #opcion 4. Obtener cualquier texto
    elif(input_menu == 4):
        logging.info("Se ingresó la opción número %2d. Obtener cualquier texto.", input_menu)
        os.system('cls')
        if(pila_textos.get_size() > 0):
            print("\tLa pila contiene %2d texto(s). Ingrese un número entero desde el 1 hasta el %2d para obtener el texto." %(pila_textos.get_size(), pila_textos.get_size()))
            try:
                indice = int(input("\tTexto número: "))
                logging.debug("Valor ingresado es del tipo correcto (int).")
                texto_i = pila_textos.get_any_texto(indice)
                if(texto_i):
                    print(texto_i)
                else:
                    print("\tTexto número ", indice, " no existe.")
            except:
                logging.debug("Valor ingresado es del tipo incorrecto. %s. %s",  sys.exc_info()[0],  sys.exc_info()[1])
                print("\tEntrada no es válida.")
        else:
            logging.info("No se retornó ningún texto. Pila vacía.")
            print("\tLa Pila está vacía.")
        print("\tAprete ENTER para continuar.")
        input_aux = input()
        os.system('cls')

    #Opcion 5. Comparar Tamaños
    elif(input_menu ==5):
        logging.info("Se ingresó la opción número %2d. Comparar tamaños.", input_menu)
        os.system('cls')
        if(pila_textos.get_size() > 0):
            print("\tLa pila contiene %2d texto(s). Ingrese dos números enteros, desde el 1 hasta el %2d para comparar los textos ." %(pila_textos.get_size(), pila_textos.get_size()))
            try:
                indice_1 = int(input("\tTexto 1, número: "))
                logging.debug("Se ingresó valor del tipo correcto (int).")
                texto_1 = pila_textos.get_any_texto(indice_1)
                if(texto_1):
                    try:
                        indice_2 = int(input("\tTexto 2, número: "))
                        logging.debug("Se ingresó valor del tipo correcto (int).")
                        texto_2 = pila_textos.get_any_texto(indice_2)
                        if(texto_2):
                            largo_1 = len(texto_1)
                            largo_2 = len(texto_2)
                            os.system('cls')
                            print("\tEl texto elegido 1 es de largo: ", largo_1)
                            print(texto_1)
                            print("\n\tEl texto elegido 2 es de largo: ", largo_2)
                            print(texto_2)
                            if(largo_1 > largo_2):
                                print("\n\tEl texto 1 (número: ", indice_1, ") es más largo que el texto 2 (número: ", indice_2, ").")
                                logging.info("Se indica que el texto de largo %2d es más largo que el texto de largo %2d.", largo_1, largo_2)
                            elif(largo_1 < largo_2):
                                print("\n\tEl texto 2 (número: ", indice_2, ") es más largo que el texto 1 (número: ", indice_1, ").")
                                logging.info("Se indica que el texto de largo %2d es más largo que el texto de largo %2d.", largo_2, largo_1)
                            else:
                                print("\n\tAmbos textos tienen el mismo largo.")
                                logging.info("Se indica que el texto de largo %2d es igual de largo que %2d.", largo_1, largo_2)
                        else:
                            print("No existe el texto número ", indice_2)
                    except:
                        logging.debug("Valor ingresado es del tipo incorrecto. %s. %s",  sys.exc_info()[0],  sys.exc_info()[1])
                        print("\tEntrada incorrecta para texto 2.")
                else:
                    print("No existe el texto de número ", indice_1)
            except:
                logging.debug("Valor ingresado es del tipo incorrecto. %s. %s",  sys.exc_info()[0],  sys.exc_info()[1])
                print("\tEntrada incorrecta para texto 1")
        else:
            logging.info("No se comparó ningún texto. Pila vacía.")
            print("La Pila está vacía.")
        print("\tAprete ENTER para continuar.")
        input_aux = input()
        os.system('cls')

    #opcion 9. Salir
    elif(input_menu == 9):
        logging.info("Se ingresó la opción número %2d. Salir.", input_menu)
        os.system('cls')
        print("\tSaliendo")
    else:
        logging.info("Se ingresó la opción número %2d. No existente o valor incorrecto (-1).", input_menu)
        os.system('cls')
        print("Opción no válida.")


logging.info("Ejecución terminada")
            

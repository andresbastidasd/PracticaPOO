class Paciente: #Clase o molde 
    def __init__(self): #constructor 
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
              
    #metodos get, permiten visualizar datos, además estas funciones retornan datos 
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 
    # metodos set, permiten modificar y/o asignar datos, estas funciones no retornan datos, solo los actualiza
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarServicio(self,s):
        self.__servicio = s 
        
class Sistema:    #Clase o molde 
    def __init__(self):
        self.__lista_pacientes = [] #En esta lista se guardan los pacientes 
        
    def verificarPaciente(self,cedula): #Se verifica que este el paciente pidiendo su documento y haciendo un ciclo 
        if cedula != '' :
            for p in self.__lista_pacientes:
                if cedula == p.verCedula():
                    return True 
            return False
        elif cedula == '' :
            for p in self.__lista_pacientes:
                if cedula == p.verNombre():
                    return True
            return False 
        
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac) #Se agrega el paciente a la lista 
        return True
    
    def verDatosPaciente(self, c):
        if c != '' :
            if self.verificarPaciente(c) == False: #polimorfismo 
                return None
            for p in self.__lista_pacientes: #Busca en la lista de pacientes 
                #retorne la cedula y la comparo con la ingresada por teclado
                if c == p.verCedula(): #polimorfismo
                    return p #si encuentro el paciente lo retorno
        elif c == '' :
            if self.verificarPaciente(c) == False: #polimorfismo 
                return None
            for p in self.__lista_pacientes: #Busca en la lista de pacientes 
                #retorne la cedula y la comparo con la ingresada por teclado
                if c == p.verNombre(): #polimorfismo
                    return p #si encuentro el paciente lo retorno
        
                
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 
    

def main():
    sis = Sistema() 
    #probemos lo que llevamos programado
    while True:
        #Menú
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente\n\t--> ")) 
        
        if opcion == 1:
            #ingreso pacientes
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)     #Polimorfismo         
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            #1. solicito la cedula que quiero buscar
            c = int(input("Ingrese la cedula a buscar: ")) 
            #le pido al sistema que me devuelva en la variable p al paciente que tenga
            #la cedula c en la lista
            p = sis.verDatosPaciente(c) #Polimorfismo 
            #2. si encuentro al paciente imprimo los datos
            if p != None:
                print("Nombre: " + p.verNombre()) 
                print("Cedula: " + str(p.verCedula())) 
                print("Genero: " + p.verGenero()) 
                print("Servicio: " + p.verServicio()) 
            else:
                print("No existe un paciente con esa cedula") 
        elif opcion !=0:
            continue 
        else:
            break 

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 
        
        
        
        
        
        
        
        

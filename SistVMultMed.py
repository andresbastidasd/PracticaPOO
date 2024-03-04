import datetime #Importo datetime para usar fechas 
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    #Métodos get
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    #Métodos set 
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    def __init__(self):
        self.__canino = {} #Se guarda en diccionario solo caninos
        self.__felino = {} #Se guarda en diccionario solo felinos
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]

    #Métodos get   
            
    def verCanino(self,c):
        return self.__canino.get(c)
    def verFelino(self,f):
        return self.__felino.get(f)
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 

    #Métodos set      
    def asignarCanino(self,n):
        self.__canino[n.verFecha()]=n
    def asignarFelino(self,n):
        self.__felino[n.verFecha()]=n
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.verFecha = datetime.datetime.now().strftime("%x")
    
    def verificarExiste(self,historia): #Métodos get
        for m in self.__lista_mascotas:
            if historia == m.verHistoria(): #Polimorfismo 
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
    
    #Verifica si existe el medicamento 
    def verificarExisteM(self,nombreM): #Métodos get
        med = Mascota() 
        for n in med.__lista_medicamentos: 
            if nombreM == n.verLista_Medicamentos():
                return True
        return False 
        
    def verNumeroMascotas(self):  #Métodos get
        can = Mascota()
        return str(len(can.__canino)) + str(len(can.__felino))
    
    def ingresarCanino(self,canino):  #Métodos set 
        cf = Mascota()
        cf.__canino(canino)

    def ingresarFelino(self,felino):  #Métodos set 
        cf = Mascota()
        cf.__felino(felino)

    def verFechaIngresof(self,felino):  #Métodos get
        cf = Mascota()
        #busco la mascota y devuelvo el atributo solicitado
        for masc in cf.__felino:
            if felino == masc.verHistoria():
                return masc.verFecha() 
        return None
    
    def verFechaIngresoc(self,canino):  #Métodos get
        cf = Mascota()
        #busco la mascota y devuelvo el atributo solicitado
        for masc in cf.__canino:
            if canino == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamentoc(self,canino):  #Métodos get
        #busco la mascota y devuelvo el atributo solicitado
        cf= Mascota()
        for masc in cf.__canino:
            if canino == masc.verHistoria():
                return masc.verCanino() 
        return None
    
    def verMedicamentof(self,felino):  #Métodos get
        #busco la mascota y devuelvo el atributo solicitado
        cf= Mascota()
        for masc in cf.__felino:
            if felino == masc.verHistoria():
                return masc.verFelino() 
        return None
    
    def eliminarMascotaf(self, felino):  #Métodos set 
        cf= Mascota()
        for masc in cf.__felino:
            if felino == masc.verHistoria():
                cf.__felino.pop(masc)  #polimorfismo 
                return True  #eliminado con exito
        return False 
    
    def eliminarMascotafc(self, canino):  #Métodos set 
        cf= Mascota()
        for masc in cf.__canino:
            if canino == masc.verHistoria():
                cf.__canino.pop(masc)  #polimorfismo 
                return True  #eliminado con exito
        return False 

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False: #Polimorfismo 
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    if servicio_hospitalario.verificarExisteM(nombre_medicamentos):
                        print("\n<< Ya existe un medicamento con ese nombre >>".upper())
                    else:
                        dosis =int(input("Ingrese la dosis: "))
                        medicamento = Medicamento() #Herencia 
                        medicamento.asignarNombre(nombre_medicamentos)
                        medicamento.asignarDosis(dosis)
                        lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q)  #Polimorfismo 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                


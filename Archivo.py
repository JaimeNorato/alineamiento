class Archivo:

    def __init__(self,dir=""):
        self.dir=dir

    # abre el archivo espesificad
    def abrir(self):
        archivo=False
        try:
            archivo=open(self.dir,"r")
        except:
            print("Error al abrir el archivo ")

        return archivo

    #cierra el archivo espesificado
    def cerrar(self,archivo):
        archivo.close()

    #lee y retorna el contenido de un archvo especificad
    def leer(self):
        self.data=""
        archivo=self.abrir()
        if archivo:
            self.data=archivo.readlines()
            self.cerrar(archivo)
        return self

    #retorna el contenido del archivo como estring
    def toString(self):
        return self.data

    #retorna el string de la linea espesificada como un array
    def toArray(self,index=0):
        return list('0'+self.data[index].replace('\n',''))
#
#
# arch=Archivo("adn2.txt")
#
# dat=arch.leer().toArray()
# print('toString',dat)
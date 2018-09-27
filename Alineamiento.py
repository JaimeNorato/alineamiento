from Archivo import Archivo

class Alineamiento:

    def __init__(self):
        self.archivo=Archivo("adn1.txt")
        self.cargarData()
        self.matrizScore=dict({# a
            "AA":10,"AG":-1,"AC":-3,"AT":-4,
            # g
            "GA":-1,"GG":7,"GC":-5,"GT":-3,
            # c
            "CA":-3,"CG":-5,"CC":9,"CT":0,
            # t
            "TA":-4,"TG":-3,"TC":0,"TT":8,});

    #carga el archivo a memoria
    def cargarData(self):
        self.data=self.archivo.leer()

    #carga la secuencia de adn indecada dentro de un archivo
    def cargarSecuencia(self,index=0):
        return self.data.toArray(index)

    #crea la matriz con las dos cadenas de adn, que permitira el alineamiento
    def preAlineamineto(self):
        self.matrizParcial={}
        secuenciaX=self.cargarSecuencia(0)
        secuenciaY=self.cargarSecuencia(1)
        cerosX=0
        cerosY=0
        for value in secuenciaY:
            # agrega columna 0 en Y
            if not value + "0" in self.matrizParcial:
                cerosY+=-5
                self.matrizParcial[value + "0"] = cerosY
            #agrega valores en x segun la pocision y
            for item in secuenciaX:
                # agrega columna 0 en X
                if not "0"+item in self.matrizParcial:
                    cerosX+=-5
                    self.matrizParcial["0"+item]=cerosX

                #peso de la combinacion
                    # self.matrizParcial[value+item]=self.matrizScore[value+item]


alin=Alineamiento()
alin.preAlineamineto()
print(alin.matrizParcial)
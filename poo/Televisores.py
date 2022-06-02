from Aparato import Aparato
class Televisor(Aparato):
    __tipoPantalla=""
    __pulgadas=""
    __tipoDefinicion=""
    __conexion=""

    def __init__(self, marca, modelo, color, pf, precio, tp,pulgadas,td,conexion):
        super().__init__(marca, modelo, color, pf, precio)
        self.__tipoPantalla= tp
        self.__pulgadas= pulgadas
        self.__tipoDefinicion= td
        self.__conexion=""

    
    def getTipoP(self):
        return self.__tipoPantalla
    
    def getPulgadas(self):
        return self.__pulgadas
    
    def getTipoD(self):
        return self.__tipoDefinicion
    
    def getConexion(self):
        return self.__conexion
    



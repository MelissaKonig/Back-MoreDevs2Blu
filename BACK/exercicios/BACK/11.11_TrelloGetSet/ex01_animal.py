class Animal():
    def __init__(self, especie, raca, porte, cor):
        self.__especie = especie
        self.__raca = raca
        self.__porte = porte
        self.__cor = cor

    @property
    def especie(self):
        return self.__especie
    @especie.setter
    def especie(self, especie):
        self.__especie = especie
        
    @property
    def raca(self):
        return self.__raca
    @raca.setter
    def raca(self, raca):
        self.__raca = raca
        
    @property
    def porte(self):
        return self.__porte
    @porte.setter
    def porte(self, porte):
        self.__porte = porte
        
    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, cor):
        self.__cor = cor
        
    def __str__(self):
        return f'Especie: {self.especie}\nRaça: {self.raca}\nPorte: {self.porte}\nCor: {self.cor}.'
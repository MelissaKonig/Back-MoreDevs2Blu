class Conta:
    __titular = ''
    __numero = 0
    __saldo = 0
    
@property
def titular(self):
    return self.__titular
@titular.setter
def titular(self, __titular):
    self.__titular = __titular
    
@property
def numero(self):
    return self.__numero
@numero.setter
def numero(self, __numero):
    self.__numero = __numero
    
@property
def saldo(self):
    return self.__saldo
@saldo.setter
def saldo(self, __saldo):
    self.__saldo = __saldo
    
    
def __str__(self): #def = define (metodo único de python)
        return f'O número da conta é {self.__titular}, o titular é {self.__numero}e o saldo é {self.__saldo}'
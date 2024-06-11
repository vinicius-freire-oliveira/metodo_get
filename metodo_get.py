# Define a classe Conta
class Conta:
    # Método construtor para inicializar os atributos numero, titular, saldo e limite
    def __init__(self, numero, titular, saldo, limite):
        # Imprime uma mensagem indicando que um objeto está sendo construído
        print("Construindo objeto ...{}".format(self))
        # Atributo privado __numero para armazenar o número da conta
        self.__numero = numero
        # Atributo privado __titular para armazenar o titular da conta
        self.__titular = titular
        # Atributo privado __saldo para armazenar o saldo da conta
        self.__saldo = saldo
        # Atributo privado __limite para armazenar o limite da conta
        self.__limite = limite

    # Método para exibir o extrato da conta
    def extrato(self):
        # Imprime o saldo e o titular da conta
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    # Método para realizar um depósito na conta
    def deposita(self, valor):
        # Adiciona o valor ao saldo da conta
        self.__saldo += valor

    # Método para realizar um saque na conta
    def saca(self, valor):
        # Subtrai o valor do saldo da conta
        self.__saldo -= valor

    # Método para transferir um valor para outra conta
    def transfere(self, valor, destino):
        # Realiza um saque na conta atual
        self.saca(valor)
        # Realiza um depósito na conta destino
        destino.deposita(valor)

    # Método getter para obter o saldo da conta
    def get_saldo(self):
        return self.__saldo

    # Método getter para obter o titular da conta
    def get_titular(self):
        return self.__titular

# Cria uma instância da classe Conta com os parâmetros especificados
conta = Conta(121, "Tadeu", 100.0, 1000.0)

# Obtém e imprime o saldo atual da conta usando o método get_saldo
saldo_atual = conta.get_saldo()
print(saldo_atual)

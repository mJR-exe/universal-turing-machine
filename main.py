class MTU(object):
    def __init__(self, fita="", branco=" ", estadoInicial="", estadoFinal=None, execTransicao=None):
        self.__fita = Fita(fita)
        self.__posCabeca = 0
        self.__branco = branco
        self.__estadoAtual = estadoInicial
        if execTransicao == None:
            self.__execTransicao = {}
        else:
            self.__execTransicao = execTransicao
        if estadoFinal == None:
            self.__estadoFinal = set()
        else:
            self.__estadoFinal = set(estadoFinal)

    def getFita(self):
        return str(self.__fita)

    def prox(self):
        cabecaAux = self.__fita[self.__posCabeca]
        x = (self.__estadoAtual, cabecaAux)
        if x in self.__execTransicao:
            y = self.__execTransicao[x]
            self.__fita[self.__posCabeca] = y[1]
            if y[2] == "R":
                self.__posCabeca += 1
            elif y[2] == "L":
                self.__posCabeca -= 1
            self.__estadoAtual = y[0]

    def final(self):
        if self.__estadoAtual in self.__estadoFinal:
            return True
        else:
            return False


class Fita(object):
    branco = " "

    def __init__(self,
                 palavra=""):
        self.__fita = dict((enumerate(palavra)))

    def __str__(self):
        s = ""
        minimo = min(self.__fita.keys())
        maximo = max(self.__fita.keys())
        for i in range(minimo, maximo):
            s += self.__fita[i]
        return s

    def __getitem__(self, index):
        if index in self.__fita:
            return self.__fita[index]
        else:
            return Fita.branco

    def __setitem__(self, pos, char):
        self.__fita[pos] = char


estadoInicial = "init",
accepting_states = ["final"],
execTransicao = {("init", "0"): ("init", "1", "R"), ("init", "1"): (
    "init", "0", "R"), ("init", " "): ("final", " ", "N")}
estadoFinal = {"final"}
entrada = input("Digite a entrada do número a ser calculado pela MTU: ")


t = MTU(entrada, estadoInicial="init",
        estadoFinal=estadoFinal, execTransicao=execTransicao)

print("\nEntrada:\n" + t.getFita())

while not t.final():
    t.prox()

print("Saída:")
print(t.getFita())

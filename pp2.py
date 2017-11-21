from copy import copy

class Matriz:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.celulas = [colunas*[0] for i in range(linhas)]

    def __str__(self):
        return "\n".join([str(linha) for linha in self.celulas])

    def set_celulas(self, celulas):
        self.celulas = celulas
        self.linhas = len(celulas)
        self.colunas = len(celulas[0])

    def transpoe(self):
        self.set_celulas(list(map(list, zip(*self.celulas))))

    def multiplica(self, outra):
        celulas = [outra.colunas*[0] for i in range(self.linhas)]
        for i in range(self.linhas):
            for j in range(outra.colunas):
                for k in range(self.colunas):
                    celulas[i][j] += self.celulas[i][k]*outra.celulas[k][j]
        self.set_celulas(celulas)


class AFD:
    # estados: quantidade de estados
    # alfabeto: quantidade de simbolos
    # delta: matriz estados por alfabeto
    # inicial: inteiro
    # finais: lista de inteiros
    def __init__(self, tupla):
        self.estados = tupla[0]
        self.alfabeto = tupla[1]
        self.delta = tupla[2]
        self.inicial = tupla[3]
        self.finais = tupla[4]

    def gera_pi(self):
        pi = Matriz(self.estados, 1)
        pi.celulas[self.inicial][0] = 1
        return pi

    def gera_eta(self):
        eta = Matriz(self.estados, 1)
        for final in self.finais:
            eta.celulas[final][0] = 1
        return eta

    def gera_curry(self):
        curry = [Matriz(self.estados, self.estados) for simbolo in range(self.alfabeto)]
        for simbolo in range(self.alfabeto):
            for estado in range(self.estados):
                curry[simbolo].celulas[estado][self.delta[estado][simbolo]] = 1
        return curry

    def le_palavra(self, palavra):
        resultado = self.gera_pi()
        resultado.transpoe()
        curry = self.gera_curry()
        for simbolo in palavra:
            resultado.multiplica(curry[simbolo])
        resultado.multiplica(self.gera_eta())
        return resultado.celulas[0][0]


def main():
    representacao_do_afd = eval(input())
    alfabeto = 2
    tupla = [
        representacao_do_afd['estados'],
        alfabeto,
        representacao_do_afd['delta'],
        representacao_do_afd['inicial'],
        representacao_do_afd['final']]

    A = AFD(tupla)

    qtd_palavras = int(input())
    for i in range(qtd_palavras):
        palavra = [ord(simbolo)-ord('a') for simbolo in input().rstrip('\r')]
        print("ACEITA" if A.le_palavra(palavra) else "REJEITA")

if __name__ == '__main__':
    main()

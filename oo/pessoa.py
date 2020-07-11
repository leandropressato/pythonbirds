class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Leandro', 20)
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
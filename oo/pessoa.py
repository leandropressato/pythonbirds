class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    leandro = Pessoa(nome='Leandro')
    luciano = Pessoa(leandro, nome='Luciano')
    for filho in luciano.filhos:
        print(filho.nome)
    del luciano.filhos
    Pessoa.olhos = 4
    luciano.olhos = 1
    del luciano.olhos
    luciano.sobrenome = 'Estevam'
    print(luciano.__dict__)
    print(id(Pessoa.olhos), id(luciano.olhos), id(leandro.olhos))


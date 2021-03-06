class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é  {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mao'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    leandro = Homem(nome='Leandro')
    luciano = Pessoa(leandro, nome='Luciano')
    for filho in luciano.filhos:
        print(filho.nome)
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    luciano.sobrenome = 'Estevam'
    print(luciano.__dict__)
    print(id(Pessoa.olhos), id(luciano.olhos), id(leandro.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())

    pessoa=Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(leandro.cumprimentar())
    print(luciano.cumprimentar())


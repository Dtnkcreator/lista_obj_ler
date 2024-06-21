class Lista_pega:
    def __init__(self, nome_, idade_, peso_):
        self.nome = nome_
        self.idade = idade_
        self.peso = peso_

    def __repr__(self):
        return f"Pessoa: Nome: {self.nome} ; Idade: {self.idade} ; Peso: {self.peso}"
        
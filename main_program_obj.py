from suporte_lista_class import Lista_pega

def ler_pessoa():
    lista_das_pessoas = []
    with open('lista_obj_ler/textinho.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
                if line.startswith('Pessoa: '):
                    atributos =line.split('Pessoa: ')[1]
                    nome = atributos.split(':')[1].split(';')[0]
                    idade = atributos.split(':')[2].split(';')[1]
                    peso = atributos.split(':')[3]

                    pessoa1 = Lista_pega(nome,idade,peso)
                    lista_das_pessoas.append(pessoa1)
        return lista_das_pessoas
    
pessoa = ler_pessoa()
print(pessoa)
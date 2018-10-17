# Classe para criação dos Vértices
class Vertice:
    def __init__(self, end_x, end_y):
        self.end_x = end_x  # Endereço de X
        self.end_y = end_y  # Endereço de Y

    # Viadagem de Python pra retorno de String, não funciona com __str__ não sei o motivo
    def __repr__(self):
        return f"[{self.end_x},{self.end_y}]"

    # Outra viadagem de Python dessa vez para fazer comparações (ESSA EU ENTENDI)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.end_x == other.end_x and self.end_y == other.end_y
        return False


# Classe para criação de Arestas
class Aresta:
    def __init__(self, a, b):
        self.origem = a
        self.destino = b

    def __repr__(self):
        return f'({self.origem},{self.destino})'


# Arquivo .txt para guardar as informações
# todo ler o arquivo ao inicializar o programa
db = open("database.txt", "r+")
db.write("Vértices\n")

vertices = []  # Lista de vértices criados
create = True
while create:  # Criação/ligação de vértices enquanto a função estiver ativa todo a porra do menu
    v = Vertice(input("X: "), input("Y: "))  # todo trocar input teclado por input mouse
    if len(vertices) < 2:
        vertices.append(v)
    if v in vertices:
        create = False
        break
    vertices.append(v)

db.write(f"{vertices}")  # Salvando no arquivo
db.close()  # Fechando o arquivo
print(f"Vértices: {vertices}")  # Teste inútil

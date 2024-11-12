# Base de conhecimento - Bar
bebidas = {
    "cerveja": "alcoolica",
    "cachaça": "alcoolica",
    "agua": "nao_alcoolica",
    "refrigerante": "nao_alcoolica"
}

clientes = {
    "Diva": 25,
    "Ari": 17,
    "Pierre": 30
}

pedidos = [
    ("Diva", "cerveja"),
    ("Ari", "agua"),
    ("Pierre", "cachaça"),
    ("Ari", "cerveja")
]

# Fatos: Função maior de idade
def maior_de_idade(nome):
    return clientes.get(nome, 0) >= 18

# Função pode comsumir
def pode_consumir(nome, bebida):
    tipo_bebida = bebidas.get(bebida, "")
    if tipo_bebida == "nao_alcoolica":
        return True
    elif tipo_bebida == "alcoolica" and maior_de_idade(nome):
        return True
    return False

# Regras: Função se pedido é válido
def pedido_valido(nome, bebida):
    if (nome, bebida) in pedidos and pode_consumir(nome, bebida):
        return True
    return False

# Verificar pedidos válidos
print("Pedidos válidos:")
for nome, bebida in pedidos:
    if pedido_valido(nome, bebida):
        print(f"{nome} Pode consumir {bebida}")
    else:
        print(f"{nome} NÃO pode consumir {bebida}")

print('Beba com moderação')
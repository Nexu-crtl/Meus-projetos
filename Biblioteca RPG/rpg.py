import random  # CORRIGIDO: movido para o topo

personagem = {
    "nome": "Gandalf",
    "classe": "Mago",
    "nivel": 1,
    "vida": 10,
    "vida_max": 10,
    "mana": 10,
    "xp": 0,
    "xp_proximo_nivel": 50
}


item_1 = {"nome": "Espada Longa", "tipo": "Arma", "dano": 15, "quantidade": 1}
item_2 = {"nome": "Poção de Cura", "tipo": "Consumível", "cura": 20, "quantidade": 3}
item_3 = {"nome": "Armadura de Couro", "tipo": "Armadura", "defesa": 5, "quantidade": 1}


inventario = [item_1, item_2, item_3]

# CORRIGIDO: movido para antes do menu
monstros = [
    {"nome": "Goblin", "vida": 30, "dano": 5, "dano-max": 10, "xp": 20},
    {"nome": "Orc", "vida": 50, "dano": 10, "dano-max": 20, "xp": 50},
    {"nome": "Troll", "vida": 80, "dano": 15, "dano-max": 30, "xp": 100}]


def mostrar_ficha(personagem):
    print(f"=== {personagem['nome']} | {personagem['classe']} | Nível {personagem['nivel']} ===")
    print(f"Vida: {personagem['vida']}/{personagem['vida_max']} | Mana: {personagem['mana']}")
    print(f"XP: {personagem['xp']}/{personagem['xp_proximo_nivel']}")  # MELHORIA: mostra o XP na ficha


def mostrar_inventario(inventario):
    print("\n=== Inventário ===")
    for posicao, item in enumerate(inventario, start=1):
        print(f"{posicao}. {item['nome']} (Tipo: {item['tipo']}, Quantidade: {item['quantidade']})")


def usar_pocao(personagem, inventario):
    for item in inventario:
        if item["nome"] == "Poção de Cura" and item["quantidade"] > 0:
            personagem["vida"] = min(personagem["vida"] + item["cura"], personagem["vida_max"])
            item["quantidade"] -= 1      # diminui 1 poção
            print(f"Você usou uma poção! Vida: {personagem['vida']}/{personagem['vida_max']}")
            return
    print("Você não tem poções!")


def subir_nivel(personagem):
    while personagem["xp"] >= personagem["xp_proximo_nivel"]:
        personagem["nivel"] += 1
        personagem["vida_max"] += 10
        personagem["vida"] = personagem["vida_max"]
        personagem["mana"] += 5
        personagem["xp"] -= personagem["xp_proximo_nivel"]
        personagem["xp_proximo_nivel"] = int(personagem["xp_proximo_nivel"] * 1.5)
        print(f"🎉 Parabéns! Você subiu para o nível {personagem['nivel']}!")
        print(f"Vida máxima aumentada para {personagem['vida_max']}. Mana aumentada para {personagem['mana']}.")


def ganhar_xp(personagem, xp):
    personagem["xp"] += xp
    print(f"Você ganhou {xp} pontos de experiência!")
    subir_nivel(personagem)


# CORRIGIDO: a função batalha agora fica antes do menu
def batalha(personagem, monstro):
    print(f"\nVocê encontrou um {monstro['nome']}!")
    while monstro["vida"] > 0 and personagem["vida"] > 0:
        acao = input("Escolha sua ação: (1) Atacar | (2) Usar poção | (3) Fugir: ")
        if acao == "1":
            dano_personagem = random.randint(10, 20)
            monstro["vida"] -= dano_personagem
            print(f"Você atacou o {monstro['nome']} causando {dano_personagem} de dano!")
            if monstro["vida"] <= 0:
                print(f"Você derrotou o {monstro['nome']}!")
                ganhar_xp(personagem, monstro["xp"])  # CORRIGIDO: chama ganhar_xp, que também sobe de nível
                break
            dano_monstro = random.randint(monstro["dano"], monstro["dano-max"])
            personagem["vida"] = max(0, personagem["vida"] - dano_monstro)  # MELHORIA: vida não fica negativa
            print(f"O {monstro['nome']} atacou você causando {dano_monstro} de dano! Vida restante: {personagem['vida']}/{personagem['vida_max']}")
        elif acao == "2":
            usar_pocao(personagem, inventario)
        elif acao == "3":
            print("Você fugiu da batalha!")
            break
        else:
            print("Ação inválida!")

    if personagem["vida"] <= 0:  # MELHORIA: mensagem de derrota
        print("💀 Você foi derrotado...")


# Programa principal
while True:
    print("\n1. Ficha | 2. Inventário | 3. Usar poção | 4. Lutar | 0. Sair")  # CORRIGIDO: opção 4
    opcao = input("Escolha: ")

    if opcao == "1":
        mostrar_ficha(personagem)
    elif opcao == "2":
        mostrar_inventario(inventario)
    elif opcao == "3":
        usar_pocao(personagem, inventario)
    elif opcao == "4":
        monstro = random.choice(monstros).copy()
        batalha(personagem, monstro)
    elif opcao == "0":
        print("Até a próxima aventura!")
        break
    else:
        print("Opção inválida!")
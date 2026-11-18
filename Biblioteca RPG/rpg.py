import random  # CORRIGIDO: movido para o topo

personagem = {
    "nome": "Gandalf",
    "classe": "Mago",
    "nivel": 1,
    "vida": 10,
    "vida_max": 10,
    "mana": 10,
    "xp": 0,
    "xp_proximo_nivel": 50,
    "ouro": 100
}


item_1 = {"nome": "Espada Longa", "tipo": "Arma", "dano": 15, "quantidade": 1}
item_2 = {"nome": "Poção de Cura", "tipo": "Consumível", "cura": 20, "quantidade": 3}
item_3 = {"nome": "Armadura de Couro", "tipo": "Armadura", "defesa": 5, "quantidade": 1}


inventario = [item_1, item_2, item_3]

# CORRIGIDO: movido para antes do menu
monstros = [
    {"nome": "Goblin", "vida": 30, "dano": 5, "dano-max": 10, "xp": 20, "ouro": 10, "nivel_minimo": 1, "chance_loot": 0.5, "loot": {"nome": "Poção de Cura", "tipo": "Consumível", "cura": 20, "quantidade": 1}},
    {"nome": "Orc", "vida": 50, "dano": 10, "dano-max": 20, "xp": 50, "ouro": 25, "nivel_minimo": 2, "chance_loot": 0.3, "loot": {"nome": "Espada Longa", "tipo": "Arma", "dano": 15, "quantidade": 1}},
    {"nome": "Troll", "vida": 80, "dano": 15, "dano-max": 30, "xp": 100, "ouro": 50, "nivel_minimo": 3, "chance_loot": 0.1, "loot": {"nome": "Armadura de Couro", "tipo": "Armadura", "defesa": 5, "quantidade": 1}}]

loja = [
    {"nome": "Poção de Cura", "tipo": "Consumível", "cura": 20, "preco": 10},
    {"nome": "Espada Longa", "tipo": "Arma", "dano": 15, "preco": 50},
    {"nome": "Armadura de Couro", "tipo": "Armadura", "defesa": 5, "preco": 30}
]


def mostrar_ficha(personagem):
    print(f"=== {personagem['nome']} | {personagem['classe']} | Nível {personagem['nivel']} ===")
    print(f"Vida: {personagem['vida']}/{personagem['vida_max']} | Mana: {personagem['mana']}")
    print(f"XP: {personagem['xp']}/{personagem['xp_proximo_nivel']}")  # MELHORIA: mostra o XP na ficha
    print(f"Ouro: {personagem['ouro']}")


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


def mostrar_loja(personagem, loja):
    print("\n=== Loja ===")
    for posicao, item in enumerate(loja, start=1):
        print(f"{posicao}. {item['nome']} (Tipo: {item['tipo']}, Preço: {item['preco']} ouro)")
    escolha = input("Digite o número do item que deseja comprar ou '0' para sair: ")
    if escolha.isdigit():
        escolha = int(escolha)
        if 1 <= escolha <= len(loja):
            item = loja[escolha - 1]
            if personagem["ouro"] >= item["preco"]:
                personagem["ouro"] -= item["preco"]
                novo_item = item.copy()  # CORRIGIDO: copia o produto inteiro (cura, dano, defesa...)
                novo_item["quantidade"] = 1
                adicionar_item(inventario, novo_item)
                print(f"Você comprou {item['nome']}! Ouro restante: {personagem['ouro']}")
            else:
                print("Você não tem ouro suficiente!")
        elif escolha == 0:
            print("Saindo da loja.")
        else:
            print("Escolha inválida!")
    else:
        print("Escolha inválida!")


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


def reviver(personagem):
    perda_xp = int(personagem["xp"] * 0.1)  # CORRIGIDO: calcula quanto XP será perdido (10% do atual)
    personagem["xp"] -= perda_xp  # CORRIGIDO: subtrai a perda; antes o XP virava uma tupla
    personagem["vida"] = personagem["vida_max"] // 2  # MELHORIA: reviver com metade da vida máxima
    print(f"Você foi revivido com {personagem['vida']} de vida, mas perdeu {perda_xp} pontos de experiência.")  # CORRIGIDO: mostra a perda real
    print(f"Vida: {personagem['vida']}/{personagem['vida_max']} | XP: {personagem['xp']}/{personagem['xp_proximo_nivel']}")


def sortear_monstro(personagem):
    disponiveis = [m for m in monstros if personagem["nivel"] >= m["nivel_minimo"]]
    return random.choice(disponiveis).copy()


def adicionar_item(inventario, item):
    for inv_item in inventario:
        if inv_item["nome"] == item["nome"]:
            inv_item["quantidade"] += item.get("quantidade", 1)
            print(f"Você encontrou {item['quantidade']}x {item['nome']}! Agora você tem {inv_item['quantidade']}.")
            return
    inventario.append(item)
    print(f"Você encontrou {item['quantidade']}x {item['nome']}! Adicionado ao inventário.")


def soltar_loot(personagem, monstro):
    if random.random() < monstro["chance_loot"]:
        adicionar_item(inventario, monstro["loot"].copy())
    else:
        print(f"O {monstro['nome']} não deixou nenhum item.")


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
                personagem["ouro"] += monstro["ouro"]  # MELHORIA: adiciona ouro ao personagem
                print(f"Você saqueou {monstro['ouro']} de ouro!")  # MELHORIA: mostra o ouro ganho
                soltar_loot(personagem, monstro)
                break
            dano_monstro = random.randint(monstro["dano"], monstro["dano-max"])
            personagem["vida"] = max(0, personagem["vida"] - dano_monstro)  # MELHORIA: vida não fica negativa
            print(f"O {monstro['nome']} atacou você causando {dano_monstro} de dano! Vida restante: {personagem['vida']}/{personagem['vida_max']}")
        elif acao == "2":  # CORRIGIDO: ação de usar poção na batalha
            usar_pocao(personagem, inventario)
        elif acao == "3":  # CORRIGIDO: ação de fugir da batalha
            print("Você fugiu da batalha!")
            break
        else:
            print("Ação inválida!")

    if personagem["vida"] <= 0:  # MELHORIA: mensagem de derrota
        print("💀 Você foi derrotado...")


# Programa principal
while True:
    print("\n1. Ficha | 2. Inventário | 3. Usar poção | 4. Lutar | 5. Loja | 0. Sair")  # CORRIGIDO: opção 4
    opcao = input("Escolha: ")

    if opcao == "1":
        mostrar_ficha(personagem)
    elif opcao == "2":
        mostrar_inventario(inventario)
    elif opcao == "3":
        usar_pocao(personagem, inventario)
    elif opcao == "4":
        monstro = sortear_monstro(personagem)  # CORRIGIDO: usa a função que filtra os monstros pelo nível
        batalha(personagem, monstro)
        if personagem["vida"] <= 0:
            reviver(personagem)
    elif opcao == "5":
        mostrar_loja(personagem, loja)
    elif opcao == "0":
        print("Até a próxima aventura!")
        break
    else:
        print("Opção inválida!")
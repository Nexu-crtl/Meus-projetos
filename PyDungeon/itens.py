class Item:
    def __init__(self, nome, tipo, quantidade=1):
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} ({self.tipo}) x{self.quantidade}"

    def empilhar(self, quantidade):  # ⭐ desafio: soma ao que já existe
        self.quantidade += quantidade


class Arma(Item):
    def __init__(self, nome, dano, quantidade=1):
        super().__init__(nome, "Arma", quantidade)
        self.dano = dano


class Pocao(Item):
    def __init__(self, nome, cura, quantidade=1):
        super().__init__(nome, "Consumível", quantidade)
        self.cura = cura


class Armadura(Item):
    def __init__(self, nome, defesa, quantidade=1):
        super().__init__(nome, "Armadura", quantidade)
        self.defesa = defesa


if __name__ == "__main__":
    espada = Arma("Espada Longa", dano=15)
    pocao = Pocao("Poção de Cura", cura=20, quantidade=3)
    armadura = Armadura("Armadura de Couro", defesa=5)

    inventario = [espada, pocao, armadura]
    for posicao, item in enumerate(inventario, start=1):
        print(f"{posicao}. {item}")

    print(f"\nDano da espada: {espada.dano}")
    print(f"Cura da poção: {pocao.cura}")
    print(f"Defesa da armadura: {armadura.defesa}")

    print(f"\nA espada é um Item? {isinstance(espada, Item)}")
    print(f"A espada é uma Poção? {isinstance(espada, Pocao)}")

    pocao.empilhar(2)
    print(f"\nDepois de empilhar 2: {pocao}")
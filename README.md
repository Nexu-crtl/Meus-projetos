# PyDungeon

Um RPG de terminal desenvolvido em Python. Escolha um personagem, enfrente monstros, evolua de nível, obtenha itens e administre seus recursos ao longo da aventura.

## Recursos

- Três personagens jogáveis: mago, guerreiro e arqueiro;
- Combate por turnos contra monstros escalados por nível;
- Sistema de experiência, progressão de nível e renascimento;
- Inventário, itens empilháveis, equipamentos e poções;
- Loja e recompensas de ouro e saque.

## Tecnologias

- Python 3
- Biblioteca padrão do Python (sem dependências externas)

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/Nexu-crtl/Meus-projetos.git
   cd Meus-projetos
   ```

2. Execute o jogo:

   ```bash
   python PyDungeon/rpg.py
   ```

> No Windows, caso necessário, substitua `python` por `py`.

## Estrutura do projeto

```text
.
├── .github/workflows/   # Automação de verificação
├── PyDungeon/
│   ├── rpg.py           # Jogo principal em terminal
│   └── itens.py         # Modelos de itens e equipamentos
├── CONTRIBUTING.md      # Orientações para contribuições
└── README.md            # Documentação do projeto
```

## Desenvolvimento

Para verificar a sintaxe dos arquivos Python localmente:

```bash
python -m py_compile PyDungeon/rpg.py PyDungeon/itens.py
```

## Contribuições

Contribuições são bem-vindas. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) antes de abrir uma issue ou pull request.

## Licença

Este repositório ainda não possui uma licença definida. Antes de reutilizar ou distribuir o código, entre em contato com o proprietário do projeto.

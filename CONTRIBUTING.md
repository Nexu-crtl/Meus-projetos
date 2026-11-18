# Como contribuir

Obrigado pelo interesse em contribuir com o PyDungeon.

## Antes de começar

- Abra uma issue para discutir mudanças grandes antes de implementá-las.
- Mantenha cada pull request focado em um único objetivo.
- Não envie arquivos gerados, ambientes virtuais ou dados sensíveis.

## Fluxo sugerido

1. Crie uma branch a partir de `main`.
2. Faça alterações pequenas e objetivas.
3. Verifique a sintaxe antes de enviar:

   ```bash
   python -m py_compile PyDungeon/rpg.py PyDungeon/itens.py
   ```

4. Descreva no pull request o que mudou e como a alteração foi verificada.

## Commits

Use mensagens curtas e descritivas. Exemplos:

```text
feat: adiciona novo tipo de item
fix: corrige cálculo de defesa
docs: atualiza instruções de execução
```

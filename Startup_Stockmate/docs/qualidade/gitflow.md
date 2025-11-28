# GitFlow Simplificado – StockMate

O processo de versionamento do projeto segue um GitFlow simplificado:

## Branches Principais
- **main** → versão estável, usada para entregas.
- **dev** → evolução contínua do projeto.
- **feature/** → branches criadas para cada tarefa específica.

## Fluxo
1. Criar uma branch a partir de `dev`, por exemplo:
   - `feature/adicionar-produto`
2. Implementar a funcionalidade.
3. Commitar e enviar para o GitHub.
4. Abrir Pull Request da feature → dev.
5. Após testes e revisão, merge para dev.
6. Quando o sprint terminar: dev → main.

Isso garante organização, rastreabilidade e qualidade no processo de desenvolvimento.

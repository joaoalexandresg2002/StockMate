# Plano de Testes – StockMate

Este plano define quais testes serão realizados para validar o sistema.

## Testes Funcionais

### 1. Teste de Login
- Usuário consegue inserir nome e senha?
- Campos aceitam somente valores válidos?
- Mensagens de erro aparecem corretamente?

### 2. Teste de Adicionar Produto
- Produto é adicionado com nome, preço e quantidade?
- Impede valores negativos?
- Mostra mensagem de sucesso?

### 3. Teste de Remover Produto
- Remove produto existente?
- Retorna erro se ID não existir?

### 4. Teste de Atualizar Quantidade
- Quantidade altera corretamente?
- Impede valores inválidos?

### 5. Teste de Listagem de Produtos
- Lista produtos cadastrados?
- Exibe mensagem se lista estiver vazia?

### 6. Teste de Buscar Produto por ID
- Retorna produto correto?
- Exibe erro caso não encontre?

## Frequência dos Testes
- Após cada funcionalidade concluída.
- Antes do merge para dev.
- No fim da sprint, antes do merge para main.

## Estratégia
- Testes manuais.
- Verificação dos requisitos.
- Revisão em dupla quando possível.

Esse plano garante que o sistema funcione corretamente durante toda a evolução do projeto.

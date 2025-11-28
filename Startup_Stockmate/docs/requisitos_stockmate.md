# Requisitos do Sistema — StockMate

## 1. Requisitos Funcionais (RF)

    RF01 — Cadastrar produto

        O sistema deve permitir cadastrar novos produtos informando ID, nome, quantidade e preço.

    RF02 — Listar produtos

        O sistema deve exibir todos os produtos cadastrados em formato organizado.

    RF03 — Buscar produto

        O sistema deve permitir buscar produtos por ID ou nome.

    RF04 — Atualizar produto

        O sistema deve permitir alterar informações de um produto existente.

    RF05 — Remover produto

        O sistema deve permitir excluir um produto do estoque.

    RF06 — Exibir detalhes de um produto

        Opcional: visualizar todas as informações completas de um item específico.

    RF07 — Registrar quantidade

        O sistema deve permitir adicionar e remover unidades do estoque.

## 2. Requisitos Não Funcionais (RNF)

    RNF01 — Interface

        O sistema deve operar via interface de linha de comando (CLI).

    RNF02 — Usabilidade

        As opções devem ser claras e de fácil entendimento para iniciantes.

    RNF03 — Desempenho

        Cada operação deve ser executada com tempo de resposta inferior a 1 segundo.

    RNF04 — Simplicidade do Código

        O código deve ser organizado e fácil de manter, usando boas práticas de programação.

    RNF05 — Armazenamento

        Os dados ficarão guardados apenas em memória enquanto o sistema estiver em execução.

# 3. Regras de Negócio (RN)

    RN01 — Quantidade não pode ser negativa

        Nenhum produto pode ter quantidade abaixo de zero.

    RN02 — Preço não pode ser negativo

        O sistema deve validar preços para impedir valores inválidos.

    RN03 — ID único

        Cada produto deve possuir um ID único e não pode ser duplicado.

    RN04 — Nome obrigatório

        Todo produto deve possuir nome válido.

## 4. Escopo do MVP

    O MVP do StockMate contempla apenas as funcionalidades essenciais para o controle básico de estoque:

        A. Cadastro de produtos (RF01)

        B. Listagem de produtos (RF02)

        C. Busca de produtos (RF03)

        D. Atualização de produtos (RF04)

        E. Remoção de produtos (RF05)

        Essas funcionalidades permitem que o usuário já utilize o sistema de forma funcional e prática, sem necessidade de recursos adicionais.
# Atividade 3 -  Agenda Telefônica

Este projeto implementa uma agenda telefônica em Python utilizando o framework Flask para fornecer uma interface web simples. A agenda permite adicionar, listar, buscar e remover contatos, com a capacidade de salvar e carregar contatos de um arquivo JSON.

## Funcionalidades

- Adicionar contato: Permite adicionar um novo contato com nome, telefone e email.
- Listar contatos: Exibe todos os contatos adicionados na agenda.
- Buscar contato: Permite buscar um contato pelo nome (funcionalidade disponível no código Python, mas não na interface web).
- Remover contato: Permite remover um contato existente da agenda.
- Salvar agenda: Salva os contatos em um arquivo JSON (`agenda.json`) para persistência de dados.
- Carregar agenda: Carrega os contatos de um arquivo JSON (`agenda.json`) na inicialização.

## Tecnologias Utilizadas

- Python
- Flask (framework web)
- HTML (para a interface web)
- JSON (para persistência de dados)

## Estrutura do Projeto

- `app.py`: Script principal que implementa a lógica da agenda e configura o servidor Flask.
- `templates/index.html`: Arquivo HTML que define a interface web.

## Como Executar

### Pré-requisitos

- Python 3 instalado
- Flask instalado (pode ser instalado via pip)

### Passos para execução

1. Clone este repositório para sua máquina local.
2. Navegue até o diretório do projeto.
3. Instale as dependências necessárias:
    ```sh
    pip install Flask
    ```
4. Execute o aplicativo:
    ```sh
    python app.py
    ```
5. Abra o navegador e acesse `http://127.0.0.1:5000/` para interagir com a agenda telefônica.

## Arquivos

### `app.py`

Contém a implementação das classes `Contato` e `Agenda`, e define as rotas do Flask para manipulação dos contatos. As principais funções são:

- `adicionar_contato`: Adiciona um novo contato à agenda.
- `listar_contatos`: Lista todos os contatos da agenda.
- `buscar_contato`: Busca um contato pelo nome.
- `remover_contato`: Remove um contato da agenda.
- `salvar_em_arquivo`: Salva os contatos em um arquivo JSON.
- `carregar_de_arquivo`: Carrega os contatos de um arquivo JSON.

### `templates/index.html`

Define a interface web para interação com a agenda telefônica. Inclui um formulário para adicionar novos contatos e uma lista para exibir e remover contatos existentes.

## Exemplos de Uso

1. **Adicionar Contato:**
   - Preencha o formulário com o nome, telefone e email do contato.
   - Clique em "Adicionar" para salvar o contato.

2. **Listar Contatos:**
   - Todos os contatos adicionados são exibidos na lista abaixo do formulário.

3. **Remover Contato:**
   - Clique no botão "Remover" ao lado do contato que deseja remover.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

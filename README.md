# 📝 Gerenciador de Tarefas em Python

Um **gerenciador de tarefas** simples desenvolvido em Python, utilizando **JSON** para persistência dos dados.

Este projeto foi desenvolvido como um exercício prático para aprimorar conhecimentos em Python, incluindo funções, módulos, listas, dicionários, manipulação de arquivos, JSON e operações CRUD.

## ✨ Funcionalidades

* ➕ Adicionar tarefas
* ✏️ Renomear tarefas
* 🗑️ Deletar tarefas
* ✅ Marcar tarefas como concluídas
* 🔄 Marcar tarefas como em progresso
* 📋 Listar todas as tarefas
* ✅ Listar tarefas concluídas
* ⏳ Listar tarefas em progresso
* 📌 Listar tarefas não concluídas
* 🔢 Atribuição automática de IDs
* ♻️ Reutilização de IDs disponíveis após a exclusão de tarefas
* 💾 Salvamento automático das tarefas em um arquivo JSON

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **JSON**
* **Bibliotecas padrão do Python**

## 📂 Estrutura do projeto

```text
Task-Manager/
│
├── main.py
├── functions.py
├── tasks.json
└── README.md
```

### `main.py`

Responsável pelo loop principal do programa, menu, entrada de dados e interação com o gerenciador de tarefas.

### `functions.py`

Contém as funções responsáveis por criar, atualizar, deletar, marcar e listar tarefas.

### `tasks.json`

Arquivo responsável por armazenar as tarefas e suas informações para que possam ser carregadas novamente quando o programa for iniciado.

## 📋 Estrutura de uma tarefa

Cada tarefa é armazenada como um dicionário:

```python
{
    "id": 1,
    "name": "Estudar Python",
    "completed": false,
    "In_progress": false
}
```

Uma tarefa pode possuir três estados:

* **Não concluída / Não iniciada**
* **Em progresso**
* **Concluída**

## 🚀 Download

### 1. Apenas abaixe o executável (Não é necessário ter o Python instalado)


## 🎮 Menu

Ao iniciar o programa, o seguinte menu será exibido:

```text
==============================
         TASK MANAGER
==============================
1-add
2-update
3-delete
4-mark
5-list
6-completed list
7-not completed list
8-list in progress
9-exit
==============================
```

Escolha uma opção digitando o número correspondente.

## 💾 Armazenamento dos dados

As tarefas são armazenadas localmente no arquivo `tasks.json`.

O arquivo é criado automaticamente quando o programa é iniciado, caso ainda não exista.

Exemplo:

```json
[
    {
        "id": 1,
        "name": "Estudar Python",
        "completed": true,
        "In_progress": false
    },
    {
        "id": 2,
        "name": "Estudar Redes",
        "completed": false,
        "In_progress": true
    }
]
```

## 🎯 Objetivos do projeto

Este projeto foi desenvolvido para praticar:

* Funções em Python
* Módulos e imports
* Listas e dicionários
* Loops e estruturas condicionais
* Tratamento de exceções
* Manipulação de arquivos
* Dados em JSON
* Operações CRUD
* Organização de código
* Persistência de dados

## 🔮 Possíveis melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

* [ ] Adicionar descrição às tarefas
* [ ] Adicionar prazos
* [ ] Adicionar prioridades
* [ ] Adicionar categorias
* [ ] Melhorar a validação das entradas
* [ ] Adicionar cores ao terminal
* [ ] Adicionar pesquisa de tarefas
* [ ] Adicionar opções de ordenação
* [ ] Melhorar a interface
* [ ] Adicionar testes automatizados

## Site URL
https://github.com/vitoxhj/Task-Tracker-CLI-in-Python

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.

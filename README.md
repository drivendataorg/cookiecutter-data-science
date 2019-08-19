## Projetos para Data Science

### Requisitos para utilizar este template

```
Python 3.6
Pipenv
Cookiecutter
Git
```

### Instalação dos requisitos:

#### Ubuntu:

Pipenv:
```
pip3 install pipenv
```

Cookiecutter:
```
pip3 install cookiecutter
```

Git:
```
sudo apt-get install git-core
```

### Inicialização do projeto:

```
cookiecutter https://github.com/lucaslrolim/cookiecutter-data-science
```

[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)

Após as configurações do projeto:

```
cd "nome-do-projeto"
```

Inicialização do Pipenv:

```
pipenv shell
pipenv lock
```

## Estrutura do Projeto
```
├── LICENSE
├── Makefile           <- Arquivo para armazenar comandos bash necessários para setup
├── README.md          <- Descrição geral com objetivos e contexto do projeto
├── data
│   ├── processed       <- Datasets finais, utilizados pelos modelos.
│   └── raw             <- Dump original extraído das bases de dado (imutável)
|   └── queries         <- Consultas utilizadas para extração de informações das bases de
│
├── models             <- Modelos treinados, predições geradas e sumário descritivo dos modelos e parâmetros utilizados
│
├── notebooks          <- Jupyter notebooks. A conversão para nomes é a versão (para ordenar), as iniciais do criador e uma descrição. Tudo separado por "-", e.x.
│                         `1.0-lr-initial-data-exploration`.
│
├── references         <- Artigos, links e outras referências para entendimento dos modelos.
│
├── outputs            <- Análises geradas em HTML, PDF, LaTeX, etc.
│   └── figures        <- Gráficos e figuras geradas e utilizadas nos relatórios.
│
├── requirements.txt   <- Requerimentos de ambiente para execução do projeto. e.x:
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Classes funções do projeto
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts para baixar e/ou gerar os datasets
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scrpits para criar features ou datasets nos quais serão aplicados os modelos
│   │   └── build_features.py
│   │
│   ├── models         <- Modelos
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Visualizações
│       └── visualize.py
```
## Para instalar as dependências:

```
pipenv install
```

## Instalação de bibliotecas auxiliares:

Certifique-se que o ambiente virtual do Pipenv esteja ativo.

```
pipenv install package
```

Exportanto o **src** para variável de ambiente:
```
pipenv install --editable .
```


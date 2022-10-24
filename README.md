# Projeto Job Insights

Analise de um conjunto de dados sobre empregos. Os dados foram extraídos do site Glassdoor e obtidos através do Kaggle, uma plataforma disponibilizados conjuntos de dados para cientistas de dados.

As implementações foram incorporadas a um aplicativo web com Flask desenvolvido pela [Trybe](https://www.betrybe.com/).

## Demo

![Demo](./gifs/demo.gif)

## Instalação e execução

### 1- Clone o repositório

```
git clone git@github.com:Leandroswq/job-insights.git
```

#### 2- Entre no diretório do projeto

```
cd job-insights
```

### 3- Crie um ambiente virtual

```
python3 -m venv .venv
```

### 4- Ative o ambiente virtual 

```
source .venv/bin/activate
```

### 5- Instale as dependências no ambiente virtual

```
python3 -m pip install -r dev-requirements.txt
```

### 6- Inicialize a aplicação

```
flask run
```
Ao digitar esse comando a aplicação irá inicializar na porta na porta 5000: http://127.0.0.1:5000/

## Habilidades Desenvolvidas

* Estruturas de repetição
* Estruturas condicionais
* Manipulação de arquivos
* Desenvolver testes com pytest
# Solução do TSP via Algoritmos Genéticos

Projeto de busca de soluções para o problema do caixeiro viajante, aplicado à distribuição de vacinas contra a COVID-19 em postos de vacinação de Curitiba - PR.

## Requisitos 
Interpretador Python;

Instalação do numPy: `pip install numpy`

## Execução
Executar o arquivo \_\_main\_\_.py
```
python __main__.py
```

## Alteração de parâmetros
No arquivo `tsp_ga.py`, alterar as seguintes variáveis:
```
tamPopulacao = 100 #1200 1000
# numero de pais selecionados para cruzamento em cada geracao:
nPais = 10 #25 40
geracoes = 20
#Probabilidade de Mutação:
p=0.002
```

Para calcular rota considerando retorno ao início, alterar o valor de `retornaInicio` para `True`, no método `calculafitness` da classe `cromossomo` (arquivo `cromossomo.py`).

## Dados
A matriz de distâncias deve ser salva com o nome `dist.csv`, no formato `csv`, com separadores `;`.
Cada linha da matriz representa uma origem, e cada coluna representa um destino. O número de linhas deve ser igual ao número de colunas.
A matriz deve conter apenas números inteiros. 

É necessário criar um arquivo com os apelidos das "cidades" tal que o número de apelidos seja idêntico ao número de linhas e colunas da matriz de distância. O arquivo deve ter o nome `US.txt`, no formato `csv`, com separadores `;`. Todos os itens devem estar na mesma linha.

<p align="center">
  <img align="center" src='https://user-images.githubusercontent.com/54161035/200095500-d5fec4ba-c97e-4f19-9e39-6764418a736b.png' />
</p>
<p align="center">UNIVERSIDADE FEDERAL DE PERNAMBUCO-UFPE</p>
<p align="center">CENTRO DE INFORMÁTICA</p>

##

<p align="center">
  <img align="center" src='https://img.shields.io/badge/Status-in%20progress-blue' />
  <img align="center" src='https://img.shields.io/badge/version-0.1-blue' />
  <img align="center" src='https://img.shields.io/badge/release%20date-abr/2023-blue' />
</p>

# Projeto: Busca do menor caminho entre dois nós usando algorítimo de Dijkstra

## 📋 Sobre

O projeto aplica o algorítimo de Dijkstra na busca da menor distância entre usuários da rede social "<a href="http://snap.stanford.edu/data/feather-lastfm-social.html">Last.f Asia</a>". Para executar o programa, disponibilizamos duas alternativas. A primeira consiste em um Jupyter Notebook, main.ipynb, onde é possível acompanhar a evolução etapa por etapa seguindo o fluxo das celúlas. A segunda permite interação com o programa a partir de uma interface executando o arquivo <span>main.py</span>.

## 📂 Estrutura do projeto

```
dijkstra-algorithm
├── README.md
├── data_base
|  ├── README.txt
|  ├── lastfm_asia_edges.csv
|  ├── lastfm_asia_features.json
|  └── lastfm_asia_target.csv
├── main.ipynb
├── main.py
└── modules
   ├── __init__.py
   ├── data.py
   ├── dijkstra.py
   ├── graph.py
   └── setup.py

```

## 🚀 Rodando o projeto

### A partir do Jupyter Notebook

1. Abra o notebook
2. Escolha o nó de partida e o nó de chegada atribuindo as variáveis node_a e node_b
  <img src="./assets/notebook-set-node.png" />
3. Execute o notebook
4. Acompanhe os resultados
  4.1 Rota percorrida
  <img src="./assets/notebook-log.png" />
  4.2 Grafo
  <img src="./assets/notebook-grafo.png" />

### A partir da interface gráfica

1. Execute o arquivo <span>main.py</span>

   Executando via terminal
   Na pasta do projeto execute:

   > python3 main.py

   Executando via Code Runner
   Abra o arquivo main.py e clique em executar (botão Code Runner) ou pelo atalho (ctrl + Alt + N)

2. Selecione o valor dos nós na interface e clique em "Buscar"
  <img src="./assets/interface-empty.png" />

3. Acompanhe o resultado pelo log na interface e pelo grafo
  <img src="./assets/interface-result.png" />
## 🛠️ Tecnologias utilizadas

- Python3
- Jupter Notebook

### Bibliotecas
- csv
- typing
- networkx
- matplotlib
- tkinter

## ✒️ Autores

| [<img src="https://avatars.githubusercontent.com/u/54161035?v=4" width=115><br><sub>Hítalo Nascimento</sub>](https://github.com/HitaloNasc) | [<img src="https://avatars.githubusercontent.com/u/100882928?v=4" width=115><br><sub>Ingrid Freire</sub>](https://github.com/ingridfsl) |
| :-----------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------: |

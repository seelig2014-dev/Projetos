# Calculadora de Consumo de Energia

## Sobre o Projeto

Este projeto consiste em uma calculadora de consumo de energia elétrica, desenvolvida em Python, com o objetivo de ajudar usuários a estimar o consumo mensal de aparelhos eletrônicos e o custo aproximado na conta de luz.

## Objetivo

Permitir que o usuário informe dados simples de um aparelho e receba:

* Consumo mensal em kWh
* Estimativa de custo mensal
* Possibilidade de informar o valor do kWh (ou usar valor padrão)
---

## Tecnologias Utilizadas

* 🐍 Python
* 💻 VS Code
* 🌐 GitHub
---
## Fórmularios

```
consumoMensal = (potencia * horasDia * 30) / 1000
```

Onde:

* Potência em Watts (W)
* Tempo de uso diário em horas
* Resultado em kWh/mês
---
##  Cálculo de Custo

```
custo = consumoMensal * tarifa
```

Se o usuário não informar o valor da tarifa, o sistema utiliza:

R$ 0,75 por kWh (valor padrão)
---
## Como Executar o Programa

1. Clone o repositório:

```
git clone https:https://github.com/seelig2014-dev/Projetos/blob/main/consumo_energia/consumo_energia.py
```

2. Acesse a pasta do projeto:

```
consumo-energia
```

3. Execute o programa:

```
consumo_energia.py
```
---
##  Objetivo Educacional

Este projeto foi desenvolvido para a agenda 5 de DSI do curso técnico em desenvolvimento de sistemas, com foco em:

* Lógica de programação
* Entrada e saída de dados
* Organização de projetos
* Publicação no GitHub
---
## 👨‍💻 Autor

Desenvolvido por Luis_seelig

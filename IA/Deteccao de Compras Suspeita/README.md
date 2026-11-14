# 🛒 Sistema de Detecção de Compras Suspeitas

## 📌 Sobre o projeto

Projeto desenvolvido em Python como atividade prática da disciplina de **Inteligência Artificial e DevOps**.

O sistema simula um ambiente de compras com diferentes categorias de produtos, analisando os itens selecionados e identificando possíveis compras fora dos padrões habituais.

A aplicação utiliza uma abordagem inspirada no algoritmo **Apriori**, comparando os produtos escolhidos com padrões de compra previamente definidos. Também estabelece limites de quantidade por categoria para identificar operações que possam necessitar de uma análise adicional.

## ⚙️ Funcionalidades

- **Identificação do cliente:** coleta o nome do usuário.
- **Menu de compras:** disponibiliza diferentes categorias de produtos.
- **Seleção de produtos:** permite escolher itens e informar quantidades.
- **Cálculo de valores:** calcula o preço total de cada compra.
- **Análise de padrões:** compara os produtos selecionados com padrões frequentes previamente definidos.
- **Detecção de compras fora do normal:** verifica se a quantidade comprada ultrapassa o limite estabelecido para cada categoria.
- **Sistema de alertas:** sinaliza compras que precisam de análise adicional.
- **Resumo da compra:** apresenta os detalhes da operação realizada.

## 🧠 Conceito de Inteligência Artificial: Apriori

O projeto utiliza uma lógica inspirada no algoritmo **Apriori**, conhecido por sua aplicação em mineração de dados e identificação de padrões frequentes em conjuntos de itens.

Nesta implementação, são definidos padrões de produtos para cada categoria:

| Categoria | Produtos considerados frequentes |
|---|---|
| Passagens | Primeira Classe e Classe Executiva |
| Mercado | M&M, Sucrilhos e Coca-Cola |
| Salgados | Coxinha, Pastel e Refrigerante |

O sistema compara o produto escolhido com essa lista e informa se ele pertence aos padrões previamente definidos.

**Observação:** esta atividade utiliza uma simulação simplificada inspirada no Apriori. Não implementa o algoritmo original nem realiza treinamento ou descoberta automática de padrões a partir de transações.

## 🚨 Detecção de compras fora do normal

O sistema estabelece limites de quantidade para cada categoria:

| Categoria | Limite de quantidade |
|---|---:|
| Passagens de avião | 5 unidades |
| Itens de mercado | 10 unidades |
| Salgados | 120 unidades |

Quando a quantidade informada ultrapassa o limite, o sistema apresenta um alerta de compra fora do normal e informa que a operação foi encaminhada para análise.

## 🛠️ Tecnologias e conceitos utilizados

- Python 3
- Estruturas condicionais (`if`, `elif` e `else`)
- Estruturas de repetição (`while`)
- Funções e estruturas de dados
- Dicionários e listas
- Operações matemáticas
- Entrada e saída de dados
- Lógica de detecção de padrões
- Fundamentos de mineração de dados

## 🚀 Como executar

**1. Clone o repositório:**

```bash
git clone https://github.com/SEU-USUARIO/IA_DevOPS.git
```

**2. Acesse a pasta da atividade:**

```bash
cd IA_DevOPS/atividade-02-deteccao-de-compras-suspeitas
```

**3. Execute o programa:**

```bash
python main.py
```

## 🎯 Objetivo acadêmico

Desenvolver uma aplicação que simula a análise de transações comerciais, aplicando conceitos de lógica de programação, identificação de padrões e detecção de comportamentos fora do normal.

A atividade busca demonstrar como conceitos de análise de dados e mineração de dados podem ser utilizados para auxiliar na identificação de operações que merecem atenção.

---

**Disciplina:** Inteligência Artificial e DevOps  
**Linguagem:** Python  
**Conceito estudado:** Algoritmo Apriori  
**Autor:** João Pedro Machado e Rebeca Matewanga
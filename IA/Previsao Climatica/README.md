# 🌡️ Previsão Climática e Recomendação de Roupas

## 📌 Sobre o projeto

Projeto desenvolvido em Python como atividade prática da disciplina de **Inteligência Artificial e DevOps**.

A aplicação permite informar uma cidade e registrar as temperaturas previstas para os dias de uma viagem. Com base nesses dados, o programa realiza uma análise climática e apresenta recomendações de roupas adequadas para cada condição de temperatura.

Além das recomendações, o sistema identifica situações de frio ou calor extremo e apresenta alertas para ajudar o usuário a se preparar para as condições climáticas.

## ⚙️ Funcionalidades

- **Entrada de dados:** identificação da cidade e quantidade de dias da viagem.
- **Registro de temperaturas:** coleta manual das temperaturas de cada dia.
- **Recomendação de roupas:** sugestões de vestuário conforme a temperatura.
- **Alertas climáticos:** identificação de frio extremo e calor extremo.
- **Cálculo da temperatura média:** análise da média das temperaturas registradas.
- **Temperatura máxima e mínima:** identificação dos valores extremos durante o período informado.

## 🌡️ Regras de recomendação

| Temperatura | Classificação | Recomendação |
|---|---|---|
| Até 5°C | Frio extremo | Usar roupas bem quentes |
| Até 15°C | Frio | Casaco ou blusa de frio |
| Até 25°C | Agradável | Roupas leves |
| Acima de 25°C | Calor | Camiseta, shorts ou roupas frescas |
| A partir de 35°C | Calor extremo | Hidratação e proteção solar |

## 🛠️ Tecnologias utilizadas

- Python 3
- Estruturas condicionais (`if`, `elif` e `else`)
- Estruturas de repetição (`for`)
- Funções
- Listas
- Operações matemáticas
- Entrada e saída de dados

## 🚀 Como executar

**1. Clone o repositório:**

```bash
git clone https://github.com/SEU-USUARIO/IA_DevOPS.git
```

**2. Acesse a pasta da atividade:**

```bash
cd IA_DevOPS/atividade-01-previsao-climatica
```

**3. Execute o programa:**

```bash
python main.py
```

## 💡 Exemplo de utilização

```text
Digite o nome da cidade: São Paulo
Quantos dias você ficará na cidade? 3

Digite a temperatura do dia 1: 12
Sugestão de roupa: Está frio. Vista um casaco ou blusa de frio.

Digite a temperatura do dia 2: 22
Sugestão de roupa: Clima agradável. Use roupa leve.

Digite a temperatura do dia 3: 36
Sugestão de roupa: Está calor. Use camiseta, shorts ou roupa fresca.
⚠ Alerta: Calor extremo! Beba bastante água e use protetor solar.

Cidade: São Paulo
Média de temperatura: 23.33 °C
Temperatura mais alta da viagem: 36.0 °C
Temperatura mais baixa da viagem: 12.0 °C
```

## 🎯 Objetivo acadêmico

Aplicar fundamentos de lógica de programação e Python na construção de uma solução automatizada capaz de processar informações climáticas, realizar cálculos e tomar decisões com base em condições predefinidas.

---

**Disciplina:** Inteligência Artificial e DevOps  
**Linguagem:** Python  
**Autor:** João Pedro Machado e Giovanna Aparecida
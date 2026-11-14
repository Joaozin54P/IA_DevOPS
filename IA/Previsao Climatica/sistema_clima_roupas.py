'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

''' 
# Função para sugerir roupa
def sugerir_roupa(temperatura):
    if temperatura <= 15:
        return "Está frio. Vista um casaco ou blusa de frio."
    elif temperatura <= 25:
        return "Clima agradável. Use roupa leve."
    else:
        return "Está calor. Use camiseta, shorts ou roupa fresca."


# Nova função: alerta climático
def alerta_clima(temperatura):
    if temperatura <= 5:
        return "⚠ Alerta: Frio extremo! Use roupas bem quentes."
    elif temperatura >= 35:
        return "⚠ Alerta: Calor extremo! Beba bastante água e use protetor solar."
    else:
        return ""


# Informar cidade
cidade = input("Digite o nome da cidade: ")

# Quantos dias ficará na cidade
dias = int(input("Quantos dias você ficará na cidade? "))

temperaturas = []

# Loop para cada dia
for i in range(dias):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

    print("Sugestão de roupa:", sugerir_roupa(temp))

    alerta = alerta_clima(temp)
    if alerta != "":
        print(alerta)

    print("-----------------------------")


# Calcular média da temperatura
media = sum(temperaturas) / len(temperaturas)

# Nova funcionalidade: temperatura máxima e mínima
temp_max = max(temperaturas)
temp_min = min(temperaturas)

print("\nCidade:", cidade)
print("Média de temperatura:", round(media, 2), "°C")
print("Temperatura mais alta da viagem:", temp_max, "°C")
print("Temperatura mais baixa da viagem:", temp_min, "°C")
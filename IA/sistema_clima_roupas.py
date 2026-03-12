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
    print("-----------------------------")

# Calcular média da temperatura
media = sum(temperaturas) / len(temperaturas)

print("\nCidade:", cidade)
print("Média de temperatura:", media, "°C")
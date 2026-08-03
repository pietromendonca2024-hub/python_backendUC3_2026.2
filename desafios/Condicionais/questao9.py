"""
9.	Crie o verificador de final de semana e de dia da semana (switch)
"""
day = input("Digite o dia da semana: ").lower()

if day == "sábado" or day == "domingo":
    print("É final de semana.")
else:
    print("É dia da semana.")
    
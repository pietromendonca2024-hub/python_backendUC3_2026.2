"""
8.	Sistema de notas com conceito
•	Peça a nota e exiba:
o	9 a 10 → "Excelente"
o	7 a 8.9 → "Bom"
o	5 a 6.9 → "Regular"
o	abaixo de 5 → "Insuficiente"
"""
grade = float(input("Digite a nota: "))
if 9 <= grade <= 10:
    print("Excelente")
elif 7 <= grade < 9:
    print("Bom")
elif 5 <= grade < 7:
    print("Regular")
else:
    print("Insuficiente")  
    
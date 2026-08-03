"""
5.	Aprovado ou reprovado
•	Peça a nota do aluno.
•	Se >= 7, mostre "Aprovado", senão "Reprovado".

"""
grade = float(input("Digite a nota do aluno: "))
if grade >= 7:
    print("Aprovado")
else:
    print("Reprovado")
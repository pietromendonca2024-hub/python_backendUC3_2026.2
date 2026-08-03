"""1.	Crie um dicionário com dados de um funcionário: nome, idade e cargo.


2.	Acesse o nome e o cargo do dicionário do exercício anterior e exiba na tela.



3.	Adicione ao funcionário uma chave "salário" com valor 3500 do exercício 1 e exiba na tela.


Altere o cargo do funcionário para “Pleno” do exercício 1 e exiba na tela.


4.	Percorra o dicionário do exercício 1 e imprimindo chave → valor.



6.Crie uma lista com 3 funcionários (cada um é um dicionário) e depois exiba na seguinte ordem :
ex: 
id: 01   - nome: Valdir   -  cargo: gerente
id: 02   - nome: José   -  cargo: suporte
id: 03   - nome: Maria  -  cargo: analista




7. Atualizar vários campos de uma vez.
Atualize o funcionário com:
cargo = “Sênior”
salário = 5000

pri
8. Criar dicionário com input do usuário
Enunciado:
Peça nome, idade e setor e salve em um dicionário.
"""
funcionário = {
    "nome": "Ana",
    "idade": "22",
    "cargo": "Analista"
}

print(f"Nome: {funcionário['nome']}")
print(f"Cargo: {funcionário['cargo']}") 

funcionário["salário"] = 3500
print(f"Salário: {funcionário['salário']}")

funcionário["cargo"] = "Pleno"
print(f"Cargo atualizado: {funcionário['cargo']}")

for chave, valor in funcionário.items():
    print(f"{chave} → {valor}")

funcionários = [
    {"id": 1, "nome": "Valdir", "cargo": "gerente"},
    {"id": 2, "nome": "José", "cargo": "suporte"},
    {"id": 3, "nome": "Maria", "cargo": "analista"}
]

for func in funcionários:
    print(f"id: {func['id']}   - nome: {func['nome']}   -  cargo: {func['cargo']}")

funcionário.update({"cargo": "Sênior", "salário": 5000})
print(f"Cargo atualizado: {funcionário['cargo']}")
print(f"Salário atualizado: {funcionário['salário']}")
print("funcionário atualizado:", funcionário)

nome = input("Digite o nome do funcionário: ")
idade = input("Digite a idade do funcionário: ")
setor = input("Digite o setor do funcionário: ")

funcionário_input = {
    "nome": nome,
    "idade": idade,
    "setor": setor

}
print("Dicionário criado com input do usuário:", funcionário_input)


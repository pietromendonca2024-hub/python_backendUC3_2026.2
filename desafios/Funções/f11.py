"""
11. Função que simula três tentativas de login
Use while com contador + if.

"""
def login():
    senha_correta = "python123"
    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        senha = input("Digite a senha: ")
        if senha == senha_correta:
            print("Senha correta! Acesso concedido.")
            return True
        else:
            tentativas += 1
            print(f"Senha incorreta. Tentativa {tentativas} de {max_tentativas}.")
    
    print("Número máximo de tentativas atingido. Acesso negado.")
    return False

print(login())
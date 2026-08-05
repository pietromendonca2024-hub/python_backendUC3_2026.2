"""
7. Função que valida senha
Peça ao usuário uma senha.
 Enquanto a senha for diferente de "python123", repita com while.

"""
def validar_senha():
    senha_correta = "python123"
    while True:
        senha = input("Digite a senha: ")
        if senha == senha_correta:
            print("Senha correta! Acesso concedido.")
            break
        else:
            print("Senha incorreta. Tente novamente.")

print(validar_senha())
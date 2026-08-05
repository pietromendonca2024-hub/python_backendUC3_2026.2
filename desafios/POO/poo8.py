"""
8.	Classe com contador de objetos
Enunciado:
 Conte quantos objetos foram criados.

"""
class ContadorObjetos:
    contador = 0  # Atributo de classe para contar objetos

    def __init__(self):
        ContadorObjetos.contador += 1  # Incrementa o contador ao criar um objeto

    @classmethod
    def exibir_contador(cls):
        print(f"Total de objetos criados: {cls.contador}")

# Exemplo de uso
objeto1 = ContadorObjetos()
objeto2 = ContadorObjetos()
ContadorObjetos.exibir_contador()  # Exibe o total de objetos criados


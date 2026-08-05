"""
6.	Classe Veiculo e subclasses
Enunciado:
 Crie duas subclasses Carro e Moto.

"""
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Portas: {self.portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Cilindrada: {self.cilindrada} cc")
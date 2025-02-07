'''1. Crie uma classe que modele o objeto "carro". 

2. Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade. 

3. Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera. 

4. Crie uma instância da classe carro. 

5. Faça o carro "andar" utilizando os métodos da sua classe.

 6. Faça o carro "parar" utilizando os métodos da sua classe.'''

class Carro:

    def __init__(self):
        self.ligado = False
        self.cor = "prata"
        self.modelo = "HB20"
        self.velocidade =0
       

    def ligar(self):
        if not self.ligado:
            self.ligado = True
    
    def desliga(self):
        if self.ligado and self.velocidade ==0:
            self.ligado = False

    def acelera(self):
        if self.ligado:
            self.velocidade +=10
    
    def desacelera(self):
        if self.ligado and self.velocidade >0:
            self.velocidade -=10
    

    


class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = "Prata"
        self.modelo = "HB20"
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("Carro ligado!")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.ligado and self.velocidade == 0:
            self.ligado = False
            print("Carro desligado!")
        elif self.velocidade > 0:
            print("Pare o carro antes de desligar!")
        else:
            print("O carro já está desligado.")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print(f"Acelerando... Velocidade atual: {self.velocidade} km/h")
        else:
            print("Ligue o carro primeiro!")

    def desacelerar(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 10
            print(f"Desacelerando... Velocidade atual: {self.velocidade} km/h")
        elif self.velocidade == 0:
            print("O carro já está parado.")
        else:
            print("Ligue o carro primeiro!")


meu_carro = Carro()

meu_carro.ligar()

meu_carro.acelerar()
meu_carro.acelerar()
meu_carro.acelerar()

meu_carro.desacelerar()
meu_carro.desacelerar()
meu_carro.desacelerar()

meu_carro.desligar()

#Código do dia-a-dia: um parque de diversões
class parque:
  def __init__(self, brinquedo, lotacao, funcionando):
    self.dinheiro = 0
    self.brinquedo = brinquedo
    self.lotacao = lotacao
    self.funcionando = funcionando
    self.com_espaço = True #acabou de abrir
    self.pessoas = 0
    pass

class Pessoa:
  def __init__(self, nome, dinheiro):
    self.nome = nome
    self.dinheiro = dinheiro

  def diversao(self, parque):
    if parque.funcionando == True:
      if self.dinheiro < 5:
        print("Você não tem saldo suficiente para o brinquedo escolhido, um ticket custa 5 reais")

      else:
        if parque.pessoas == parque.lotacao: 
          self.com_espaco = False
          print(f"Não pode entrar mais ninguém. {parque.brinquedo} com lotação máxima")

        elif parque.pessoas < parque.lotacao: #ainda pode entrar
          self.com_espaco = True
          self.dinheiro -= 5
          parque.pessoas += 1
          print(f"Ticket comprado com sucesso. Agora, você tem {self.dinheiro} reais. Pode entrar >> {parque.brinquedo}")
          parque.dinheiro += 5
          print(f'O caixa do parque se encontra em {parque.dinheiro} reais')

    else: #manutenção
      print(f'A {parque.brinquedo} está em manutenção')


#Brinquedos
brinquedo1 = parque('roda gigante', 1, True)
brinquedo2 = parque('montanha russa', 12, False) #em manutenção
brinquedo3 = parque('bate-bate', 8, True)
brinquedo4 = parque('carrosel', 6, True)
brinquedo5 = parque('navio pirata', 10, True)

#Clientes em potencial
Pessoa1 = Pessoa("Ana", 10)
Pessoa2 = Pessoa("Claudia", 4)
Pessoa3 = Pessoa("Elisa", 20)

#Ações de cada cliente: previsão de saldo, entrada, manutenção e lotação
Pessoa2.diversao(brinquedo1)
print("\n")
Pessoa1.diversao(brinquedo1)
print("\n")
Pessoa3.diversao(brinquedo2)
print("\n")
Pessoa3.diversao(brinquedo1)
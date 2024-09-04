import statistics

class Estatistica:
    def __init__(self, dados):
        self.dados = dados

    def media(self):
        return sum(self.dados) / len(self.dados)

    def mediana(self):
        return statistics.median(self.dados)

    def moda(self):
        try:
            return statistics.mode(self.dados)
        except statistics.StatisticsError:
            return "Não existe uma moda única."

    def desvio_padrao(self):
        return statistics.stdev(self.dados)

# Função para coletar dados do usuário
def coletar_dados():
    dados = []
    while True:
        entrada = input("Digite um número (ou 'sair' para terminar): ")
        if entrada.lower() == 'sair':
            break
        try:
            numero = float(entrada)
            dados.append(numero)
        except ValueError:
            print("Por favor, insira um número válido.")
    return dados

# Coletar os dados
dados = coletar_dados()

# Verificar se há dados suficientes para cálculo
if len(dados) > 0:
    estatistica = Estatistica(dados)

    while True:
        print("\nEscolha uma operação estatística:")
        print("1. Calcular a Média")
        print("2. Calcular a Mediana")
        print("3. Calcular a Moda")
        print("4. Calcular o Desvio Padrão")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '1':
            print("Média:", estatistica.media())
        elif escolha == '2':
            print("Mediana:", estatistica.mediana())
        elif escolha == '3':
            print("Moda:", estatistica.moda())
        elif escolha == '4':
            print("Desvio Padrão:", estatistica.desvio_padrao())
        elif escolha == '5':
            print("Encerrando o programa.")
            break
        else:
            print("Escolha inválida. Tente novamente.")
else:
    print("Nenhum dado válido foi inserido para cálculo.")

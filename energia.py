try:
    import matplotlib.pyplot as plt
except ImportError:
    print("O pacote matplotlib não está instalado. Para instalar, execute: pip install matplotlib")

def calcular_consumo(aparelhos):
    total_consumo_kwh = 0
    total_custo = 0

    consumos = {}
    
    for aparelho in aparelhos:
        nome = aparelho['nome']
        potencia = aparelho['potencia']
        horas = aparelho['horas']
        dias = aparelho['dias']
        preco_kwh = aparelho['preco_kwh']

        # Cálculo do consumo mensal em kWh
        consumo_kwh = (potencia / 1000) * horas * dias
        custo = consumo_kwh * preco_kwh

        total_consumo_kwh += consumo_kwh
        total_custo += custo

        # Armazenar os resultados individuais para o gráfico
        consumos[nome] = consumo_kwh

        # Exibir resultados individuais
        print(f"Consumo mensal de {nome}: {consumo_kwh:.2f} kWh")
        print(f"Custo mensal de {nome}: R$ {custo:.2f}\n")

    # Exibir resultados totais
    print(f"Consumo total mensal: {total_consumo_kwh:.2f} kWh")
    print(f"Custo total mensal: R$ {total_custo:.2f}\n")

    # Sugestões de economia
    if total_consumo_kwh > 500:
        print("Sugestão: Tente reduzir o uso de aparelhos que consomem muita energia.\n")
    else:
        print("Bom trabalho! Seu consumo de energia está em níveis aceitáveis.\n")

    return consumos


def adicionar_aparelho():
    nome = input("Digite o nome do aparelho: ")

    while True:
        try:
            potencia = float(input(f"Digite a potência (em watts) de {nome}: "))
            horas = float(input(f"Digite as horas de uso diário de {nome}: "))
            dias = int(input(f"Digite os dias de uso no mês para {nome}: "))
            preco_kwh = float(input(f"Digite o preço do kWh em sua região: "))
            break
        except ValueError:
            print("Por favor, insira um valor válido.")

    return {
        'nome': nome,
        'potencia': potencia,
        'horas': horas,
        'dias': dias,
        'preco_kwh': preco_kwh
    }


def plotar_consumo(consumos):
    if not consumos:
        print("Nenhum dado para plotar.")
        return

    nomes = list(consumos.keys())
    valores = list(consumos.values())

    plt.barh(nomes, valores, color='blue')
    plt.xlabel('Consumo (kWh)')
    plt.ylabel('Aparelho')
    plt.title('Consumo de Energia por Aparelho')
    plt.show()


def main():
    aparelhos = []
    print("Bem-vindo à Calculadora de Consumo de Energia!\n")

    while True:
        adicionar = input("Deseja adicionar um aparelho eletrônico? (s/n): ").lower()
        if adicionar == 's':
            aparelho = adicionar_aparelho()
            aparelhos.append(aparelho)
        elif adicionar == 'n':
            break
        else:
            print("Por favor, responda com 's' ou 'n'.")

    if aparelhos:
        consumos = calcular_consumo(aparelhos)

        # Perguntar se deseja plotar o gráfico
        plotar = input("Deseja visualizar um gráfico do consumo? (s/n): ").lower()
        if plotar == 's':
            plotar_consumo(consumos)
    else:
        print("Nenhum aparelho adicionado. Encerrando o programa.")


if __name__ == "__main__":
    main()

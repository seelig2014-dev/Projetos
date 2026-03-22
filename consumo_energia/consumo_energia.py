# Calculadora de Consumo de Energia Elétrica

def calcular_consumo(): # Monta uma estrutura de bloco, para poder ser usada posteriormente
    print("Calculadora de Consumo de Energia\n")

    aparelho = input("Digite o nome do aparelho: ")
    potencia = float(input("Digite a potência (em Watts): "))
    horas_dia = float(input("Digite o tempo de uso diário (em horas): "))

    # Entrada do valor do kWh (com padrão)
    entrada_tarifa = input("Digite o valor do kWh (pressione Enter para usar R$ 0,75): ")

    if entrada_tarifa.strip() == "":# estrutura usada para permitir a entrada do valor do kwh ou aceitar o padrão, posteriormente pode-se usar um bloco para calcular os custos com ICMS

        tarifa = 0.75#tarifa padrão sugerida na agenda
        print("Usando valor padrão de R$ 0.75 por kWh")
    else:
        tarifa = float(entrada_tarifa)

    # Cálculo do consumo mensal
    consumo_mensal = (potencia * horas_dia * 30) / 1000

    # Cálculo do custo
    custo = consumo_mensal * tarifa

    print("\n Resultado:")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"Tarifa utilizada: R$ {tarifa:.2f}/kWh")
    print(f"Custo estimado: R$ {custo:.2f} por mês")


# Executar o programa, estudando em um material na internet, vi que a estrutura é importante para evitar que o programa seja executado automaticamente em uma transferencia, é como se fosse um dispositivo de segurança
if __name__ == "__main__":
    calcular_consumo()


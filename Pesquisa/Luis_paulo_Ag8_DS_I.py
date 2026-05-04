# Pesquisa de satisfação
# Aluno_Luis_Paulo

qtd_excelente = 0
qtd_ruim = 0

# Estrutura de repeticao para os primeiros 50 entrevistados
for i in range(1, 51):
    print("\nEntrevistado", i)
    
    nome = input("Digite seu nome: ")
    
    # verificacao da idade do entrevistado
    idade = input("Digite sua idade: ")
    while idade.isdigit() == False:
        print("Digite apenas números!")
        idade = input("Digite sua idade: ")
    
    idade = int(idade)

    print("Avalie o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    # estrutura da opiniao do entrevistado (usando And "e")
    opiniao = input("Digite sua opção: ")
    while opiniao != "1" and opiniao != "2" and opiniao != "3":
        print("Opção inválida! Digite 1, 2 ou 3.")
        opiniao = input("Digite sua opção: ")

    # Contador
    if opiniao == "1":
        qtd_excelente = qtd_excelente + 1
    elif opiniao == "3":
        qtd_ruim = qtd_ruim + 1

# Resultado final do programa
print("\nRESULTADO DA PESQUISA")
print("Quantidade de respostas EXCELENTE:", qtd_excelente)
print("Quantidade de respostas RUIM:", qtd_ruim)
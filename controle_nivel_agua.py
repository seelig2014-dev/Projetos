# ==========================================
# Sistema de Controle de Níveis de Água
# Agenda 11 - DSI
# ==========================================

# Importação da biblioteca
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [
    "Nível 1",
    "Nível 2",
    "Nível 3",
    "Nível 4",
    "Nível 5"
]

# Função responsável pelas cores e mensagens
def verificar_nivel(nivel):

    if nivel == 1:
        return Fore.RED + "Nível 1 - Muito baixo (CRÍTICO)"

    elif nivel == 2:
        return Fore.YELLOW + "Nível 2 - Baixo"

    elif nivel == 3:
        return Fore.GREEN + "Nível 3 - Médio"

    elif nivel == 4:
        return Fore.CYAN + "Nível 4 - Alto"

    elif nivel == 5:
        return Fore.BLUE + "Nível 5 - Muito alto (ALERTA)"

    else:
        return Fore.WHITE + "Nível inválido"


# Exibição do sistema
print("\n===== MONITORAMENTO DO RESERVATÓRIO =====\n")

# Simulação dos níveis
for i in range(1, 6):

    mensagem = verificar_nivel(i)
    print(mensagem)

# Restaura o terminal ao padrão
print(Style.RESET_ALL) 
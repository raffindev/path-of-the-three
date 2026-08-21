# Função de Cabeçalho
def cabeçalho(txt):
    return '='*40 + '\n' + txt.center(40) + '\n' + '='*40

# Validar ação
def validar_ação(escolha):
    if escolha in ["1", "2", "3", "4"]:
        return True
    return False
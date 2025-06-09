from modelos.cofre import CofreDeSenhas
from modelos.senha import SenhaEmailPessoal, SenhaComplexa, SenhaTemporal, SenhaSimples

def menu():
    print("\n=== GERADOR DE SENHAS ===")
    print("1 - Gerar senha para Email pessoal")
    print("2 - Gerar Senha Complexa")
    print("3 - Gerar Senha para Login Temporario")
    print("4 - Gerar Senha Simples (apenas letras)")
    print("0 - Sair")

    entrada = input("Escolha uma opcao: ").strip()

    opcoes_validas = {
        "0": "0", "00": "0",
        "1": "1", "01": "1",
        "2": "2", "02": "2",
        "3": "3", "03": "3",
        "4": "4", "04": "4"
    }

    if entrada not in opcoes_validas:
        print("Entrada invalida! Digite uma opcao entre 0 e 4.")
        return None

    return opcoes_validas[entrada]

if __name__ == "__main__":
    cofre = CofreDeSenhas("senhas.json")
    cofre.carregar_de_arquivo()

    while True:
        opcao = menu()

        if opcao is None:
            continue

        if opcao == "1":
            senha = SenhaEmailPessoal(8)
            senha.gerar()
            cofre.adicionar_senha("Email pessoal", senha)

        elif opcao == "2":
            senha = SenhaComplexa(12)
            senha.gerar()
            cofre.adicionar_senha("Senha Complexa", senha)

        elif opcao == "3":
            senha = SenhaTemporal(6)
            senha.gerar()
            cofre.adicionar_senha("Login temporario", senha)

        elif opcao == "4":
            senha = SenhaSimples(10)
            senha.gerar()
            cofre.adicionar_senha("Senha Simples", senha)

        elif opcao == "0":
            break

    cofre.listar_senhas()
    cofre.salvar_em_arquivo()
    print("Programa encerrado.")

import json

class CofreDeSenhas:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.senhas = []

    def adicionar_senha(self, descricao, senha):
        if senha.validar():
            self.senhas.append({"descricao": descricao, "senha": senha.valor})
            print(f"Senha adicionada: {descricao}")
        else:
            print("Senha invalida. Nao foi adicionada.")

    def salvar_em_arquivo(self):
        try:
            with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(self.senhas, arquivo, indent=4, ensure_ascii=False)
                print("Senhas salvas com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar senhas: {e}")

    def carregar_de_arquivo(self):
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                self.senhas = json.load(arquivo)
                print("Senhas carregadas com sucesso.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Arquivo de senhas nao encontrado ou corrompido. Criando novo cofre.")
            self.senhas = []
            self.salvar_em_arquivo()
        except Exception as e:
            print(f"Erro inesperado: {e}")

    def listar_senhas(self):
        print("=== Senhas no Cofre ===")
        for s in self.senhas:
            print(f"{s['descricao']}: {s['senha']}")

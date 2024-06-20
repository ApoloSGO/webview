import string
import secrets

# Lista de caracteres para geração de senhas
caracteres = list(string.ascii_letters + string.digits + "!@#$%¨&*()-?:")

def gerar_senha(tamanho):
    senha = [secrets.choice(caracteres) for _ in range(tamanho)]
    return "".join(senha)

def obter_input_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 1:
                raise ValueError("O valor deve ser pelo menos 1.")
            return valor
        except ValueError as ve:
            print(f"Entrada inválida: {ve}")

def main():
    while True:
        # Obter tamanho e quantidade de senhas com validação de entrada
        tamanho = obter_input_positivo("Digite um tamanho para a senha: ")
        qtd = obter_input_positivo("Digite a quantidade de senhas a ser gerada: ")

        # Gera a quantidade de senhas solicitada
        for _ in range(qtd):
            senha = gerar_senha(tamanho)
            print(senha)

        # Pergunta ao usuário se deseja rodar novamente
        checar = input("Gostaria de rodar o programa novamente? (sim/nao): ").strip().lower()
        
        if checar not in ["sim", "s"]:
            print("\nAté mais! Finalizando o programa.\n")
            break  # Sai do loop se a resposta não for "sim" ou "s"

if __name__ == "__main__":
    main()

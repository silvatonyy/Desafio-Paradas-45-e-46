import random

def escolha_do_usuario():
    print("Escolha uma das opções:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    escolha = input("Digite o número correspondente à sua escolha: ")
    return int(escolha)

def escolha_do_computador():
    return random.randint(1, 3)

def vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif (escolha_usuario == 1 and escolha_computador == 3) or \
         (escolha_usuario == 2 and escolha_computador == 1) or \
         (escolha_usuario == 3 and escolha_computador == 2):
        return "Você venceu!"
    else:
        return "Você perdeu."

def principal():
    escolhas = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

    escolha_usuario = escolha_do_usuario()
    escolha_computador = escolha_do_computador()

    print(f"Você escolheu: {escolhas[escolha_usuario]}")
    print(f"O computador escolheu: {escolhas[escolha_computador]}")

    resultado = vencedor(escolha_usuario, escolha_computador)
    print(resultado)

if __name__ == "__main__":
    principal()

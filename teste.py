import random
import time
def traduzir_escolha(escolha):
    """Converte número ou palavra para a opção correspondente."""
    mapa = {
        "1": "papel",
        "2": "pedra",
        "3": "tesoura",
        "papel": "papel",
        "pedra": "pedra",
        "tesoura": "tesoura"
    }
    return mapa.get(escolha.lower())

def jogar_rodada():
    opcoes = ["papel", "pedra", "tesoura"]
    sistema = random.choice(opcoes)
    usuario = input("Escolha (1=papel, 2=pedra, 3=tesoura ou escreva): ")
    usuario = traduzir_escolha(usuario)

    if usuario not in opcoes:
        print("Opção inválida. Rodada perdida!")
        return None

    print(f"Você escolheu: {usuario}")
    print(f"O sistema escolheu: {sistema}")

    if usuario == sistema:
        print("Empate!")
        return "empate"
    elif (usuario == "pedra" and sistema == "tesoura") or \
         (usuario == "papel" and sistema == "pedra") or \
         (usuario == "tesoura" and sistema == "papel"):
        print("Você venceu esta rodada! 🎉")
        return "usuario"
    else:
        print("O sistema venceu esta rodada! 🤖")
        return "sistema"

def jogo():
    pontos_usuario = 0
    pontos_sistema = 0

    for rodada in range(1, 4):
        print(f"\n--- Rodada {rodada} ---")
        resultado = jogar_rodada()
        if resultado == "usuario":
            pontos_usuario += 1
        elif resultado == "sistema":
            pontos_sistema += 1
        # empate não soma pontos

    print("\n=== Resultado Final ===")
    print(f"Você: {pontos_usuario} | Sistema: {pontos_sistema}")

    if pontos_usuario > pontos_sistema:
        print("🏆 Você é o campeão!")
    elif pontos_sistema > pontos_usuario:
        print("🤖 O sistema é o campeão!")
    else:
        print("⚖️ O jogo terminou empatado!")
    time.sleep(3)
# Executa o jogo
jogo()


 

# Programa para calcular médias de um time de futebol


while True:
    print("\n--- Cálculo de Médias do Time ---")
    time = input("Digite o nome do time: ")
    jogos = int(input("Quantos jogos você quer analisar? "))
    
    total_gols = 0
    total_escanteios = 0
    total_cartoes = 0

    for i in range(1, jogos + 1):
        print(f"\nJogo {i}:")
        gols = int(input("  Quantos gols? "))
        escanteios = int(input("  Quantos escanteios? "))
        cartoes = int(input("  Quantos cartões? "))

        total_gols += gols
        total_escanteios += escanteios
        total_cartoes += cartoes

    media_gols = total_gols / jogos
    media_escanteios = total_escanteios / jogos
    media_cartoes = total_cartoes / jogos
    
    print(f"\nMédias do {time}:")
    print(f"Gols por jogo: {media_gols:.2f}")
    print(f"Escanteios por jogo: {media_escanteios:.2f}")
    print(f"Cartões por jogo: {media_cartoes:.2f}")

    continuar = input("\nQuer analisar outro time? (s/n): ").lower()
    if continuar != 's':
        print("Encerrando o programa... Até mais!")
        break
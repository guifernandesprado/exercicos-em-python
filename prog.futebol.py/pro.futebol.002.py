import csv

# Nome do arquivo onde os dados serão salvos
ARQUIVO = "estatisticas_times.csv"

# Cabeçalho do arquivo CSV
cabecalho = ["Time", "Média de Gols", "Média de Escanteios", "Média de Cartões"]

# Cria o arquivo CSV (ou sobrescreve se já existir) com o cabeçalho
with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(cabecalho)

times = []  # lista para guardar resultados temporariamente

while True:
    print("\n--- Cálculo de Médias do Time ---")

    time = input("Digite o nome do time: ").strip().title()

    # Garantir entrada válida
    while True:
        try:
            jogos = int(input("Quantos jogos você quer analisar? "))
            if jogos <= 0:
                print("⚠️ Digite um número maior que zero.")
                continue
            break
        except ValueError:
            print("⚠️ Entrada inválida. Tente novamente.")

    total_gols = total_escanteios = total_cartoes = 0

    for i in range(1, jogos + 1):
        print(f"\nJogo {i}:")
        try:
            gols = int(input("  Quantos gols? "))
            escanteios = int(input("  Quantos escanteios? "))
            cartoes = int(input("  Quantos cartões? "))
        except ValueError:
            print("⚠️ Valor inválido! Este jogo será ignorado.")
            continue

        total_gols += gols
        total_escanteios += escanteios
        total_cartoes += cartoes

    # Cálculo das médias
    media_gols = total_gols / jogos
    media_escanteios = total_escanteios / jogos
    media_cartoes = total_cartoes / jogos

    # Mostra o resultado
    print(f"\n📊 Médias do {time}:")
    print(f"   ⚽ Gols por jogo: {media_gols:.2f}")
    print(f"   🏁 Escanteios por jogo: {media_escanteios:.2f}")
    print(f"   🟥 Cartões por jogo: {media_cartoes:.2f}")

    # Salva no CSV
    with open(ARQUIVO, "a", newline="", encoding="utf-8") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([time, f"{media_gols:.2f}", f"{media_escanteios:.2f}", f"{media_cartoes:.2f}"])

    # Guarda na lista também (para mostrar o resumo final)
    times.append({
        "time": time,
        "média_gols": media_gols,
        "média_escanteios": media_escanteios,
        "média_cartões": media_cartoes
    })

    continuar = input("\nQuer analisar outro time? (s/n): ").lower().strip()
    if continuar != "s":
        break

# Exibe o resumo final
print("\n=== Resumo Final ===")
for t in times:
    print(f"\n{t['time']}:")
    print(f"  ⚽ Gols: {t['média_gols']:.2f}")
    print(f"  🏁 Escanteios: {t['média_escanteios']:.2f}")
    print(f"  🟥 Cartões: {t['média_cartões']:.2f}")

print(f"\n📁 Todos os dados foram salvos em '{ARQUIVO}'.")
print("Programa encerrado. 👋")

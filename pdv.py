historico = []

print("=== PDV - Ponto de Venda ===")

while True:
    while True:
        texto = input("\nValor da compra em R$ (0 para encerrar): ").strip().replace(",", ".")
        numero = texto[1:] if texto.startswith("-") else texto

        if not numero.replace(".", "", 1).isdecimal():
            print("Digite um número válido.")
        elif float(texto) < 0:
            print("O valor não pode ser negativo.")
        else:
            valor = float(texto)
            break

    if valor == 0:
        break

    while True:
        texto = input("Idade do cliente: ").strip()
        numero = texto[1:] if texto.startswith("-") else texto

        if not numero.isdecimal():
            print("Digite um número inteiro válido.")
        elif int(texto) < 0:
            print("A idade não pode ser negativa.")
        else:
            idade = int(texto)
            break

    valor_final = valor

    if idade >= 65:
        valor_final *= 0.80

    if valor_final > 100:
        valor_final *= 0.90

    historico.append({
        "bruto": valor,
        "idade": idade,
        "final": valor_final,
    })

    print(f"Valor final: R$ {valor_final:.2f}")

# Resumo do dia
print("\n" + "=" * 40)
print("RESUMO DO DIA")
print("=" * 40)

if not historico:
    print("Nenhuma compra registrada.")
else:
    total_bruto = sum(c["bruto"] for c in historico)
    total_final = sum(c["final"] for c in historico)
    total_descontos = total_bruto - total_final
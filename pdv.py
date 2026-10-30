historico = []

while True:
    valor = float(input("Valor da compra (0 para encerrar): "))
    if valor == 0:
        break
    idade = int(input("Idade: "))

    if valor < 0 or idade < 0:
        print("Valor e idade não podem ser negativos.")
        continue

    final = valor
    if idade >= 65:
        final *= 0.80
    if final > 100:
        final *= 0.90

    historico.append((valor, final))
    print(f"Valor final: R$ {final:.2f}")

bruto = sum(b for b, f in historico)
final = sum(f for b, f in historico)

print("\nRESUMO DO DIA")
print(f"Compras: {len(historico)}")
print(f"Total bruto: R$ {bruto:.2f}")
print(f"Descontos: R$ {bruto - final:.2f}")
print(f"Total final: R$ {final:.2f}")

input("\nPressione Enter para sair...")
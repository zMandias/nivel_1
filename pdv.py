def ler_valor():
    """Lê o valor da compra. Retorna 0 para encerrar. Repete se inválido."""
    while True:
        try:
            valor = float(input("\nValor da compra em R$ (0 para encerrar): ").replace(",", "."))
        except ValueError:
            print("⚠️  Digite um número válido.")
            continue
        if valor < 0:
            print("⚠️  O valor não pode ser negativo.")
            continue
        return valor


def ler_idade():
    """Lê a idade do cliente. Repete se inválida ou negativa."""
    while True:
        try:
            idade = int(input("Idade do cliente: "))
        except ValueError:
            print("⚠️  Digite um número inteiro válido.")
            continue
        if idade < 0:
            print("⚠️  A idade não pode ser negativa.")
            continue
        return idade


def calcular_valor_final(valor, idade):
    """Aplica as regras de desconto e retorna o valor final."""
    valor_final = valor

    # Regra 1: desconto de 20% para idosos (65+)
    if idade >= 65:
        valor_final *= 0.80

    # Regra 2: 10% extra se o valor (já com desconto de idade) passar de R$ 100
    if valor_final > 100:
        valor_final *= 0.90

    return valor_final


def exibir_resumo(historico):
    """Mostra o resumo do dia."""
    print("\n" + "=" * 40)
    print("RESUMO DO DIA")
    print("=" * 40)

    if not historico:
        print("Nenhuma compra registrada.")
        return

    total_bruto = sum(c["bruto"] for c in historico)
    total_final = sum(c["final"] for c in historico)
    total_descontos = total_bruto - total_final

    print(f"Compras registradas : {len(historico)}")
    print(f"Total bruto         : R$ {total_bruto:.2f}")
    print(f"Total de descontos  : R$ {total_descontos:.2f}")
    print(f"Total final         : R$ {total_final:.2f}")
    print("=" * 40)


def main():
    historico = []

    print("=== PDV - Ponto de Venda ===")

    while True:
        valor = ler_valor()
        if valor == 0:
            break

        idade = ler_idade()
        valor_final = calcular_valor_final(valor, idade)

        historico.append({
            "bruto": valor,
            "idade": idade,
            "final": valor_final,
        })

        print(f"Valor final: R$ {valor_final:.2f}")

    exibir_resumo(historico)


if __name__ == "__main__":
    main()
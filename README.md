O PDV é um programa que calcula o valor final de cada compra aplicando descontos em sequência: 20% para clientes com 65 anos ou mais e, em seguida, mais 10% se o valor já com o primeiro desconto passar de R$ 100. Ele guarda cada compra numa lista e repete o processo até você digitar `0` no valor da compra. No fim, mostra o resumo do dia com a quantidade de compras, o total bruto, o total de descontos e o total final.

## Como rodar: 
O comando para executar o programa (python pdv.py).

## Casos de teste

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|-----------:|------:|:--------------:|:--------------:|---------------------:|
| 1 | 50.00 | 30 | 0% | 0% | **R$ 50.00** |
| 2 | 100.00 | 30 | 0% | 0% | **R$ 100.00** |
| 3 | 80.00 | 65 | 20% | 0% | **R$ 64.00** |
| 4 | 100.00 | 70 | 20% | 0% | **R$ 80.00** |
| 5 | 125.00 | 70 | 20% | 0% | **R$ 100.00** |
| 6 | 200.00 | 30 | 0% | 10% | **R$ 180.00** |
| 7 | 101.00 | 30 | 0% | 10% | **R$ 90.90** |
| 8 | 200.00 | 65 | 20% | 10% | **R$ 144.00** |
| 9 | 1000.00 | 80 | 20% | 10% | **R$ 720.00** |
| 10 | 200.00 | 64 | 0% | 10% | **R$ 180.00** |

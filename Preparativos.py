
bolo = float (input("Diga o valor do bolo: "))


salgado1v = float(input("Qual o valor do salgado 1? "))
salgado1q = float(input("Quantas unidades voces compraram? "))

salgado2v = float(input("Qual o valor do salgado 2? "))
salgado2q = float(input("Quantas unidades voces compraram? "))

salgado3v = float(input("Qual o valor do salgado 3? "))
salgado3q = float(input("Quantas unidades voces compraram? "))

salgado1 = salgado1v * salgado1q
salgado2 = salgado2v * salgado2q
salgado3 = salgado3v * salgado3q

colegas = 10

total = salgado1 + salgado2 + salgado3 + bolo

total_dividido = total / colegas

print("O valor total e: ", total)
print("O valor dividido e: ",total_dividido)

aluno1 = str(input("Qual do  aluno? "))

nota1 = float(input("Qual a primeira nota? "))

nota2 = float (input("Qual a segunda nota? "))

nota3 = float (input("Qual a terceira nota? ")) 

media1 = (nota1*2)+(nota2*3)+(nota3*5)
mediafinal =  media1 / 10

if mediafinal <= 4.9: 
  print(aluno1)  
  print("Reprovado")
elif mediafinal >= 5 and mediafinal <= 6.9:
  print(aluno1)
  print("recuperação") 
else:
 print(aluno1, "foi aprovado")

 
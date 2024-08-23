#Construa um pseudocódigo que informe se o aluno foi aprovado, reprovado ou fará uma nova avaliação
Nota1 = int(input("Digite um número:"))
Nota2 = int(input("Digite um número:"))
Nota3 = int(input("Digite um número:"))
media = (Nota1+Nota2+Nota3)/3

if media >= 70:
    print("aprovado")
elif media >= 50 and media < 70:
    print("nova avaliação")
else:
    print("reprovado")
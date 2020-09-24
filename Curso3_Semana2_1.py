import re

fname=input("Enter the file name: ")
fhand=open(fname)
num_list=list()
p=list()
x=list()
soma=0
for line in fhand:
    line=line.rstrip() #ok
    if re.search('[0-9.]+',line): #se tiver numero na linha
        p=re.findall('([0-9]+)',line) # p vai receber uma lista com os numeros da linha
        for i in range(len(p)):
            num=int(p[i])#convertendo os numeros de caractere para float
            x.append(num) #adicionando na lista
    else: continue #se nao tem numero na linha, continua o loop
#print(x)
i=0
for i in range(len(x)):
    soma+=x[i]
    #cont+=1
print("Sum", int(soma))
#print("Contador ", cont)

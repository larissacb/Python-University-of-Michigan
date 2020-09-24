import urllib.request
import re
from bs4 import BeautifulSoup

url=input("Enter - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
x=list()
p=list()
sum=0
num=0
# Retrieve all of the anchor tags
tags = soup('span') #filtrar todas as tags de spam do codigo html
#print(type(tags)) #tags nao e list. tem que converter para string
for tag in tags:
    y=str(tag) #convertendo para string para fazer a analise
    if re.search('[0-9.]+',y): #se tiver numero na string da linha
        p=re.findall('([0-9]+)',y) # p vai receber uma lista com os numeros string da linha
        for i in range(len(p)):
            num=int(p[i])#convertendo os numeros de caractere para float
            sum+=num
            x.append(num) #adicionando na lista
    else: continue #se nao tem numero na string da linha, continua o loop

print("Sum", sum)

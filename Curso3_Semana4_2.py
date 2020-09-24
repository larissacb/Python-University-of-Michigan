import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

total=0
url = input('Enter - ')
c=input('Repeticao do programa -')
count=int(c)
p=input('Posicao do link -')
pos=int(p)
while total<=count:
    html = urllib.request.urlopen(url).read()
    print("Retrieving",url) #imprimindo o site da posicao e o inicial
    soup = BeautifulSoup(html, 'html.parser')#convertendo o html
    tags = soup('a')#procurando pelas tags de links no html
    counter=0 #contador da posicao do link dentro do loop
    for tag in tags:
        counter+=1
        if(counter<=pos):#enquanto o contador interno nao chegar no valor informado, fica atualizando os links
            x=tag.get('href',None) #a chave da questao esta em que x ja e o link completo. nao tenho que usar expressoes regulares
            url=x #url recebe o link para a proxima iteracao do loop while
        else: #quando chega no link, o for e quebrado
            break
    total+=1


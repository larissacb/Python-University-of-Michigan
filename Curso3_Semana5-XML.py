import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

link = input('Enter location: ')
html = urllib.request.urlopen(link).read().decode() #acessando o site fornecido
print('Retrieving', link)
print('Retrieved', len(html), 'characters')

cn = 0
sm = 0
data = ET.fromstring(html) #objeto do tipo arvore de elementos
tags = data.findall('comments/comment')
#print(tags)
#print(type(data))

for tag in tags:
    cn += 1 #contador de iteracoes
    sm += int(tag.find('count').text) #encontrar o texto da tag count

print('Count:', cn)
print('Sum:', sm)

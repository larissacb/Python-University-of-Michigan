fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
count = 0
emails=list()
fh = open(fname)
for line in fh:
    line=line.rstrip()
    if line.startswith('From '): #verificando se a linha comeca com from
        count=count+1 #incremetando o contador
        fline=line.split() #separando todos as strings da linha
        emails.append(fline[1]) #salvando os emails na lista
        
#mexendo agora com o dicionario
dicemails=dict()#dicionario para os emails
for email in emails:
    dicemails[email]=dicemails.get(email,0)+1 #add os emails ao dicionario e contando a frequencia de repeticao

lista=list(dicemails.keys()) #criando lista com as chaves do dicionario - emails
nums=list(dicemails.values()) #criando lista com a frequencia de repeticao dos emails

num=0
index=0
for i in range(len(nums)):
    nums[i]=int(nums[i])
    if num<nums[i]: 
        num=nums[i] #salvando a maior frequencia em num
        index=i #salvando a posicao da maior frequencia
print(lista[index], nums[index])

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
hours=list()
fh = open(fname)
string=''
for line in fh:
    line=line.rstrip()
    if line.startswith('From '): #verificando se a linha comeca com from
        fline=line.split() #separando todos as strings da linha
        string = fline[5] #retirando somente o horario
        string=string[0:2] #cortando a hora
        hours.append(string) #salvando a hora na lista
        
#mexendo agora com o dicionario
dic_hours=dict()#dicionario para as horas
for hour in hours:
    dic_hours[hour]=dic_hours.get(hour,0)+1 #add as horas ao dicionario e contando a frequencia de repeticao

#organizando na ordem - chave: hora - valor: frequencia de repeticao
for key, value in sorted(dic_hours.items()):
    print(key, value)

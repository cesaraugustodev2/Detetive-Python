#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.

respo=[]  #declaração de lista vazia para armazenar as respostas
def perguntar(p:str): #método para perguntar para o usuário 
            print(p) # aqui é informado a pergunta para o usuário
            r = input()
            r = r.capitalize()
            if 'Sim'  in r:#testa se a palavra Sim está contida na resposta
                print("Você disse que Sim, vamos continuar")
                respo.append(r)#add a resposta na lista
            elif 'Não' in r:#testa se a palavra Não está contida na resposta
                print("Você disse que  Não, vamos continuar")
                respo.append(r)#add a resposta na lista
            else:#caso a resposta não seja sim ou não o detetive irá parar o questionário
                print("Você está muito nervoso para responder agora, vamos continuar depois")
                exit()#força o encerramento do script
#lógica do detetive
print("Responda somente Sim ou Não para as seguintes perguntas: ")
perguntar("Telefonou para a vitima?")
perguntar("Esteve no local do crime?")
perguntar("Mora perto da vítima?")
perguntar("Devia para a vítima?")
perguntar("Já trabalhou com a vítima?")
s = respo.count("Sim")# conta quantas vezes a palavra sim aparece na lista
if s<2: #1 resposta sim
    print("De acordo com nossas investigações e as respostas do seu questionário, consideramos você Inocente" 
    +"\n" +"<Você respira aliviado enquanto sai pela porta da frente da delegácia.>")
if s==2: #2 respostas sim
    print("De acordo com nossas investigações e as respostas do seu questionário, consideramos você Suspeito" 
    +"\n" +"<Você sai pela porta da frente da delegacia, porém ainda será investigado>")
if s==2 and s<4: #3 ou 4 respostas sim
    print("De acordo com nossas investigações e as respostas do seu questionário, consideramos você Cumplice" 
    +"\n" +"<Você é algemado enquanto um policial lê os seus direitos constitucionais>")
    if s==5:#5 respostas sim
     print("De acordo com nossas investigações e as respostas do seu questionário, consideramos você Culpado pelo asssassinato" 
    +"\n" +"<Você é algemado enquanto um policial lê os seus direitos constitucionais>")
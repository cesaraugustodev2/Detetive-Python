# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Versão de linha de comando
import time
def main():
    respo = []
    global c
    c = 0

    def perguntar(p: str): # método para perguntar para o usuário
        global c
        # conta quantas vezes a palavra sim aparece na lista
        s = respo.count("Sim")
        print(p)  # aqui é informado a pergunta para o usuário
        r = input()
        r = r.capitalize()
        if r[0] =='S':  # testa se a palavra Sim está contida na resposta
            r = "Sim"
            print("Você disse que Sim, vamos continuar")
            respo.append(r)  # add a resposta na lista
        elif r[0] =='N':  # testa se a palavra Não está contida na resposta
            r = "Não"
            print("Você disse que  Não, vamos continuar")
            respo.append(r)
        else:  # caso a resposta não seja sim ou não o detetive irá perguntar novamente
            if c < 2:
                print("Resposta invalida,responda apenas Sim ou Não")
                c += 1
                perguntar(p)

            else:
                print(
                    "Você está muito nervoso para responder agora, vamos tentar de novo depois")
            exit()

    # lógica do detetive
    print("Responda somente Sim ou Não para as seguintes perguntas: ")
    perguntar("Telefonou para a vitima?")
    perguntar("Esteve no local do crime?")
    perguntar("Mora perto da vítima?")
    perguntar("Devia para a vítima?")
    perguntar("Já trabalhou com a vítima?")
    print("Processando respostas....")
    s = respo.count('Sim')
    time.sleep(3)
    print(respo)
    print(s)
    if s < 2:  # 1 resposta sim
        print("De acordo com nossas investigações e as respostas do seu questionário, consideramos você Inocente"
              + "\n" + "<Você respira aliviado enquanto sai pela porta da frente da delegácia.>")
    elif s == 2:  # 2 respostas sim
        print("De acordo com nossas investigações e as respostas do seu questionário, consideramos você Suspeito"
              + "\n" + "<Você sai pela porta da frente da delegacia, porém ainda será investigado>")
    elif s > 2 and s < 5:  # 3 ou 4 respostas sim
        print("De acordo com nossas investigações e as respostas do seu questionário, consideramos você Cumplice"
              + "\n" + "<Você é algemado enquanto um policial lê os seus direitos constitucionais>")
    else:  # 5 respostas sim
            print("De acordo com nossas investigações e as respostas do seu questionário, consideramos você Culpado pelo asssassinato"
                  + "\n" + "<Você é algemado enquanto um policial lê os seus direitos constitucionais>")

if __name__ == '__main__':
    main()

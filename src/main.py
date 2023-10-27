import random

# Uma das "boas práticas" é a utilização de variáveis em inglês e com nomes "verbificados"
def playerPontuationCalc(countOfWins, countOfLoses): #função focada apenas no calculo entre os valores que serão insertados de forma aleatório pela biblioteca "random"
    # Assim como ensinado como "boas práticas" definir funções para uma função específica
    resultado = countOfWins - countOfLoses
    return resultado # Retorno de calculo 


def pontuationRanking(playerPontuation): #função focada em extrair o ranking do jogador, de acordo com o valor definido no bloco def acima
    if playerPontuation < 10:
        playerPontuation = 'Ferro'
    elif 11 <= playerPontuation <= 20:
        playerPontuation = 'Bronze'
    elif 21 <= playerPontuation <= 50:
        playerPontuation = 'Prata'
    elif 51 <= playerPontuation <= 80: 
        playerPontuation = 'Ouro'
    elif 81 <= playerPontuation <= 90:
        playerPontuation = 'Diamente'
    elif 91 <= playerPontuation <= 100:
        playerPontuation = 'Lendário'
    elif playerPontuation >= 101:
        playerPontuation = 'Imortal'
    return playerPontuation

def main(): #função principal, responsável por tratar a lógica e fazer as impressões no prompt para o usuário
    pontuationNumbers = playerPontuationCalc(random.randint(1, 101), random.randint(1, 101))
    finalRanking = pontuationRanking(pontuationNumbers)
    if pontuationNumbers < 0:
        print(f'Seu herói possui mais derrotas do que vitórias! portanto.. você não possui ranking!')
    else:
        print (f'Seu herói possui um saldo de "{pontuationNumbers}" vitórias!, e seu ranking atual é: "{finalRanking}"')
    
main()
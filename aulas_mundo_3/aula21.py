#Parte 2 Aulas função
#Interactive Help
#help() no console aparece um terminal para ajuda
#print(input.__doc__) mesmo de help

#docstrings:
#importar uma função com uma descritiva explicando o uso da função. Ex:
#para criar uma docstring, colocar entre """""" (aspas duplas, triplas)



def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: número de inicio da contagem
    :param f: final da contagem
    :param p:passo da contagem
    :return: não retorna
    """
    c = i
    while c<= f:
        print(f'{c}', end=' ')
        c+=p
    print('FIM!')


help(contador)


#Parametros Opcionais

def somar(a,b,c=0): #se c não receber nenhum valor, ele recebe 0
    #somar(a=0,b=0,c=0) nenhum parametro seria obrigatório receber um número, podendo somar 0 + 0 + 0 
    s = a + b + c


somar(3,2)


#escopo de variaveis
#depende de onde a variável for alocada. EX:
def teste():
    x = 8 #por estar dentro da identação do def teste, x só vale 8 quando a função for chamada (variavel local)
    print(f'Na função teste n vale {n} e x vale {x}')


n = 2 #por estar fora de qualquer identação, n tem valor em qualquer lugar do código (variável global)
print(f'Na função principal, n vale {n} e x não tem valor')


#return
#def somar(a=0,b=0,c=0):
#    s = a + b + c
#    return s


#r1 = somar(3,2,5)
#r2 = somar(4,2)
#r3 = somar(5,c=3)
#print(f'As somas valem {r1}, {r2}, {r3} a soma dos 3 vale {r1 + r2 + r3}')


def par(n=0):
    if n % 2==0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print(f'{num} É par')
else:
    print(f'{num} Não é par')


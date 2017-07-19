def primo(n,i,j):
    if i>j:
        return False
    elif n%i==0:
        return True
    else:
        return primo(n,i+1,j)

    
def verificarPrimo(n):
    return n>1 and not (primo(n,2,n-1))

n=int(input('Número'))
resposta=verificarPrimo(n)
print(resposta)














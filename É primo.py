 
def numero_divisores(n):

 
 div = 0
 
 for i in range(1,n+1):
  
   
   if (n % i) == 0:
    div=div+1

 return div
 
   
x=int(input("numero"))
resposta=numero_divisores(x)
if resposta==2:
 print("é primo")
else:
  print("não é Primo")  



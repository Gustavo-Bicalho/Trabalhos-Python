print("Verificação de Numeros primos")

for numero in range(1,101): # Ta puxando o laço de repetição de 1 até 100
    if numero > 1: 
        eh_primo = True # Se o numero for maior que 1 vai seguir pra proxima etapa de verificação

        for i in range(2,int(numero ** 0.5) + 1): # Esse for esta realizando a verificação se o numero e divisivel a partir de 2 ate sua raiz quadrada
            if numero % i == 0: 
                eh_primo = False # Se o resto da divisão do numero for zero quer dizer que ele foi divido por algum numero e mostra ue ele não é primo
                break # Vai quebrar o looping se o numero não for primo
        if eh_primo:
            print(numero, "É primo") # Condição de que se o numero for primo vai mostrar ele e colocar a mensagem de que é primo
 
